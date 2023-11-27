#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username == "admin" and password == "12345":
        return "Access granted"
    if username == "ADMIN" and password == "12345":
        return "Access granted"
    
    return "Access denied"

def hows_the_weather(temperature):
    # your code here
    if (temperature < 40):
        return "It's brisk out there!"
    elif (temperature >= 40 and temperature <= 65) :
        return "It's a little chilly out there!"
    if (temperature >85):
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
    return "It's perfect out there!"

def fizzbuzz(num):
    # your code here
    if (num % 3 == 0) and (num % 5 == 0):
        return "FizzBuzz"
    elif (num % 3 == 0):
        return "Fizz"
    elif (num % 5 == 0):
        return "Buzz"
    return num

def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # Check for division by zero
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Division by zero!")
            return None
    else:
        print("Invalid operation!")
        return None

# Example usage:
result = calculator('+', 5, 3)
print(result)  # Output: 8

result = calculator('-', 10, 4)
print(result)  # Output: 6

result = calculator('*', 2, 7)
print(result)  # Output: 14

result = calculator('/', 8, 2)
print(result)  # Output: 4.0

result = calculator('%', 5, 2)  # Invalid operation!
print(result)  # Output: None
