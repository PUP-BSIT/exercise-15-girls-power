from girls_power.gomez import Gomez
from girls_power.mosenos import Mosenos
from girls_power.esparagoza import Esparagoza
from girls_power import alejandro
from girls_power.deleon import Deleon


ashley = Gomez()
mosenos = Mosenos(title={}, author={}, genre={})
esparagoza = Esparagoza()
deleon = Deleon()

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
            alejandro.start_calculator()

        elif choice == '2':
            print("-----")
            deleon.menu()
            
        elif choice == '3':
            esparagoza.start_menu()

        elif choice == '4':
            ashley.start_menu()
           
        elif choice == '5':
            mosenos.start_menu()
            
        elif choice == '6':
            print("\nExiting program.\n")  
            break
        else:
            print("\nInvalid option. Please try again.\n")

main_menu()