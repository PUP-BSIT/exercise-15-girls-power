from girls_power.gomez import Gomez

ashley = Gomez()

def main_menu():
    while True:
        print("============== Main Menu ==============")
        print("+  [1] Aleck Mcklaiyre Alejandro      +")
        print("+  [2] Jasmine Robelle De leon        +")
        print("+  [3] Mikka Kette Esparagoza         +")
        print("+  [4] Ashley Hermoine Gomez          +")
        print("+  [5] Loise Nicole Mosenos           +")
        print("+  [6] Exit                           +")
        print("=======================================")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            print("-----")
            # TODO(alejanddro_aleck):

        elif choice == '2':
            print("-----")
            # TODO(de_leon_jasmine):
            
        elif choice == '3':
            print("-----")
            # TODO(esparagoza_mikka):

        elif choice == '4':
            ashley.menu()
           
        elif choice == '5':
            print("-----")
            # TODO(mosenos_loise):

        elif choice == '6':
            print("\nExiting program.\n")  
            break
        else:
            print("\nInvalid option. Please try again.\n")

main_menu()