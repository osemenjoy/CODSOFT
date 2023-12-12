print("Enter '+' for addition.\n Enter '-' for subtraction.\n Enter '/' for division." )
print("Enter '*' for multiplication.")
operator = input("Enter the operator (+, -, /, *): ")
num1 = float(input("Enter First number: "))
num2 = float(input("Enter Second number: "))
if operator == '+':
    sum = num1 + num2
    print(sum)
elif operator == '-':
    subtraction = num1 - num2
elif operator == '/':
    division = num1/num2
elif operator == '*':
    multiplication = num1 * num2