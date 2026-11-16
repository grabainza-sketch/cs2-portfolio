# Exercise 1: Count Even Numbers
# Loop through numbers starting at 2 up to 20, stepping by 2 each time
for count in range(2, 21, 2):
  # Print the current even number
  print(count)
  
# Exercise 2: The Countdown Timer
# Set the starting value for the countdown at 10
count1=10
# Keep repeating the loop as long as count1 is greater than 0
while count1 > 0:
  # Display the current countdown number
  print(count1)
  # Subtract 1 from count1 on each pass
  count1 -= 1
  
# Exercise 3: Skip Multiples
# Loop through every number from 1 to 15
for count2 in range(1, 16):
    # Check if the number divides evenly by 3 (a multiple of 3)
    if count2 % 3 == 0:
        # Skip the rest of this loop turn so multiples of 3 are not printed
        continue
    # Print numbers that were not skipped
    print(count2)

# Exercise 4: Multiplication Table Generator
# Define a function that takes a number and prints its multiples from 1 to 10
def show_table(number):
    # Loop from 1 to 10
    for i in range(1, 11):
        # Multiply the given number by the current loop number and print it
        print(number * i)
# Ask the user to type a number and convert it into an integer
user_number = int(input("Enter a number: "))
# Check the range condition on user_number
if 10 > user_number < 0:
  print(w)
# Call the function and pass the user's number as an argument
show_table(user_number)
