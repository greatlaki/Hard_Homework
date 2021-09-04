from const import RANKS, SUITS
from itertools import product

from random import shuffle


class Card:

    def __init__(self, suit, rank, points):  # add picture
        self.suit = suit
        self.rank = rank
        self.points = points

    def __str__(self):
        message = f'Rank: {self.rank}; Points: {str(self.points)}' # add picture
        return message

class Deck:

    def __init__(self):
        self.cards = self._generate_deck()
        shuffle(self.cards)

    def _generate_deck(self):
        cards = []
        for suit, rank in product(SUITS, RANKS):  # watch itertools, product
            if rank == 'ace':
                points = 11
            elif rank.isdigit():
                points = int(rank)
            else:
                points = 10
            c = Card(suit=suit, rank=rank, points=points)
            cards.append(c)
        return cards

    def get_card(self):
        return  self.cards.pop()

    def __len__(self):
        return len(self.cards)