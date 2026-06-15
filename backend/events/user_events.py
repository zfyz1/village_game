# 注册所有 SocketIO 事件处理函数
# 1 标准库
import uuid
# 2 第三方库
from flask import request
from flask_socketio import emit
# 3 本地模块
from core.player_store import player_store, PlayerInfo

def register_user_events(socketio):
    """注册所有用户相关的 SocketIO 事件"""
    @socketio.on('connect')
    def handle_connect():
        # 处理连接
        emit('connected',{'message':'connected to server'})

    @socketio.on('disconnect')
    def handle_disconnect():
        sid = request.sid
        player = player_store.get_by_sid(sid)
        # 删除玩家
        player_store.remove_by_sid(sid)
        # 如果有玩家，广播离开消息
        if player:
            emit('player_left', {
                'player_id': player.player_id,
                'nickname': player.nickname,
                'online_count': player_store.count()
            }, broadcast=True)

    @socketio.on('login')
    def handle_login(data):
        sid = request.sid

        nickname = data.get('nickname')
        # 1. 校验
        if not nickname or not nickname.strip():
            emit('login_error', {'message': '昵称不能为空'})
            return

        # 2. 检查是否已经登录（sid 重复）
        existing = player_store.get_by_sid(sid)
        if existing:
            # 已经登录过，直接返回旧信息
            emit('login_success', {
                'player_id': existing.player_id,
                'nickname': existing.nickname
            })
            return

        # 3. 生成 player_id
        player_id = str(uuid.uuid4())[:8]

        # 4. 生成并存储 PlayerInfo
        info = PlayerInfo(player_id=player_id, nickname=nickname.strip(), sid=sid)
        player_store.add(info)  # ← 用的是实例 player_store，不是类 PlayerStore

        # 5. 返回成功
        emit('login_success', {
            'player_id': info.player_id,
            'nickname': info.nickname
        })

        # 6. 广播给其他人
        emit('player_joined', {
            'player_id': info.player_id,
            'nickname': info.nickname,
            'online_count': player_store.count()
        }, broadcast=True, include_self=False)

    @socketio.on('get_players')
    def handle_get_players():
        players = player_store.get_all()
        player_list = [
            {'player_id': p.player_id, 'nickname': p.nickname}
            for p in players.values()
        ]
        emit('players_list', {
            'players': player_list,
            'online_count': len(player_list)
        })

