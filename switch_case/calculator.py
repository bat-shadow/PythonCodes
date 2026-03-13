num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operator (+,-,*,/): ")

match op:
    case "+":
        print("Result:", num1 + num2)
    case "-":
        print("Result:", num1 - num2)
    case "*":
        print("Result:", num1 * num2)
    case "/":
        print("Result:", num1 / num2)
    case _:
        print("Invalid operator")