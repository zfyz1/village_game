
"""
扑克牌点数、花色、牌型定义以及显示映射的常量模块。
"""
from enum import IntEnum


# ---------------------------------------------------------------------------
# 点数枚举（3 最小，大王最大）
# ---------------------------------------------------------------------------
class Rank(IntEnum):
    """
    村长扑克中所有可能的牌点，数值即为大小顺序：
    3 最小，大王最大。
    """
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14
    TWO = 15
    SMALL_JOKER = 16
    BIG_JOKER = 17


# ---------------------------------------------------------------------------
# 供界面或调试使用的显示名映射
# ---------------------------------------------------------------------------
class Suit(IntEnum):
    """
    扑克牌花色，JOKER 专门用于大小王。
    """
    SPADE = 4      # 黑桃
    HEART = 3      # 红桃
    CLUB = 2       # 梅花
    DIAMOND = 1    # 方块
    JOKER = 0      # 大小王（花色不区分）


# ---------------------------------------------------------------------------
# 供界面或调试使用的显示名映射
# ---------------------------------------------------------------------------
RANK_DISPLAY = {
    Rank.THREE: '3',
    Rank.FOUR: '4',
    Rank.FIVE: '5',
    Rank.SIX: '6',
    Rank.SEVEN: '7',
    Rank.EIGHT: '8',
    Rank.NINE: '9',
    Rank.TEN: '10',
    Rank.JACK: 'J',
    Rank.QUEEN: 'Q',
    Rank.KING: 'K',
    Rank.ACE: 'A',
    Rank.TWO: '2',
    Rank.SMALL_JOKER: '小王',
    Rank.BIG_JOKER: '大王',
}

SUIT_DISPLAY = {
    Suit.SPADE: '♠',
    Suit.HEART: '♥',
    Suit.CLUB: '♣',
    Suit.DIAMOND: '♦',
    Suit.JOKER: '',          # 大小王没有花色符号
}


# ---------------------------------------------------------------------------
# 牌型枚举
# ---------------------------------------------------------------------------
class HandType(IntEnum):
    """
    All valid hand patterns in Village Chief Poker.
    """
    PASS = 0               # 要不起
    SINGLE = 1             # 单张
    PAIR = 2               # 对子
    STRAIGHT = 3           # 顺子（≥5张连续，3~A）
    STRAIGHT_PAIRS = 4     # 连对（≥3对连续，3~A）
    THREE_WITH_PAIR = 5    # 三带二（三条+对子）
    BOMB = 6               # 炸弹（≥4张相同点数）
    KING_BOMB = 7          # 天王炸（两大王+两小王）


# 牌型对应的中文名称
HAND_TYPE_NAMES = {
    HandType.PASS: '要不起',
    HandType.SINGLE: '单张',
    HandType.PAIR: '对子',
    HandType.STRAIGHT: '顺子',
    HandType.STRAIGHT_PAIRS: '连对',
    HandType.THREE_WITH_PAIR: '三带二',
    HandType.BOMB: '炸弹',
    HandType.KING_BOMB: '天王炸',
}


# ---------------------------------------------------------------------------
# 顺子和连对允许的点数序列（仅 3 ~ A，2 不参与）
# ---------------------------------------------------------------------------
STRAIGHT_SEQUENCE = [
    Rank.THREE, Rank.FOUR, Rank.FIVE, Rank.SIX, Rank.SEVEN,
    Rank.EIGHT, Rank.NINE, Rank.TEN, Rank.JACK, Rank.QUEEN,
    Rank.KING, Rank.ACE
]


# ---------------------------------------------------------------------------
# 天王炸固定组合（排序后应为两大王 + 两小王）
# ---------------------------------------------------------------------------
KING_BOMB_RANKS = [Rank.BIG_JOKER, Rank.BIG_JOKER, Rank.SMALL_JOKER, Rank.SMALL_JOKER]