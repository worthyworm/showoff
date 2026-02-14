import data_handler
import ui_handler
from ui_handler import menu
import statistics_handler

VERSION = 1
db = data_handler
ui = ui_handler
stats = statistics_handler
games = data_handler.db["games"]

def main():

    while True:
        menu.showInfo(VERSION, False)
        user_choice = menu.createMenu()

        if user_choice == 1:
            stats.addMatch()
            print("Added!")
            db.save()
            input()
            menu.clearScreen()

        elif user_choice == 2:
            gamescount = len(games)
            for i in range(gamescount):
                print(f"{i + 1} - {str(games[i]["name"])}")
            choice = input("What match to show?(leave blank to exit)\n")
            if choice != '':
                stats.showStats(int(choice) - 1)
            input()
            menu.clearScreen()

        elif user_choice == 3:
            stats.statsReview()
            input()
            menu.clearScreen()

        elif user_choice == 5:
            '''
            menu.clearScreen()
            print("Coach mode is a mode that helps to track statistics of all your players")
            if input("Enable? (Y/N)") == "Y":
                data_handler.enableCoachMode()
                print("Enabled!")
            else:
                pass
            '''
            print("Coach mode is currently under work. Stay tuned for updates")
            input()
            menu.clearScreen()
            pass

        elif user_choice == 6:
            menu.clearScreen()
            menu.showInfo(VERSION, True)
            input()
            menu.clearScreen()
        elif user_choice == 7:
            break

main()
db.save()
exit()