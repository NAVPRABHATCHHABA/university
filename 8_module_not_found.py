try:
    import non_existent_module
except ModuleNotFoundError as e:
    print("Error:", e)
