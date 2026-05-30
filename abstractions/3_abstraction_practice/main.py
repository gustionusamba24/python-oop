import random

class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    """
    1. Complete the constructor:
        1. Initialize a private empty list called cards.
        2. Fill that empty list by calling the create_deck method within the constructor.
    """
    def __init__(self):
        self.__cards = []
        self.create_deck()

    """
    2. Complete the create_deck(self) method:
        1. Create a (Rank, Suit) tuple for each combination of the 52 cards in the deck and append them to the cards list.
        Order matters! The cards should be appended to the list in the following order: all ranks of hearts, then diamonds, then clubs, and finally spades. Within each suit, the cards should be ordered from lowest rank (Ace) to highest rank (King).
    """
    def create_deck(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.__cards.append((rank, suit))

    """
    3. Complete the shuffle_deck(self) method:
        1. Use the random.shuffle() function (available from the random package) to shuffle the cards in the deck.
    """
    def shuffle_deck(self):
        random.shuffle(self.__cards)

    """
    4. Complete the deal_card(self) method
        1. .pop() the first card off the top of the deck (top of the deck is the end of the list) and return it. If there are no cards left in the deck the method should instead return None.
    """
    def deal_card(self):
        if len(self.__cards) == 0:
            return None
        return self.__cards.pop()

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"


"""
TEST CASE
"""

deck = DeckOfCards()
print(deck)  # The deck has 52 cards
print(deck.deal_card())  # ('King', 'Spades')
print(deck.deal_card())  # ('Queen', 'Spades')
print(deck)  # The deck has 50 cards
deck.shuffle_deck()
print(deck.deal_card())  # Random card from the deck    
deck.shuffle_deck()
print(deck.deal_card())  # Random card from the deck
print(deck)  # The deck has 50 cards