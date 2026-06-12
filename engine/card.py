# engine/card.py
"""
Card representation and deck management for Village Chief Poker.
"""
import random

from .patterndef import Rank, Suit, RANK_DISPLAY, SUIT_DISPLAY


class Card:
    """A single playing card defined by suit and rank."""

    __slots__ = ('suit', 'rank')  # 节省内存，防止动态添加属性

    def __init__(self, suit: Suit, rank: Rank) -> None:
        self.suit = suit
        self.rank = rank

    # ---- 显示 ----
    def __repr__(self) -> str:
        """可读的牌面表示，例如 ♠A 或 小王"""
        if self.suit == Suit.JOKER:
            return f"{RANK_DISPLAY[self.rank]}"
        return f"{SUIT_DISPLAY[self.suit]}{RANK_DISPLAY[self.rank]}"

    # ---- 等价性与哈希 ----
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return False
        return self.suit == other.suit and self.rank == other.rank

    def __hash__(self) -> int:
        return hash((self.suit, self.rank))

    # ---- 排序规则：按点数升序，花色视为平局 ----
    def __lt__(self, other: 'Card') -> bool:
        return self.rank < other.rank

    def __le__(self, other: 'Card') -> bool:
        return self.rank <= other.rank

    def __gt__(self, other: 'Card') -> bool:
        return self.rank > other.rank

    def __ge__(self, other: 'Card') -> bool:
        return self.rank >= other.rank


class DeckFactory:
    """
    静态工厂方法，用于创建一副合并的两副牌（108张）并进行洗牌/发牌。
    本类不应被实例化。
    """

    @staticmethod
    def create_double_deck() -> list[Card]:
        """生成两副标准扑克牌（含大小王）的组合。"""
        cards: list[Card] = []
        for _ in range(2):                     # 两副
            # 普通花色牌 (3~2)
            for suit in (Suit.SPADE, Suit.HEART, Suit.CLUB, Suit.DIAMOND):
                for rank in Rank:
                    if rank in (Rank.SMALL_JOKER, Rank.BIG_JOKER):
                        continue
                    cards.append(Card(suit, rank))
            # 大小王各一张
            cards.append(Card(Suit.JOKER, Rank.SMALL_JOKER))
            cards.append(Card(Suit.JOKER, Rank.BIG_JOKER))
        return cards

    @staticmethod
    def shuffle(deck: list[Card]) -> list[Card]:
        """返回打乱后的新列表（不修改原列表）。"""
        new_deck = deck[:]
        random.shuffle(new_deck)
        return new_deck

    @staticmethod
    def deal(deck: list[Card], num_players: int = 4) -> list[list[Card]]:
        """
        将牌平均分配给玩家（每人27张），返回按点数降序排列的手牌列表。
        参数 deck 应为洗过的牌组。
        """
        if len(deck) != num_players * 27:
            raise ValueError(f"牌组数量 {len(deck)} 无法均分给 {num_players} 人")
        hands: list[list[Card]] = []
        for i in range(num_players):
            start = i * 27
            end = start + 27
            hand = deck[start:end]
            # 按点数降序排列（大王>小王>2>A>...>3）
            hand.sort(reverse=True)
            hands.append(hand)
        return hands