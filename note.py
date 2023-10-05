def make_withdraw_list(balance):
   b = balance
   def withdraw(amount):
      nonlocal b
      if amount > b:
         return "Insufficient funds"
      b = b - amount
      return b
   return withdraw

# withdraw = make_withdraw_list(100)
# withdraw(25)
# withdraw(213)