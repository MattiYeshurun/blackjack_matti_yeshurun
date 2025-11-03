
from core.deck import build_standard_deck, shuffle_by_suit
from core.game_logic import run_full_game, deal_two_each, dealer_play
from core.player_io import ask_player_action

def init_game():
    player = {"hand":[]}
    dealer = {"hand":[]}

    deck = build_standard_deck()
    shuffle_by_suit(deck)
    deal_two_each(deck, player, dealer)
    dealer_play(deck, dealer)
    ask_player_action()
    run_full_game(deck, player, dealer)

if __name__ == "__main__":

    init_game()


