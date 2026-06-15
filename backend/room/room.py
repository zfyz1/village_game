"""
通用房间数据结构
不包含任何具体游戏的业务逻辑
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum


class RoomStatus(Enum):
    WAITING = "waiting"
    PLAYING = "playing"



@dataclass
class Room:
    """通用房间实体　以及房间内部操作"""

    # 基础信息
    room_id: str    #　房间唯一id
    room_type: str  # 'rps', 'poker', 'chess'
    owner_id: str   #  房主id
    max_players: int
    # 玩家相关
    player_ids: List[str] = field(default_factory=list)


    # 房间状态
    status: RoomStatus = RoomStatus.WAITING

    # === 准备状态 ===
    ready_status: Dict[str, bool] = field(default_factory=dict)

    # ========== 玩家操作 ==========

    def add_player(self, player_id: str) -> bool:
        """添加玩家"""
        if player_id in self.player_ids:
            return False
        if len(self.player_ids) >= self.max_players:
            return False
        if self.status != RoomStatus.WAITING:
            return False

        self.player_ids.append(player_id)
        self.ready_status[player_id] = False
        return True

    def remove_player(self, player_id: str) -> bool:
        """移除玩家"""
        if player_id not in self.player_ids:
            return False

        self.player_ids.remove(player_id)
        self.ready_status.pop(player_id, None)

        # 如果房主离开，转让给第一个玩家
        if player_id == self.owner_id and self.player_ids:
            self.owner_id = self.player_ids[0]

        return True

    def get_player(self, player_id: str) -> Optional[dict]:
        """获取玩家信息"""
        if player_id not in self.player_ids:
            return None
        return {
            'player_id': player_id,
            'is_ready': self.ready_status.get(player_id, False)
        }

    def get_players(self) -> List[dict]:
        """获取所有玩家列表"""
        return [
            {'player_id': pid, 'is_ready': self.ready_status.get(pid, False)}
            for pid in self.player_ids
        ]

    def get_player_count(self) -> int:
        """获取玩家数量"""
        return len(self.player_ids)

    def is_full(self) -> bool:
        """房间是否已满"""
        return len(self.player_ids) >= self.max_players

    def is_empty(self) -> bool:
        """房间是否为空"""
        return len(self.player_ids) == 0

    def has_player(self, player_id: str) -> bool:
        """检查玩家是否在房间"""
        return player_id in self.player_ids

    # ========== 准备操作 ==========

    def set_ready(self, player_id: str, is_ready: bool) -> bool:
        """设置玩家准备状态"""
        if player_id not in self.player_ids:
            return False
        if self.status != RoomStatus.WAITING:
            return False
        self.ready_status[player_id] = is_ready
        return True

    def all_ready(self) -> bool:
        """是否所有玩家都已准备"""
        if len(self.player_ids) != self.max_players:
            return False
        return all(self.ready_status.get(pid, False) for pid in self.player_ids)

    def reset_ready(self):
        """重置所有玩家的准备状态"""
        for pid in self.player_ids:
            self.ready_status[pid] = False
    # ========== 游戏流程 ==========

    def can_start(self) -> bool:
        """是否可以开始游戏"""
        return (
                self.status == RoomStatus.WAITING and
                len(self.player_ids) == self.max_players and
                self.all_ready()
        )

    def start_game(self) -> bool:
        """开始游戏"""
        if not self.can_start():
            return False
        self.status = RoomStatus.PLAYING
        return True

    def end_game(self) -> bool:
        """结束游戏（重置为等待状态）"""
        if self.status != RoomStatus.PLAYING:
            return False
        self.status = RoomStatus.WAITING
        self.reset_ready()
        return True