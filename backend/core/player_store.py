from dataclasses import dataclass

# ========== 数据结构 ==========
@dataclass
class PlayerInfo:
    player_id: str
    nickname: str
    sid: str

# ========== 存储操作 ==========
class PlayerStore:
    def __init__(self):
        self._players = {}      # player_id -> PlayerInfo
        self._sid_to_pid = {}   # sid -> player_id

    def add(self, info: PlayerInfo):
        self._players[info.player_id] = info
        self._sid_to_pid[info.sid] = info.player_id

    def remove_by_sid(self, sid: str) -> str:
        player_id = self._sid_to_pid.pop(sid, None)
        if player_id:
            self._players.pop(player_id, None)
        return player_id

    def get_by_pid(self, player_id: str) -> PlayerInfo | None:
        return self._players.get(player_id)

    def get_by_sid(self, sid: str) -> PlayerInfo | None:
        player_id = self._sid_to_pid.get(sid)
        return self._players.get(player_id) if player_id else None

    def count(self) -> int:
        return len(self._players)

    def get_all(self) -> dict:
        """返回所有在线玩家 {player_id: PlayerInfo}"""
        return self._players.copy()  # 返回副本，防止外部意外修改


# ========== 全局单例 ==========
player_store = PlayerStore()