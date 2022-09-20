import os
clear = lambda: os.system('cls')
class menu:

    functions = []
    options_strings = []
    num_opt = 0

    #Builder
    '''Functions_list -> List of the functions the menu is going to call
    opt_list -> Lisf ot the strings that describe that functions and the menu is going to print
    Both list need to have the same size, and the function and his description in the same position
    '''
    def __init__(self,functions_list,opt_list):
        if len(functions_list) != len(opt_list):
            print("Error: opt_list length != functions_list length")
            return None
        self.functions = functions_list
        self.options_strings = opt_list
        self.num_opt = len(functions_list)

    #Funtion that prints the menu with the options specified in the building
    def print_menu(self):
        for i in range(self.num_opt):
            print(f"Option {i+1}: {self.options_strings[i]}")
        print("Option -1: Exit")


    #Function that prints the menu and ask the user for the desired option
    # Return the function that is going to be executed, or -1 to exit.    
    def select_menu(self):
        while True:
            clear()
            self.print_menu()
            option = input("Choose an option: ")
            clear()
            try: 
                option = int(option)
                if option == -1:
                    return -1
                elif option <= self.num_opt:
                    return self.functions[option-1]
                else:
                    print("Invalid option")
                    input("Try again...")
            except:
                print("Invalid option")
                input("Try again...")


#Exemple code to run this class in your script
'''
    functions =[func_1,func_2]
    options = ["Function 1","Function 2"]
    mymenu = menu(functions,options) 

    while True:
        selected_function = mymenu.select_menu()
        if selected_function == -1: break
        else: selected_function()
        input("Continue...")
    
    input("Thanks for using this menu")
'''