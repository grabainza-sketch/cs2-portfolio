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
