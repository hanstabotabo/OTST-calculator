def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue
    
        if choice == '1':
            print(add(num1, num2))
        elif choice == '2':
            print(subtract(num1, num2))
        elif choice == '3':
            print(multiply(num1, num2))
        elif choice == '4':
            print(divide(num1, num2))
        next_calculation = input("Let's do next calculation? (y/n): ")
        if next_calculation == "n":
            break

    else:
        print("Invalid input.")