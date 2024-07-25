# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Main function to take user input and call the add_numbers function
def main():
    # Input from user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Adding the numbers
    result = add_numbers(num1, num2)
    
    # Displaying the result
    print(f"The sum of {num1} and {num2} is {result}")

# Calling the main function to run the program
if __name__ == "__main__":
    main()
