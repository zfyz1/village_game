"""
手牌分析：牌型识别、比较与提取
主要职责
-牌型识别：给定一组牌，判断它属于哪种合法牌型，并提取关键信息（主点数、长度等）。
-大小比较：判断一手牌是否能压过另一手牌。
-合法出牌检查：结合当前轮次状态（是否是自由出牌权、上一手牌是什么），判断玩家出牌是否合规。
-可出牌型列举：从一手牌中找出所有能压过上一手牌的合法组合（供 AI 或提示使用）。
"""
from patterndef import HandType, Rank, HAND_TYPE_NAMES, STRAIGHT_SEQUENCE, KING_BOMB_RANKS
class HandPattern:
    """
    用于描述一手牌的结构信息
    - hand_type: 当前手牌的牌型
    - main_rank: 当前手牌的点数(AAA22:点数为A,345678:点数为8)
    - length: 当前手牌的长度，用于连对和顺子和炸弹的比较
    - extra: 额外信息
    """
    def __init__(self, hand_type:HandType, main_rank:Rank, length: int, extra: int =0 ):
        self.hand_type = hand_type
        self.main_rank = main_rank
        self.length    = length
        self.extra     = extra

    def __repr__(self):
        """
        魔法方法， 调试用字符串
        """
        # 当要不起当前牌型时，显示要不起
        if self.hand_type == HandType.PASS:
            return HAND_TYPE_NAMES[HandType.PASS]

        desc = HAND_TYPE_NAMES[self.hand_type]
