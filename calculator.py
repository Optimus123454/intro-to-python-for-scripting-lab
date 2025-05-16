#Ask user for number 1
num1 = int(input("Choose a number between 1 and 10:"))
#Ask user for number 2
num2 = int(input("Choose another number between 1 and 10 (It can be the same number!): "))
#Ask user for an operation to perform
operandInp = input("Choose an operation to perform with your chosen number from one of the following: +, -, *, / ")
#Check the operand is a valid operand
goodOps = ("+","-","*","/")
while operandInp not in goodOps :
    operandInp = input ("Sorry but your operation is not valid. Please choose one of the following: +, -, *, / ")
if operandInp == "+":
    print(num1 + num2)
elif operandInp == "-":
    print(num1 - num2)
elif operandInp == "*":
    print(num1 * num2)
else:
    print(num1 / num2)

