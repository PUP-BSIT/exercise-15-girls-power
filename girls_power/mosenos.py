import os

class Mosenos:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        
    def greet(self):
        print("Hello! Welcome.")

    def display_title(self):
        print(f"Title: {self.title}")
    
    def display_author(self):
        print(f"Author: {self.author}")
    
    def display_genre(self):
        print(f"Genre: {self.genre}")
    
    def add_book(self):
        print("\nAdd a New Book")
        self.title = input("Enter the Book Title: ")
        self.author = input("Enter the Author: ")
        self.genre = input("Enter the Genre: ")
        print("\nNew book added successfully!")
    
    def menu(self):
        while True:
            print("\n---- Book Information Menu ----")
            print("1. Greetings")
            print("2. Add Book Title")
            print("3. Display Book Title")
            print("4. Display Author")
            print("5. Display Genre")
            print("6. Exit")
            choice = input("Please enter a number: ")

            match choice:
                case '1':
                    os.system('cls')
                    self.greet()
                    input("\nPress enter to continue.")
                case '2':
                    os.system('cls')
                    self.add_book()
                    input("\nPress enter to continue.")
                case '3':
                    os.system('cls')
                    self.display_title()
                    input("\nPress enter to continue.")
                case '4':
                    os.system('cls')
                    self.display_author()
                case '5':
                    os.system('cls')
                    self.display_genre()
                    input("\nPress enter to continue.")
                case '6':
                    break
                case _:
                    print("Invalid choice. Please try again.")
