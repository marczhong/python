num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

match operation:
      case "+":
            print(f"The result of {num1} + {num2} is: {num1 + num2}")
      case "-":
            print(f"The result of {num1} - {num2} is: {num1 - num2}")
      case "*":
            print(f"The result of {num1} * {num2} is: {num1 * num2}")
      case "/" if num2 != 0: # Handle division by zero
            print(f"The result of {num1} / {num2} is: {num1 / num2}")
      case _:
            print("Invalid operation. Please enter one of +, -, *, or /.")
