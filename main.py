accepted_ops= ["ADDITION","ADD","ADDING","+","PLUS","SUBTRACT","MINUS","SUBTRACTION","SUBTRACTING","-","MULTIPLY","TIMES","MULTIPLICATION","X","MULTIPLYING","*","DIVISION","DIVIDE","DIVIDING","/"]

op = input("What type of math are we doing today? ").upper()
while op not in accepted_ops:
    print("ERROR NOT A VALID OPERATION")
    op = input("What type of math are we doing today? ").upper()

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

if op.upper() == "ADDITION" or op.upper() == "ADD" or op.upper() == "PLUS" or op.upper() == "ADDING" or op == "+":
    print(num1 + num2)
elif op.upper() == "SUBTRACT" or op.upper() == "MINUS" or op.upper() == "SUBTRACTION" or op.upper() == "SUBTRACTING" or op == "-":
    print(num1 - num2)
elif op.upper() == "MULTIPLY" or op.upper() == "TIMES" or op.upper() == "MULTIPLICATION" or op.upper() == "X" or op.upper() == "MULTIPLYING" or op == "*":
    print(num1 * num2)
elif op.upper() == "DIVISION" or op.upper() == "DIVIDE" or op.upper() == "DIVIDING" or op == "/":
    if num2 == 0:
        print("ERROR Cannot Divide By 0")
    else:
        print(num1 / num2)
