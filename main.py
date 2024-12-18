from girls_power.gomez import Gomez
from girls_power.mosenos import Mosenos
from girls_power.esparagoza import Esparagoza

ashley = Gomez(name={}, age={}, course={})
mosenos = Mosenos(title={}, author={}, genre={})
esparagoza = Esparagoza()

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
            esparagoza.start_menu()

        elif choice == '4':
            ashley.choose_action()
           
        elif choice == '5':
            mosenos.menu()
            
        elif choice == '6':
            print("\nExiting program.\n")  
            break
        else:
            print("\nInvalid option. Please try again.\n")

main_menu()