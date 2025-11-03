import random

def build_standard_deck() -> list[dict]:
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["H", "D", "C", "S"]
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append({"rank": rank, "suit": suit})
    return deck


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    deck_size = len(deck)
    for _ in range(swaps):
        i = random.randrange(deck_size)
        suit_i = deck[i]["suit"]

        while True:
            j = random.randrange(deck_size)
            if j == i:
                is_valid_j = False
                if suit_i == "H" and j % 5 == 0:
                    is_valid_j = True
                elif suit_i == "C" and j % 3 == 0:
                    is_valid_j = True
                elif suit_i == "D" and j % 2 == 0:
                    is_valid_j = True
                elif suit_i == "S" and j % 7 == 0:
                    is_valid_j = True
                if is_valid_j:
                    break

            deck[i], deck[j] = deck[j], deck[i]
    return deck



















