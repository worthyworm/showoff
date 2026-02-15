import os

from source import MENU, INFO, DESCRIPTION


class Menu:

    @staticmethod
    def create_menu():
        print(MENU)
        choice = int(input("Select >> "))
        return choice

    @staticmethod
    def show_info(full):
        if full == False:
            print(INFO)
        else:
            print(INFO, DESCRIPTION)

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
