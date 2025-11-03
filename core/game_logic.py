from core.player_io import ask_player_action

def draw_card(deck: list[dict], hand: list[dict]) -> None:
    if deck:
        card = deck.pop(0)
        hand.append(card)

def calculate_hand_value(hand: list[dict]) -> int:
    value = 0
    for card in hand:
        rank = card["rank"]
        if rank.isdigit():
            value += int(rank)
        elif rank[card] == "A":
            value += 1
        else:
            value += 10
    return value

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    for _ in range(2):
        draw_card(deck, player["hand"])
        draw_card(deck, dealer["hand"])
        player_value = calculate_hand_value(player["hand"])
        dealer_value = calculate_hand_value(dealer["hand"])
    print(f"The initial value: player = {player_value}, dealer = {dealer_value}")


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while True:
        dealer_value = calculate_hand_value(dealer["hand"])
        if dealer_value > 21:
            print(f"the dealer lost!!!, the value: {dealer_value}")
            return False
        elif dealer_value >= 17:
            print(f"the value: {dealer_value}")
            return True



def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    start = ask_player_action()
    if start == "H":
        draw_card(deck, player["hand"])
        calc_player = calculate_hand_value(player["hand"])
        if calc_player > 21:
            print("you lost!!!")
        else:
            draw_card(deck, player["hand"])

    if start == "S":
        dealer_play(deck, dealer["hand"])

        if calculate_hand_value(player["hand"]) == calculate_hand_value(dealer["hand"]):
            print("No win! Draw!!!")











