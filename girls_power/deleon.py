import os
import sys

class Deleon:
    def __init__(self, player_name="Player 1"):
        self.player_name = player_name
        self.wins = 0
        self.losses = 0
        self.high_score = 0

    def __str__(self):
        return (
            f"GameStatsTracker for {self.player_name}:\n"
            f"Wins: {self.wins}, Losses: {self.losses}, "
            f"High Score: {self.high_score}"
        )

    def add_win(self):
        self.wins += 1
        print(f"{self.player_name} earned a win! Total Wins: {self.wins}")

    def add_loss(self):
        self.losses += 1
        print(
            f"{self.player_name} suffered a loss. Total Losses: {self.losses}"
        )

    def update_high_score(self, score):
        if score > self.high_score:
            self.high_score = score
            print(f"New high score for {self.player_name}: {self.high_score}")
        else:
            print(
                f"Score {score} did not beat the high score: "
                f"{self.high_score}"
            )

    def reset_stats(self):
        self.wins = 0
        self.losses = 0
        self.high_score = 0
        print(f"{self.player_name}'s statistics have been reset.")

    def display_stats(self):
        print(f"\n--- {self.player_name}'s Game Statistics ---")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        print(f"High Score: {self.high_score}")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_menu(self):
        while True:
            print(f"\n--- {self.player_name}'s Stats Menu ---")
            print("1. Add Win")
            print("2. Add Loss")
            print("3. Update High Score")
            print("4. Reset Stats")
            print("5. Display Stats")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                self.add_win()
            elif choice == "2":
                self.add_loss()
            elif choice == "3":
                try:
                    score = int(input("Enter the new score: ").strip())
                    self.update_high_score(score)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif choice == "4":
                self.reset_stats()
            elif choice == "5":
                self.display_stats()
                input("\nPress Enter to return to the menu.")
            elif choice == "6":
                confirm = input(
                    "Are you sure you want to exit? (y/n): "
                ).strip().lower()
                if confirm == 'y':
                    print("Exiting the menu. Goodbye!")
                    break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    tracker = Deleon(player_name="Jasmine")
    tracker.menu()
