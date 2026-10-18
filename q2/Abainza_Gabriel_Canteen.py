price = float(input("Enter price: "))
quantity = float(input("Enter quantity: "))
payment = float(input("Enter payment: "))
def calculate_total():
  total = price*quantity
  return total
def calculate_change():
  change = payment-total
  return change
total = calculate_total()
change = calculate_change()
if change < 0:
  print("Pay more.")
else:
  print("Total cost: ", P, total)
  print("Change: ", P, change)
#The calculate_total function calculates the total multiplying the price and amount and the calculate_change function subtracts the total from calculate_total to the payment.
#The difference is the parameters price and quantity are the variables defined in a function's signature, while the arguments are the actual values passed into those variables when the function was called.
#The total was temporarily stored at the place the total was called, and it was reused when it was used as a parameter in the function calculate_change.
#If the functions were separated, then it would be easier to use in a bigger context (due to available repetition and use elsewhere), easier to test for bugs, and makes the code modular.
