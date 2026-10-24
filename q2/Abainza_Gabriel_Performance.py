def calculate_average(score1, score2, score3):
  average= (score1 + score2 + score3)/3
  return average
def get_performance(average):
  if average>=85:
    performance="Mastery"
    return performance
  elif 85>average>=70:
    performance="Developing"
    return performance
  else:
    performance="Needs Review"
    return performance
def is_eligible(average, completed_tasks):
  return average >= 85 and completed_tasks >= 3
score1=int(input("Enter Score 1: "))
if score1<0 or score1>100:
  print(w)
score2=int(input("Enter Score 2: "))
if score2<0 or score2>100:
  print(w)
score3=int(input("Enter Score 3: "))
if score3<0 or score3>100:
  print(w)
completed_tasks=int(input("Completed Tasks: "))
if completed_tasks<0 or completed_tasks>5:
  print(w)
average=calculate_average(score1, score2, score3)
performance=get_performance(average)
eligibility=is_eligible(average, completed_tasks)
print("Average: ", average)
print("Performance: ", performance)
print("Eligible for Challenge: ", eligibility)
#1. calculate_average() returns a number, get_performance() returns a string, and is_eligible() returns a Boolean.
#2. The numerical average returned by calculate_average() is stored in a variable and then passed as an argument into get_performance().
#3. The is_eligible() function returns False because both the average and the completed tasks requirement must be met.
#4. The return statement sends computed values back to the main program for storage and reuse, whereas print() only displays text on the screen.
