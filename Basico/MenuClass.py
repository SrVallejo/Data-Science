import os
clear = lambda: os.system('cls')
class menu:

    functions = []
    options_strings = []
    num_opt = 0

    def __init__(self,functions_list,opt_list):
        if len(functions_list) != len(opt_list):
            print("Error: opt_list length != functions_list length")
            return None
        self.functions = functions_list
        self.options_strings = opt_list
        self.num_opt = len(functions_list)

    def print_menu(self):
        for i in range(self.num_opt):
            print(f"Option {i+1}: {self.options_strings[i]}")
        print("Option -1: Exit")
        
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