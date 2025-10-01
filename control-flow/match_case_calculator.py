num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        addition = num1 + num2
        print(f'The result is {addition}')
    case "-":
        subtraction = num1 - num2
        print(f'The result is {subtraction}')
    case "*":
        multiplication = num1 * num2
        print(f'The result is {multiplication}')
    case "/":
        if num2 == 0 or num1 == 0:
            raise ZeroDivisionError("Division by zero is not allowed")    
        division = num1 / num2
        print(f'The result is {division}')
    case _:
        print("Invalid operator.")