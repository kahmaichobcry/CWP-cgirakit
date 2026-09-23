
val = input("Give me a number: ")

try:
    f = float(val)
    if f.is_integer() and '.' not in val:
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    pass
