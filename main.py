op = input("What type of math are we doing today? ")
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

if op.upper() == "ADDITION" or op.upper() == "ADD" or op.upper() == "ADDING" or op == "+":
    print(num1 + num2)
elif op.upper() == "SUBTRACT" or op.upper() == "MINUS" or op.upper() == "SUBTRACTION" or op.upper() == "SUBTRACTING" or op == "-":
    print(num1 - num2)
elif op.upper() == "MULTIPLY" or op.upper() == "TIMES" or op.upper() == "MULTIPLICATION" or op.upper() == "X" or op.upper() == "MULTIPLYING" or op == "*":
    print(num1 * num2)
elif op.upper() == "DIVISION" or op.upper() == "DIVIDE" or op.upper() == "DIVIDING" or op == "/":
    print(num1 / num2)
else:
    print("Invalid Task!")