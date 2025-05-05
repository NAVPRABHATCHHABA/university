try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print("Result:", a / b)
    print(undefined_variable)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except NameError:
    print("NameError occurred.")
except Exception as e:
    print("Other Error:", e)
