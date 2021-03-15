### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      # The line above should use a == instead of =, since = is for assigning variables
      return True
    else
      return False
   

  dif highest_card(self, card1 card2):
  # should be def instead of dif, and there's a comma needed between card1 and card2.
  if card1.value > card2.value:
    return card
  # card is not being passed in the method definition. It should be card 1 or 2.
  else:
    return card2
  


def cards_total(self, cards):
  total
  # total is not defined. Maybe use total = 0 instead
  for card in cards:
    total += card.value
    return "You have a total of" + total

  # The return statement needs to be outside the foor loop (no indentation). Right now it will run for every card because it is in the for loop.
  
```
