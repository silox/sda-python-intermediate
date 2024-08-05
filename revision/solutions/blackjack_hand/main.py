import sys

from blackjack import BlackJack
from exceptions import BlackJackException, ValidationException


def main():
    blackjack = BlackJack()
    dealer_input = input("Enter dealer's hand: ")
    blackjack.add_hand(dealer_input, dealer=True)
    player_idx = 1
    while player_input := input(f"Enter player{player_idx}'s hand (empty line to finish): "):
        blackjack.add_hand(player_input)
        player_idx += 1
    print()

    winners = blackjack.decide_winners()
    assert winners
    if winners == ['dealer']:
        print("Nobody wins!")
    else:
        print(f"Player{'s' if len(winners) > 1 else ''} {', '.join(winners)} win{'s' if len(winners) == 1 else ''}!")


if __name__ == "__main__":
    try:
        main()
    except BlackJackException as error:
        print(error, file=sys.stderr)
    except ValidationException as error:
        print("Error during input validation:", error, file=sys.stderr)
