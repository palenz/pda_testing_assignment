import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    
    def test_check_for_ace(self):
        my_card = Card("spades", 1)
        card_game = CardGame()
        self.assertEqual(True, card_game.check_for_ace(my_card))

    def test_check_highest_card(self):
        card_one = Card('spades', 7)
        card_two = Card('hearts', 9)
        card_game = CardGame()
        self.assertEqual(card_two, card_game.highest_card(card_one, card_two))

    def test_can_count_cards(self):
        card_one = Card('spades', 2)
        card_two = Card('hearts', 3)
        cards = [card_one, card_two]
        card_game = CardGame()
        self.assertEqual("You have a total of 5", card_game.cards_total(cards))


