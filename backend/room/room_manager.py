
# 1. 内部
import uuid
from typing import Dict, Tuple, Optional, List

# 3. 项目内部
from .room import Room, RoomStatus


class RoomManager:
    def __init__(self):

        self._rooms:Dict[str,Room] = {}  # 房间列表 id->Room(实体）
        self._player_to_room: Dict[str, str] = {}

    def create_room(self,
        room_type: str,
        owner_id: str,
        max_player:int,
                    )-> Tuple[bool, str, Optional[Room]]:
        """
        :param room_type:  游戏类型
        :param owner_id:   房主id
        :param max_player: 房间最大人数
        """
        room_id  = f"{room_type}_{uuid.uuid4().hex[:6]}"
        room = Room(room_id=room_id,
                    room_type=room_type,
                    owner_id=owner_id,
                    max_players=max_player
                    )

        room.add_player(owner_id)

        self._rooms[room_id] = room
        self._player_to_room[owner_id] = room_id

        return True, '创建房间成功', room

    def join_room(self, player_id:str, room_id:str)-> Tuple[bool, str, Optional[Room]]:
        """
        玩家加入房间
        :param player_id: 玩家ID
        :param room_id:   房间id
        :return:
        """
        #　检查玩家是否已在其他房间
        if player_id in self._player_to_room:
            return False, " 你已经在其他房间了 ", None

        room =self._rooms.get(room_id)
        if not room:
            return False, "房间不存在", None

        if room.status != RoomStatus.WAITING:
            return False, "无法中途加入", None

        if not room.add_player(player_id):
            return False, " 房间已经满了 ", None

        self._player_to_room[player_id] = room_id
        return True,"加入成功", room

    def leave_room(self, player_id:str) ->Tuple[bool, str, Optional[Room]]:
        """
        玩家离开房间
        :param player_id: 玩家id
        """
        room_id = self._player_to_room.pop(player_id,None)

        if not room_id:
            return False, " 非法操作，你不在任何房间", None

        room = self._rooms.get(room_id)
        if not room:
            return False, " 房间不存在", None

        room.remove_player(player_id)

        # 如果房间没人了，删除房间
        if room.is_empty():
            self._rooms.pop(room_id, None)
        else:
            # 更新房间状态(如果游戏进行中）
            if room.status == RoomStatus.PLAYING:
                room.end_game()

        return True, "已离开房间", room

    # ========== 查询操作 ==========
    def get_room(self, player_id: str) -> Optional[Room]:
        """获取玩家所在的房间"""
        room_id = self._player_to_room.get(player_id)
        if room_id:
            return self._rooms.get(room_id)
        return None

    def get_all_rooms(self) -> List[Room]:
        """获取所有房间列表"""
        return list(self._rooms.values())

    def get_room_player_count(self, room_id: str) -> int:
        """获取房间玩家数量"""
        room = self._rooms.get(room_id)
        return room.get_player_count() if room else 0

    # ========== 房间状态操作 ==========
    def set_ready(self, player_id: str, is_ready: bool) -> Tuple[bool, str, Optional[Room]]:
        """设置玩家准备状态"""
        room = self.get_room(player_id)
        if not room:
            return False, "你不在任何房间", None

        if not room.set_ready(player_id, is_ready):
            return False, "无法设置准备状态", None

        return True, "操作成功", room

    def start_game(self, player_id: str) -> Tuple[bool, str, Optional[Room]]:
        """开始游戏（房主或准备就绪时调用）"""
        room = self.get_room(player_id)
        if not room:
            return False, "你不在任何房间", None

        if player_id != room.owner_id:
            return False, "只有房主可以开始游戏", None

        if not room.can_start():
            return False, "无法开始游戏：人数不足或未全部准备", None

        room.start_game()
        return True, "游戏开始", room

    def end_game(self, room_id: str) -> Tuple[bool, str, Optional[Room]]:
        """结束游戏（比赛分出胜负后调用）"""
        room = self._rooms.get(room_id)
        if not room:
            return False, "房间不存在", None

        room.end_game()
        return True, "游戏结束", room
# 全局单例
room_manager = RoomManager()
