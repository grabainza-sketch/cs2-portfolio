# Input Validation and Output Verification
**Activity:** PSHS Workshop Registration Validator
**Name:** Your Name
**Section:** Your Section
**Quarter:** 1
---
## Activity Overview
In this activity, I created a program that validates information entered into a PSHS workshop registration
system.
The program checks whether user input satisfies specific requirements before accepting the registration.
The program validates:
- student name
- age
- grade level
- email address and
- registration code.

---
# Part A - Validation Requirements
Complete the table below before writing your program.
| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error
Message |
|---|---|---|---|---|---|
| Student Name |Student Name|Text|Presence Check|""|Must not be empty|Registration cannot continue with invalid output (Field cannot be left blank.)|
| Age |Age|Integer|Range & Type Check|10|Must be an integer between 11 and 18|Registration cannot continue with invalid output (Age must be a number between 11 & 18.)|
| Grade Level |Grade Level|Integer|Range & Type Check|3|Must be an integer between 7 and 12|Registration cannot continue with invalid output (Invalid grade level. Grade must be a number between 7 & 12.)|
| Email Address |Email Address|String|Pattern Check|abainza@gmail.com|Must end with @brc.pshs.edu.ph|Registration cannot continue with invalid output (Email must require proper formating.)|
| Registration Code |Registration Code|String|Length Check|93iA%8r|Must be exactly 6 characters long|Registration cannot continue with invalid output (Code must require proper formating.)|
---
## Validation Questions
### 1. Why should the student name not be blank?
> Not only is it needed for the information, but it is not allowed by the presence check.
### 2. Why should age be checked for both data type and range?
> Because the integer type filters it to integers, and the range filters it to a specific range of numbers.
### 3. Why should grade level only accept specific values?
> Because most of time, grade level is represented by one data type.
### 4. What format requirements did you use for the email address?
> I required the email to include the domain @brc.pshs.edu.ph.
### 5. What length requirement did you use for the registration code?
> Write your answer here.
---
# Part B - Program Design
Before writing your program, create either a **flowchart or pseudocode** showing its logic.
## Pseudocode

```text
START
    OUTPUT "=============================="
    OUTPUT "  WELCOME TO THE WORKSHOP!   "
    OUTPUT "=============================="
    OUTPUT " "
    OUTPUT "~|WORKSHOP REGISTRATION|~"

    INPUT name
    IF name IS EQUAL TO "" THEN
        OUTPUT "Registration cannot continue with invalid output (Field cannot be left blank.)"
        EXIT PROGRAM
    ENDIF

    INPUT age
    IF age IS NOT A NUMBER OR age < 11 OR age > 18 THEN
        OUTPUT "Registration cannot continue with invalid output (Age must be a number between 11 & 18.)"
        EXIT PROGRAM
    ENDIF

    INPUT grade_level
    IF grade_level IS NOT A NUMBER OR grade_level < 7 OR grade_level > 12 THEN
        OUTPUT "Registration cannot continue with invalid output (Invalid grade level. Grade must be a number between 7 & 12.)"
        EXIT PROGRAM
    ENDIF

    INPUT email
    IF email DOES NOT CONTAIN "@brc.pshs.edu.ph" THEN
        OUTPUT "Registration cannot continue with invalid output (Email must require proper formating.)"
        EXIT PROGRAM
    ENDIF

    INPUT code
    TRIM whitespace from code
    IF LENGTH of code IS NOT EQUAL TO 6 THEN
        OUTPUT "Registration cannot continue with invalid output (Code must require proper formating.)"
        EXIT PROGRAM
    ENDIF

    OUTPUT "~|REGISTRATION SUCCESSFUL!|~"
    OUTPUT "~|STUDENT REGISTRATION INFO|~"
    OUTPUT "Student: ", name
    OUTPUT "Age: ", age
    OUTPUT "Grade: ", grade_level
    OUTPUT "Email: ", email
    OUTPUT "Registration Code: ", code

    OUTPUT "Thank you for registering!"
    OUTPUT "Exiting program..."
    EXIT PROGRAM
END
```

Your design should show:
- user input
- validation decisions
- error messages
- accepted registration
- rejected registration.
---
# Part C - Program Implementation
## Programming Language
> Python
## Source Code File
[`workshop_validator.py`](workshop_validator.py)
## Final Code
```python
import sys
print("="*30)
print(" "*2,"WELCOME TO THE WORKSHOP!"," "*3)
print("="*30)
print(" ")
print("~|WORKSHOP REGISTRATION|~")
name = input("Enter student name: ")
if name == "":
    print("Registration cannot continue with invalid output (Field cannot be left blank.)")
    sys.exit()
age = input("Enter age:")
if age not in range(11,19):
    print("Registration cannot continue with invalid output (Age must be a number between 11 & 18.)")
    sys.exit()
grade_level = input("Enter grade level:")
if grade_level not in range(7,13):
    print("Registration cannot continue with invalid output (Invalid grade level. Grade must be a number between 7 & 12.)")
    sys.exit()
email = input("Enter email: ")
if "@brc.pshs.edu.ph" not in email:
     print("Registration cannot continue with invalid output (Email must require proper formating.)")
     sys.exit()
code = input("Enter registration code: ").strip()
if len(code) != 6:
    print("Registration cannot continue with invalid output (Code must require proper formating.)")
    sys.exit()
print("~|REGISTRATION SUCCESSFUL!|~")

print("~|STUDENT REGISTRATION INFO|~")
print("Student: ", name)
print("Age: ", age)
print("Grade: ", grade_level)
print("Email", email)
print("Registration Code: ", code)

print("Thank you for registering!")

print("Exiting program...")
sys.exit()
```

---
## Validation Techniques Used
### Presence Validation
Explain where you used presence validation.
> Write your answer here.
### Data Type Validation
Explain where you used data type validation.
> Write your answer here.
### Range Validation
Explain where you used range validation.
> Write your answer here.

### Acceptable Value Validation
Explain where you used acceptable value validation.
> Write your answer here.
### Pattern Validation
Explain the simple pattern rule you used.
> Write your answer here.
### Length Validation
Explain the length rule you used.
> Write your answer here.
---
# Part D - Testing
Test your program using both valid and invalid inputs.
| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result |
|---:|---|---|---|---|---|
| 1 | All inputs valid | Normal case | | | |
| 2 | Blank student name | Presence | | | |
| 3 | Age = `fourteen` | Data type | | | |
| 4 | Age = `11` | Minimum boundary | | | |
| 5 | Age = `18` | Maximum boundary | | | |
| 6 | Age = `10` | Range | | | |
| 7 | Grade Level = `13` | Acceptable value | | | |
| 8 | Email = `studentpshs.edu.ph` | Pattern | | | |
| 9 | Registration Code = `ABC` | Length | | | |
| 10 | Registration Code = `CS2026` | Valid length | | | |
Write **PASS** when the actual output matches the expected output.
Write **FAIL** when it does not.
---
# Part E - Output Verification
Choose any **three tests** from Part D.
## Verification Test 1
**Input:**
```text
Write the input here.

```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**
```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
## Verification Test 2
**Input:**
```text
Write the input here.
```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**
```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
## Verification Test 3
**Input:**
```text
Write the input here.
```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**

```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
# Reflection
Answer briefly.
### 1. Why should a program validate input before processing it?
> Write your answer here.
### 2. What is the difference between input validation and output verification?
> Write your answer here.
### 3. Which validation technique was easiest for you to implement? Why?
> Write your answer here.
### 4. Which validation technique was most challenging? Why?
> Write your answer here.
### 5. How did testing invalid inputs help you improve your program?
> Write your answer here.
---
# Files for This Activity
- [`workshop_validator.py`](workshop_validator.py)
- [`input_validation.md`](input_validation.md)
---

[← Back to Main Portfolio](../README.md)
