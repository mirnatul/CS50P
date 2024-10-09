def main():
    difficulty = input("Difficult or casual? ")
    players = input("Multiplayer or single-player? ")
    
    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-player":
            ...
        else:
            recommend("Klondike")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        else:
            recommend("Clock")
    else:
        print("Enter a valid difficulty")

def recommend(game):
    print("You might like", game)

main()