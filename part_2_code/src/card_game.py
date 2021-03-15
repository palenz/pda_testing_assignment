### Testing task 2 code:
# Carry out dynamic testing on the code below.
# Correct the errors below that you spotted in task 1.

class CardGame:

  def check_for_ace(self, card):
    if card.value == 1:
      return True
    else:
      return False

# 1. edited the if statement to have ==
# 2. Added the : for the else statement.
   

  def highest_card(self, card1, card2):
    if card1.value > card2.value:
      return card1
    else:
      return card2

# 1. corrected typo in the method definition (def instead of dif).  
# 2. added comma between card1 and card2.
# 3. Corrected indentation.
# 4. corrected typo, card1 instead of card on line 19.


  def cards_total(self, cards):
    total = 0
    for card in cards:
      total += card.value
    return "You have a total of " + str(total)

# 1. Set total as a variable that is equal to 0.
# 2. Fixed indentation, so that the method is contained in the cardGame class.
# wrapped total variable on line 33 in a str, so that the two strings can be concatenated.

