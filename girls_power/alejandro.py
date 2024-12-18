import operator

EXIT_OPTION = 6
UNSET_OPTION = -1

class Calculator:

    operations = {
        "add": operator.add,
        "subtract": operator.sub,
        "multiply": operator.mul,
        "divide": operator.truediv,
    }

    def __init__(self):
        self.value_1 = 0
        self.value_2 = 0

    def enter_values(self):
        while True:
            try:
                self.value_1 = int(input("Enter first value: "))
                self.value_2 = int(input("Enter second value: "))
                break
            except ValueError:
                print("Error: Please enter valid numbers.")

    def show_values(self):
        print(f"Value 1: {self.value_1}")
        print(f"Value 2: {self.value_2}")

    def perform_addition(self):
        return Calculator.operations["add"](self.value_1, self.value_2)

    def perform_subtraction(self):
        return Calculator.operations["subtract"](self.value_1, self.value_2)

    def perform_multiplication(self):
        return Calculator.operations["multiply"](self.value_1, self.value_2)

    def perform_division(self):
        if self.value_2 == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return Calculator.operations["divide"](self.value_1, self.value_2)

def start_calculator():
    calculator = Calculator()
    user_choice = UNSET_OPTION

    while user_choice != EXIT_OPTION:
        user_choice = show_menu()
        handle_choice(user_choice, calculator)

def show_menu():
    print("\n----------- Welcome --------------")
    print("++++++ Aleck's Calculator Menu ++++++")
    print("+  [1] Enter Values                 +")
    print("+  [2] Add                          +")
    print("+  [3] Subtract                     +")
    print("+  [4] Multiply                     +")
    print("+  [5] Divide                       +")
    print("+  [6] Exit                         +")
    print("+++++++++++++++++++++++++++++++++++\n")

    while True:
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            print("Error: Please enter a valid menu option.")

def handle_choice(choice, calculator):
    match choice:
        case 1:
            print("----- Enter Values -----")
            calculator.enter_values()
            print("Values are added successfully!")

        case 2:
            print("-------- Add --------")
            calculator.show_values()
            result = calculator.perform_addition()
            print(f"Result: {result}")

        case 3:
            print("----- Subtract -----")
            calculator.show_values()
            result = calculator.perform_subtraction()
            print(f"Result: {result}")

        case 4:
            print("----- Multiply -----")
            calculator.show_values()
            result = calculator.perform_multiplication()
            print(f"Result: {result}")

        case 5:
            print("------ Divide ------")
            calculator.show_values()
            result = calculator.perform_division()
            if result is not None:
                print(f"Result: {result}")

        case 6:
            print("Exiting Aleck's Main Menu.")

        case _:
            print("Invalid Choice. Try Again.")
            input("\nPress Enter to continue...")