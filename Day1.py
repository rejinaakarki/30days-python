# Building a simple calculator using basic operators , variable and data types
num1 = float(input("Enter a number :"))
num2 = float(input("Enter a number:"))#
operator = input("Enter operator(+,-,*,/):")
if operator == "+":
    Add = num1+num2
    print("Addition:",Add)
elif operator == "-":
    Sub = num1-num2
    print("Subtraction:",Sub)
elif operator == "*":
    Mul = num1*num2
    print("Multiplication:",Mul)
elif operator == "/":
    Div = num1/num2
    print(f"Division: {Div:.2f}")
