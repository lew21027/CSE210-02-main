import random

class Card():

    def __init__(self):
        self.card_value = random.randint(1, 13)

    def draw_new_card(self):
        self.card_value = random.randint(1, 13)
