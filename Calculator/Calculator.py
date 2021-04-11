def calculator():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation =input('Enter your operation from ( "+" Or "-" Or "*" Or "/" ) : ')
    if (operation == "+"):
        print(f"Addition = {num1 + num2}")
    elif (operation == "-"):
        print(f"Subtraction = {num1 - num2}")
    elif (operation == "*"):
        print(f"Multiplication = {num1 * num2}")
    else:
        print(f"Division = {num1 / num2}")
    
def main():
    calculator()
    input()

if __name__ == "__main__":
    main()
