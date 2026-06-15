# engine/match.py
"""
整场比赛管理：阵营分配、四小局循环、总分计算。
"""

# 临时引入，后续逐步替换为真实模块
# from .round import GameRound
# from .player import Player

class Player:
    """
    玩家临时数据类，后续从独立模块引入。
    """
    def __init__(self, player_id, name):
        self.id = player_id
        self.name = name
        self.camp = None          # 'A' 或 'B'
        self.is_captain = False   # 是否为队长
        self.total_score = 0      # 总分

class Match:
    """
    一场村长扑克比赛 = 4 小局。
    """

    def __init__(self, player_names):
        """
        初始化四名玩家并分配固定座次 A-B-A-B。
        """
        # 创建玩家对象
        self.players = [
            Player(0, player_names[0]),
            Player(1, player_names[1]),
            Player(2, player_names[2]),
            Player(3, player_names[3]),
        ]
        # 分配阵营
        self.players[0].camp = 'widow'
        self.players[1].camp = 'village'
        self.players[2].camp = 'widow'
        self.players[3].camp = 'village'

        # 记录每一小局的详细结果（供界面或复盘使用）
        self.round_history = []

    def run_full_match(self) -> str:
        """
        执行完整四小局流程，返回获胜阵营。
        """
        print("===== 村长扑克 比赛开始 =====")
        for round_num in range(1, 5):
            # 个人得分字典
            personal_scores = self._run_one_round(round_num)

            # 计算阵营单局得分
            camp_a_round = sum(personal_scores[p.id] for p in self.players if p.camp == 'A')
            camp_b_round = sum(personal_scores[p.id] for p in self.players if p.camp == 'B')

            # 存储本局信息
            self.round_history.append({
                'round': round_num,
                'personal': personal_scores.copy(),
                'camp' : {'A': camp_a_round, 'B': camp_b_round}
            })

            # 累加个人总分
            for p in self.players:
                p.total_score += personal_scores[p.id]

            # 输出单局结果
            print("本局个人得分:")
            for p in self.players:
                role = '队长' if p.is_captain else '队员'
                role = "队长" if p.is_captain else "队员"
                print(f"  {p.name}（{role}）: {personal_scores[p.id]}")
            print(f"本局阵营得分：A={camp_a_round}, B={camp_b_round}")
        # 比赛结束，汇总
        print("\n===== 比赛结束 =====")
        final_camp_a = sum(p.total_score for p in self.players if p.camp == 'A')
        final_camp_b = sum(p.total_score for p in self.players if p.camp == 'B')
        print("个人累计总分：")
        for p in self.players:
            print(f"  {p.name}: {p.total_score}")
        print(f"阵营总分：A={final_camp_a}, B={final_camp_b}")
        # 胜负判定
        if final_camp_a > final_camp_b:
            print("获胜阵营：A")
            return 'A'
        elif final_camp_b > final_camp_a:
            print("获胜阵营：B")
            return 'B'
        else:
            print("结果：平局")
            return '平局'

    def _run_one_round(self, round_num: int) -> dict:
        """
        执行一个小局（当前为占位符，将来替换为真正的GameRound
        :return: {玩家id:得分}
        """
        # TODO: 替换为真实对局逻辑
        print("（当前为占位符，未实现真正对局流程）")
        # 占位得分示例：第1名队长5分，第2名队员3分，第3名队长2分，第4名队员1分
        # 假设玩家0（A队长）第1，玩家1（B队员）第2，玩家2（A队员）第3，玩家3（B队长）第4
        return {0: 5, 1: 3, 2: 2, 3: 1}