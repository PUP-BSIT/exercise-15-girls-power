class Gomez:
    def __init__(self):
        self.name = "Ashley Hermione"
        self.age = 19
        self.course = "DIT"

    def greet(self):
        print("Hello! I'm Ashley Hermione.")

    def display_age(self):
        print(f"My age is {self.age}.")

    def display_course(self):
        print(f"My course is {self.course}.")

    def hobby(self):
        print("I love Digital Art and Programming!")

    def favorite_food(self):
        print("My favorite food is fries.")

    def menu(self):
        while True:
            print("\n--- Ashley Menu ---")
            print("1. Greet")
            print("2. Display Age")
            print("3. Display Course")
            print("4. Hobby")
            print("5. Favorite Food")
            print("6. Go Back")
            
            choice = input("Choose an option: ")
            
            options = {
                "1": self.greet,
                "2": self.display_age,
                "3": self.display_course,
                "4": self.hobby,
                "5": self.favorite_food,
            }

            if choice in options:
                options[choice]()
            elif choice == "6":
                print("Exiting the menu...")
                break
            else:
                print("Invalid choice. Try again.")