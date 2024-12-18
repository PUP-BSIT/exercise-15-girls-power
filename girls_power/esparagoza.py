import os

EXIT_OPTION = 0
UNSET_OPTION = -1

class Esparagoza:
    def __init__(self):
        self.name = "Zild Benitez"
        self.age = 27
        self.profession = "Musician and Artist"
        self.best_album = "Huminga"
        self.popular_song = "Dekada '70"

    def admire_artist(self):
        print(f"\n{self.name} is an amazing musician and artist!")
        print(f"\nHe's known for his unique style and incredible live "
              + f"performances at the age of {self.age}.")

    def describe_album(self):
        print(f"\nHis best album for me is '{self.best_album}', which is full "
              + "of soulful tracks that showcase his artistry.")

    def share_favorite_song(self):
        print(f"\nMy favorite song by {self.name} is '{self.popular_song}'.")

    def recount_gig_experience(self):
        print(f"\nAttending {self.name}'s concert was a dream come true!")
        print("\nThe energy, the music, and the connection with the crowd "
              + "were unmatched.")
        print("If you get a chance to see him live, don’t miss it!")

    def share_random_fact(self):
        print(f"\nDid you know that {self.name} started as a bassist in a "
              + "band before going solo?")
        print("\nHe's an inspiration to many aspiring artists!")

    def display_menu(self):
        os.system('cls')
        print("========== About Zild Menu =========")
        print("1. Admire Zild Benitez")
        print("2. Describe His Best Album")
        print("3. Share My Favorite Song")
        print("4. Recount My Concert Experience")
        print("5. Share a Random Fact")
        print("0. Exit Menu")
        print("===================================")
        try:
            return int(input("\nChoose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            input("\nPress enter to continue.")
            return UNSET_OPTION

    def process_choice(self, choice):
        actions = {
            1: self.admire_artist,
            2: self.describe_album,
            3: self.share_favorite_song,
            4: self.recount_gig_experience,
            5: self.share_random_fact
        }

        if choice == EXIT_OPTION:
            print("Exiting the menu... Goodbye!")
        elif choice in actions:
            os.system('cls')
            actions[choice]()
            input("\nPress enter to continue.")
        else:
            os.system('cls')
            print("Invalid choice. Please try again.")
            input("\nPress enter to continue.")

    def start_menu(self):
        choice = UNSET_OPTION
        while choice != EXIT_OPTION:
            choice = self.display_menu()
            if choice != UNSET_OPTION:
                self.process_choice(choice)
                os.system('cls')
