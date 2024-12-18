class Gomez:
    def __init__(self, name, age, course):
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

    def choose_action(self):
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
                "4": self.share_hobby,  
                "5": self.share_favorite_food, 
            }

            if choice in options:
                options[choice]()
            elif choice == "6":
                print("Exiting the menu...")
                break
            else:
                print("Invalid choice. Try again.")
