try:
    with open("nonexistentfile.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print("Error:", e)
