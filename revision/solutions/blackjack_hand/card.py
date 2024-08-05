from dataclasses import dataclass

from enums import CardSuitEnum, CardValueEnum
from exceptions import ValidationException


@dataclass(frozen=True)
class Card:
    suit: CardSuitEnum
    value: CardValueEnum

    @property
    def color(self):
        return 'red' if self.suit in (CardSuitEnum.HEART, CardSuitEnum.DIAMOND) else 'black'

    def get_value(self):
        return self.value.get_bj_value()

    def __repr__(self):
        return f'{self.value}{self.suit}'


class CardFactory:
    @staticmethod
    def parse_from_string(string):
        if not string:
            raise ValidationException('Empty card')

        suit = string[-1]
        if suit not in {e.value for e in CardSuitEnum}:
            raise ValidationException(f'Suit "{suit}" does not exist')

        value = string[:-1]
        if value not in {e.value for e in CardValueEnum}:
            raise ValidationException(f'Value "{value}" does not exist')

        return Card(CardSuitEnum(suit), CardValueEnum(value))
