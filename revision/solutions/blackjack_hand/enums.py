from enum import Enum


class CardSuitEnum(Enum):
    CLUB = 'C'
    HEART = 'H'
    DIAMOND = 'D'
    SPADE = 'S'

    def __str__(self):
        return {
            self.CLUB: '♣',
            self.HEART: '♥',
            self.DIAMOND: '♦',
            self.SPADE: '♠',
        }.get(self)


class CardValueEnum(Enum):
    ACE = 'A'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'

    def get_bj_value(self):
        return {
            self.ACE: 1,
            self.TWO: 2,
            self.THREE: 3,
            self.FOUR: 4,
            self.FIVE: 5,
            self.SIX: 6,
            self.SEVEN: 7,
            self.EIGHT: 8,
            self.NINE: 9,
            self.TEN: 10,
            self.JACK: 10,
            self.QUEEN: 10,
            self.KING: 10,
        }.get(self)

    def __str__(self):
        return self.value
