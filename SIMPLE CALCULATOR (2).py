# Creator Information:
# Name: Abad, Jan Roan D.
# Section: BSCpE 1-2
# Date: July 17, 2024
# Faculty: Prof. Danilo Madigalejos

# Addition
def add(x, y):
    return x + y

# Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            print("Choose operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            choice = input("Enter choice (1/2/3/4): ")

            if choice == '1':
                print("The result is:", add(num1, num2))
            elif choice == '2':
                print("The result is:", subtract(num1, num2))
            elif choice == '3':
                print("The result is:", multiply(num1, num2))
            elif choice == '4':
                print("The result is:", divide(num1, num2))
            else:
                print("Invalid choice")
                continue

            again = input("Do you want to try again? (yes/no): ")
            if again.lower() != 'yes':
                print("Thank you!")
                break
        except ValueError as e:
            print("Invalid input:", e)
        except KeyboardInterrupt:
            print("\nThank you!")
            break

if __name__ == "__main__":
    calculator()
