"""This a simple calculator application that uses CLI to
receive and return results to user. This also allows the user
to perform multiple equations using previous results.
"""


#Logo art printed at the beginning once the app has been run.
logo = """    ▄▄▄▄███▄▄▄▄      ▄████████     ███        ▄█    █▄       ▄████████
 ▄██▀▀▀███▀▀▀██▄   ███    ███ ▀█████████▄   ███    ███     ███    ███ 
 ███   ███   ███   ███    ███    ▀███▀▀██   ███    ███     ███    █▀  
 ███   ███   ███   ███    ███     ███   ▀  ▄███▄▄▄▄███▄▄   ███        
 ███   ███   ███ ▀███████████     ███     ▀▀███▀▀▀▀███▀  ▀███████████ 
 ███   ███   ███   ███    ███     ███       ███    ███            ███ 
 ███   ███   ███   ███    ███     ███       ███    ███      ▄█    ███ 
  ▀█   ███   █▀    ███    █▀     ▄████▀     ███    █▀     ▄████████▀  """


#Global variable that controls the main loop.
math_calc = True


def add(num1, num2):
    #Returns the sum of two numbers.
    return num1 + num2


def subtract(num1, num2):
    #Returns the difference of two numbers.
    return num1 - num2


def multiply(num1, num2):
    #Returns the product of two numbers.
    return num1 * num2


def quotient(num1, num2):
    #Returns the quotient of two numbers.
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return num1 / num2


def get_user_input():
    """This function gets the input from the user.
    Gets user input for two numbers and an operation.
    Floats instead of integers to ensure precision."""

    while math_calc:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            sign = input("Choose an operation (+, -, *, /): ")
            if sign in ["+", "-", "*", "/"]:
                return num1, num2, sign
            print("Invalid operation. Please choose one of +, -, *, /")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main_math():
    #Main function for the program.
    global math_calc
    #Prints the logo art.
    print(logo)
    print("Let's do some math.\nHere are some symbols you can use:\n+ : for addition\n"
          "-  : for subtraction\n* : for multiplication\n/ : for division")

    #Dictionary containing all valid operational signs.
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": quotient
    }

    while math_calc:
        user_r = input("Ready to start? Y / N: ").lower()
        if user_r == "y":
            num1, num2, sign = get_user_input()
            while math_calc:
                try:
                    result = operations[sign](num1, num2)
                    print(f"Your answer is: {result}")
                    cont_math = input("Do you want to continue with the current result? Y / N: ").lower()
                    if cont_math == "y":
                        #Sets the result from the previous equation as num1
                        num1 = result
                        num2 = float(input("Enter the next number: "))
                        sign = input("Choose an operation (+, -, *, /): ")
                    elif cont_math == "n":
                        #Exits the main loop and ends the program.
                        math_calc = False
                        print("We will end it here. Bye for now.")
                        break
                except ZeroDivisionError as e:
                    #Handles a division by zero error.
                    print(str(e))
                    math_calc = False
                    break
        elif user_r == "n":
            print("Ready when you are. Bye for now. :)")
            break
        else:
            #Handles an invalid input.
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main_math()
