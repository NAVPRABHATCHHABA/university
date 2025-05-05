try:
    n = int(input("Enter a number: "))
except ValueError as e:
    print("Error:", e)
