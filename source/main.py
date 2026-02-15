import data_handler
import ui_handler
from ui_handler import Menu
import statistics_handler

db = data_handler
ui = ui_handler
stats = statistics_handler
games = data_handler.db["games"]


def main():
    while True:
        Menu.show_info(False)
        user_choice = Menu.create_menu()

        if user_choice == 1:
            stats.add_match()
            print("Added!")
            db.save()
            input("Enter to continue... ")
            Menu.clear_screen()

        elif user_choice == 2:
            gamescount = len(games)
            for i in range(gamescount):
                print(f"{i + 1} - {str(games[i]['name'])}")
            choice = input("What match to show?(leave blank to exit)\n")
            if choice != '' and int(choice) - 1 in range(gamescount):
                stats.show_stats(int(choice) - 1)
            else:
                print("Game index out of range.")
            input("Enter to continue... ")
            Menu.clear_screen()

        elif user_choice == 3:
            stats.stats_review()
            input("Enter to continue... ")
            Menu.clear_screen()

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
            input("Enter to continue... ")
            Menu.clear_screen()
            pass

        elif user_choice == 6:
            Menu.clear_screen()
            Menu.show_info(True)
            input("Enter to continue... ")
            Menu.clear_screen()
        elif user_choice == 7:
            break


if __name__ == '__main__':
    main()
    db.save()
    exit()
