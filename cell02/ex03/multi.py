print("Enter the first number:")
a = int(input())

print("Enter the second number:")
b = int(input())

res = a * b

print(f"{a} x {b} = {res}")

if res > 0:
    print("The result is positive.")
elif res < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
