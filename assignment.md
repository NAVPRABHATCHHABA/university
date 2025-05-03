//Q1. Make a zero division error handler with built in exceptions.
try:
a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))
result = a / b
print("Result:", result)
except ZeroDivisionError as e:
    print("Error:", e)
