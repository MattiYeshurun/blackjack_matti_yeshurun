
def ask_player_action() -> str:
    select = input("Press the S or H key.")
    if select != "S" or select != "H":
        print("Please select a valid character")
    return select





