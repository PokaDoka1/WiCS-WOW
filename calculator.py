# FUNCTION: calculator.py
# Author:   Rachel Fernandez
# This code represents a calculator, where users can input two numbers they want to either multiply, divide, subtract, or add.
# The user inputs which operation they want to compute, and the calculate outputs the result.

# Get our user input for num1 and num2
num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

# Get our input for which operator we are computing
operator = input('Which operation do you want to compute?')

# CASE: 'Addition'
if (operator == 'Addition'):
    output = num1 + num2

# CASE: 'Subtraction'
elif (operator == 'Subtraction'):
    output = num1 - num2

# CASE: 'Division'
elif (operator == 'Division'):
    output = num1 / num2

# CASE: 'Multiplication'
elif (operator == 'Multiplication'):
    output = num1 * num2
    
print("This is the output: " + str(output))
