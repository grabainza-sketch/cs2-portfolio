import math
x1 = float(input("Input x1 for the euclidean distance formula: "))
y1 = float(input("Input y1 for the euclidean distance formula: "))
x2 = float(input("Input x2 for the euclidean distance formula: "))
y2 = float(input("Input y2 for the euclidean distance formula: "))
distance = math.sqrt(math.pow((x2-x1), 2)+math.pow((y2-y1), 2))
print("Euclidean distance: ", round(distance, 2))

# Why is using a library more practical than writing all calculations from scratch? Explain using this activity as an example.
# Reflection:
# A library is more practical than writing all calculations from scratch because it cuts out some repetitiveness to the code.
# If I didn't have these programs, I would have to get more specific with what I mean to the computer instead of going straight to the point.
# For example, when I square the differences, if I did **2 instead of math.pow(inputs, 2), it would mean to the computer that I want it to do exponentiation instead of multiplication instead of just telling it to do exponentiation straight away.
