# engine/player.py
"""
玩家数据模型：存储身份、阵营、得分等信息。
阵营名称与角色称谓如下：
    - widow  阵营：队长 = "寡妇"，队员 = "主任"
    - village 阵营：队长 = "村长"，队员 = "书记"
"""

class Player:
    """
    村长扑克中的一名玩家。
    """

    # 阵营 → (队长称谓, 队员称谓)
    ROLE_NAMES = {
        'widow':   ('寡妇', '主任'),
        'village': ('村长', '书记'),
    }

    def __init__(self, player_id: int, name: str):
        """
        :param player_id: 唯一标识，通常 0~3
        :param name: 显示名称（玩家昵称）
        """
        self.id = player_id
        self.name = name

        # 阵营：'widow' 或 'village'，由 Match 分配
        self.camp = None

        # 是否为本局队长（每小局开始前选定）
        self.is_captain = False

        # 整场比赛个人累计得分
        self.total_score = 0

    @property
    def role_name(self) -> str:
        """
        根据当前阵营与队长身份返回角色称谓。
        例如：寡妇阵营的队长 → "寡妇"，村长阵营的队员 → "书记"。
        """
        if self.camp not in self.ROLE_NAMES:
            return "未知"
        captain_title, member_title = self.ROLE_NAMES[self.camp]
        return captain_title if self.is_captain else member_title

    def __repr__(self):
        return f"{self.name}({self.camp} {self.role_name})"