accepted_ops= ["ADDITION","ADD","ADDING","+","PLUS","SUBTRACT","MINUS","SUBTRACTION","SUBTRACTING","-","MULTIPLY","TIMES","MULTIPLICATION","X","MULTIPLYING","*","DIVISION","DIVIDE","DIVIDING","/"]

addition_ops=["ADDITION","ADD","ADDING","+","PLUS"]
subtraction_ops=["SUBTRACT","MINUS","SUBTRACTION","SUBTRACTING","-"]
multiplication_ops=["MULTIPLY","TIMES","MULTIPLICATION","X","MULTIPLYING","*"]
division_ops=["DIVISION","DIVIDE","DIVIDING","/"]

op = input("What type of math are we doing today? ").upper()
while op not in accepted_ops:
    print("ERROR NOT A VALID OPERATION")
    op = input("What type of math are we doing today? ").upper()

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

if op in addition_ops:
    print(num1 + num2)
elif op in subtraction_ops:
    print(num1 - num2)
elif op in multiplication_ops:
    print(num1 * num2)
elif op in division_ops:
    if num2 == 0:
        print("ERROR Cannot Divide By 0")
    else:
        print(num1 / num2)
