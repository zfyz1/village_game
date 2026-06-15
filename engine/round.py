"""
单局游戏流程控制器。
驱动一局完整的村长扑克：猜拳 → 发牌 → 选队长 → 出牌循环 → 计分。
本模块依赖 card（牌和牌组）、patterndef（枚举常量）、hand（牌型识别/比较）。
所有游戏状态在本类内部维护，不污染玩家对象。
"""
# 1 第一方库
import random
from typing import List

# 3 项目内
from engine.card import Card,DeckFactory

class GameRound:
    """
        管理村长扑克中一个完整小局的流程。
    """
    def __init__(self, players: List, round_num: int):
        """
           :param players: 长度为4的 Player 对象列表，已按 wid-vil-wid-vil 座次排列。
           :param round_num: 当前小局编号 (1~4)
       """
        self.players = players
        self.deck: List[Card] = []
        self.hands: List[List[Card]] = []  # 手牌容器嵌套List
        self.winner_camp: str = ""  # 猜拳胜方阵营

    def _guss_first(self):
        """
        从寡妇帮和村长帮，各随机抽取一人猜拳，胜利的一方获得先手出牌权
        :return:
        """
        widow_indices = [i for i, p in enumerate(self.players) if p.camp == 'widow']
        village_indices = [i for i, p in enumerate(self.players) if p.camp == 'village']
        # TODO: 暂时简化成随机
        self.winner_camp = random.choice(['widow', 'village'])
        print(f"[猜拳] 胜方阵营: {self.winner_camp}")

    def _deal(self):
        """
        发牌阶段：从猜拳获胜方开始发牌，两副牌4人均分
        :return:
        """

        # 创建牌组
        full_deck = DeckFactory.create_double_deck()

        # 洗牌
        shuffled = DeckFactory.shuffle(full_deck)

        # 分配手牌
        self.hands = DeckFactory.deal(shuffled, 4)

        # 枚举
        for i, hand in enumerate(self.hands):
            p = self.players[i]
            print(f"[发牌] {p.name}({p.camp}) 手牌 {len(hand)} 张")

    def _select_captains(self):
        """
        选择队长，仅在第一回合生效
        实际为30秒倒计时交互
        :return:
        """
        for camp in ('widow', 'village'):
            camp_indices = [i for i, p in enumerate(self.players) if p.camp == camp]


    def _play_loop(self):
        """
        出牌主循环,管理从第一手到所有人手牌清空的全过程
        :return:
        """
        # 确定先手
        # 执行循环，直到场上玩家只剩一个
        # 游戏结束，退出循环

