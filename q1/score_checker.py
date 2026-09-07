score=int(input("Enter score: "))
if score < 0 or score > 100:
  print("Invalid Score.")
elif score >= 90:
  print("Outstanding!")
elif score >= 80:
  print("Very Satisfactory!")
elif score >= 75:
  print("Satisfactory!")
else:
  print("Needs Improvement.")
