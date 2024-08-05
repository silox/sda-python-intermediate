from exceptions import ValidationException
from card import CardFactory


class BlackJackHand:
    used_cards = set()

    def __init__(self, cards=None):
        self.cards = []
        for card in cards or []:
            self.add_card(card)

    def add_card(self, card):
        if card in BlackJackHand.used_cards:
            raise ValidationException('Duplicate card')

        self.used_cards.add(card)
        self.cards.append(card)

    def calculate_hand_value(self):
        result = 0
        aces_count = 0
        for card in self.cards:
            if (card_value := card.get_value()) == 1:
                aces_count += 1
            else:
                result += card_value

        if aces_count and result + 11 <= 21:
            result += 11
            aces_count -= 1

        return result + aces_count

    def __contains__(self, card):
        return card in self.cards


class BlackJackHandFactory:
    def __init__(self):
        self.card_factory = CardFactory()

    def parse_from_string(self, string):
        cards = [self.card_factory.parse_from_string(string_card) for string_card in string.split()]
        return BlackJackHand(cards)
