# Clean Decision Code Makeover: Student Score Checker
**Name:** Your Name
**Section:** Your Section
---
## Activity Overview

In this activity, I improved a Student Score Checker program by applying proper coding standards and
selection structures.
The program accepts a student score from 0 to 100 and determines the appropriate classification.

The classifications are:
| Score | Classification |
|---:|---|
| 90–100 | Outstanding |
| 0–74 | Needs Improvement |

Scores below 0 or above 100 are considered invalid.
---
# Part 1 - Analyze the Logic
## Input
What information does the program need?
To formally ask the user their score, check if the score is between 0 & 100, & display "INVALID SCORE" if its outside the range.

## Valid Range
**Minimum valid score:**
0
**Maximum valid score:**
100

## Possible Outputs
List all possible outputs of the program.
1. Invalid Score.
2. Outstanding!
3. Very Satisfactory!
4. Satisfactory!
5. Needs Improvement.

## Boundary Condition
What condition will you use to determine whether the score is valid?
The "int” in ”(input("score:"))" uses the boundary condition due to the int addon filtering for integers.

## Multiple Decision Paths
Explain how the program decides which classification should be displayed.
The ”(input("score:"))" uses multiple decision paths since these are the inputs of these paths.
---
# Part 2 - Flowchart
<img width="1087" height="743" alt="image" src="https://github.com/user-attachments/assets/b1cc2508-c5e9-48cf-825b-d53be410c38e" />

## Flowchart
Insert your flowchart below.
![Score Checker Flowchart](./q1/score_checker_flowchart.png)
---

# Part 3 - Pseudocode
START
DECLARE score AS INTEGER

INPUT score

IF score < 0 OR score > 100 THEN
    DECLARE InvalidScore AS INTEGER
    DISPLAY "Invalid Score"
ELSE IF score >= 90 THEN
    DECLARE Outstanding AS .INTEGER
    DISPLAY "Outstanding!"
ELSE IF score >= 80 THEN
    DECLARE VerySatisfactory AS INTEGER
    DISPLAY "Very Satisfactory!"
ELSE IF score >= 75 THEN
    DECLARE Satisfactory AS INTEGER
    DISPLAY "Satisfactory!"
ELSE
    DECLARE NeedsImprovement AS INTEGER
    DISPLAY "Needs Improvement."
END IF

END

---
# Part 4 - Clean Code Implementation
## Source code
Insert your source code.
![Score Checker Source Code](./q1/score_checker.py)

---
# Part 5 - Testing
| Test | Input | Purpose | Expected Output | Actual Output | Result |
|---|---:|---|---|---|---|
| 1 | -1 | Below minimum |Invalid Score.|Invalid Score.|PASS|
| 2 | 0 | Minimum boundary |Needs Improvement.|Needs Improvement.|PASS|
| 3 | 74 | Below Satisfactory boundary |Needs Improvement.|Needs Improvement.|PASS|
| 4 | 75 | Satisfactory boundary |Satisfactory!|Satisfactory!|PASS|
| 5 | 80 | Very Satisfactory boundary |Very Satisfactory!|Very Satisfactory!|PASS|
| 6 | 90 | Outstanding boundary |Outstanding!|Outstanding!|PASS|
| 7 | 100 | Maximum boundary |Outstanding!|Outstanding!|PASS|
| 8 | 101 | Above maximum |Invalid Score.|Invalid Score.|PASS|

---

## Testing Reflection
### 1. Why is it important to test the values 0 and 100?
  To see if the boundaries are working through testing the minumum scores and maximum scores.
### 2. Why did you also test -1 and 101?
  To also see if the boundaries are working through inputing possible scores that could mess up the data.
### 3. Which test helped you understand boundary conditions the most?
  The first test since it showed me what happens if there is an invalid score.
### 4. Did any of your tests initially fail? If yes, what did you change in your program?
  The boundaries of the Outstanding, Very Satisfactory, and Satisfactory initially fail because they had >, not >=, so I changed > to >= to put down the supposed to be boundaries.

---

# Reflection
### 1. How did selection structures make the program more useful?
  Selection structures let my code make decisions automatically so every score gets the exact right grade right away.
### 2. How did proper comments and readable formatting improve your program?
  Clean formatting and clear comments helped me read through my code easily and fix mistakes without getting confused.
### 3. Why is it useful to plan the program using a flowchart and pseudocode before writing the code?
  Mapping things out first gave me a game plan so I could spot logical errors before I actually started writing Python code.
