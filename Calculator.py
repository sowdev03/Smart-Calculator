import math
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def square(a):
    return a*a
def cube(a):
    return a*a*a
def power(a, b):
    return a**b
def modulus(a,b):
    return a%b
def sqrt(a):
    return math.sqrt(a)
print("===== SMART CALCULATOR =====")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")
print("6. Cube")
print("7. Power")
print("8. Modulus")
print("9. SquareRoot")
choice = int(input("Enter your choice: "))
if choice in [1,2,3,4,7,8]:
    num1 = int(input("Enter First Number:" )) 
    num2 = int(input("Enter Second Number:" ))
else:
    num1 = int(input("Enter Number: "))
if choice == 1:
    print("Answer =", add(num1, num2))
elif choice == 2:
    print("Answer =", subtract(num1, num2))
elif choice == 3:
    print("Answer =", multiply (num1, num2))
elif choice == 4:
    if num2 == 0:
        print("Cannot Divide by Zero!")
    else:
        print("Answer =", divide(num1, num2))
elif choice == 5:
    print("Answer =", square(num1))
elif choice == 6:
    print("Answer =", cube (num1))
elif choice == 7:
    print("Answer =", power (num1, num2))
elif choice == 8:
    print("Answer =", modulus (num1, num2))
elif choice == 9:
    if num1 0:
        print("Cannot find the square root of a negative number..")
    else:
        print("Answer =", sqrt(num1)) 
else:
    print('''Invalid Choice!
    Please Select Between 1 and 9''')