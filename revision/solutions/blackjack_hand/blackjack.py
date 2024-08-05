from exceptions import BlackJackException
from hand import BlackJackHandFactory


class BlackJack:
    def __init__(self):
        self.dealer = None
        self.hands = []
        self.bj_hand_factory = BlackJackHandFactory()

    def add_hand(self, hand_string, dealer=False):
        if dealer:
            if self.dealer is not None:
                raise BlackJackException('Dealer already exists!')
            self.dealer = self.bj_hand_factory.parse_from_string(hand_string)

        else:
            self.hands.append(self.bj_hand_factory.parse_from_string(hand_string))

    def decide_winners(self):
        if self.dealer is None:
            raise BlackJackException('There is no Dealer!')
        if not self.hands:
            raise BlackJackException('There are no players except dealer!')

        dealer_result = self.dealer.calculate_hand_value()
        players_results = [player.calculate_hand_value() for player in self.hands]
        print(dealer_result)
        print(players_results)

        # Everyone over 21
        if dealer_result > 21 and all(res > 21 for res in players_results):
            return ['dealer']

        # Every player wins
        if dealer_result > 21:
            return [str(i) for i in range(1, len(players_results) + 1)]

        # Get every player who has larger result than the dealer
        winners = [
            str(player_idx)
            for player_idx, res in enumerate(players_results, start=1)
            if dealer_result < res <= 21
        ]
        print('winners', winners)
        return winners or ['dealer']
