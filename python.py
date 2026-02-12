# Define a function named 'studentGrade' that takes one argument, 'marks'
def studentGrade(marks):
        # Check if marks are 90 or greater. If true, it prints "Grade A" and skips all other checks.
        if(marks>=90):
            print("Grade A")
        # 'elif' is used for the "else if" condition. It checks if marks are 70 or greater (and implicitly less than 90).
        # NOTE: You don't need 'and marks < 90' when using 'elif', because the 'if' above it already handles marks >= 90.
        elif(marks>=70):
        # ERROR FIXED: The 'print' statement for "Grade B" was missing an indentation, which is mandatory in Python.
            print("Grade B")
        # ERROR FIXED: The keyword 'eliif' is misspelled. It should be 'elif'.
        # This checks if marks are 50 or greater (and implicitly less than 70).
        elif(marks>=50):
            print("Grade C")
        # This checks if marks are 35 or greater (and implicitly less than 50).
        elif(marks>=35):
            print("Grade D")
        # If none of the above conditions are met (marks are less than 35), this prints "Fail"
        else:
            print("Fail")

# Prompt the user to enter a number, convert the input to an integer, and store it in the 'mar' variable
mar  = int(input("Enter a number: "))
# Call the 'studentGrade' function with the user-provided marks
studentGrade(mar)
