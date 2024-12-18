UNSET_OPTION = -1 
EXIT_OPTION = 0   

class Gomez:
    def __init__(self):
        self.name = "Ashley Hermione"
        self.age = 19
        self.course = "DIT"
        self.hobby = "Digital Art and Programming"
        self.favorite_food = "Fries"

    def greet(self):
        print(f"Hello! I'm {self.name}.")

    def display_age(self):
        print(f"My age is {self.age}.")

    def display_course(self):
        print(f"My course is {self.course}.")

    def share_hobby(self):
        print(f"I love {self.hobby}!")

    def share_favorite_food(self):
        print(f"My favorite food is {self.favorite_food}.")

    def display_menu(self):
        print("\n===== Ashley Menu =====")
        print("1. Greet")
        print("2. Display Age")
        print("3. Display Course")
        print("4. Share Hobby")
        print("5. Share Favorite Food")
        print(f"{EXIT_OPTION}.Exit")
        return int(input("Enter your choice: "))

    def process_choice(self, choice):
        match choice:
            case 1:
                self.greet()
                input("Press Enter to continue...")
            case 2:
                self.display_age()
                input("Press Enter to continue...")
            case 3:
                self.display_course()
                input("Press Enter to continue...")
            case 4:
                self.share_hobby()
                input("Press Enter to continue...")
            case 5:
                self.share_favorite_food()
                input("Press Enter to continue...")
            case 0: 
                print("Goodbye!")
            case _:
                print("Invalid choice. Try again.")
                input("Press Enter to continue...")

    def start_menu(self):
        choice = UNSET_OPTION
        while choice != EXIT_OPTION:
            try:
                choice = self.display_menu()
                self.process_choice(choice)
            except ValueError:
                print("Invalid input. Please enter a number.")
                input("Press Enter to continue...")
