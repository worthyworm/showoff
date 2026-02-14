import data_handler
import ui_handler
from ui_handler import menu
import time

VERSION = 1
db = data_handler
ui = ui_handler
games = data_handler.db["games"]

def main():

    while True:
        menu.showInfo(VERSION, False)
        user_choice = menu.createMenu()

        if user_choice == 1:
            db.add_match(input("Enter name for a match: "),
                input("Enter date: "), 
                int(input("Enter points: ")), 
                int(input("Enter assists: ")), 
                int(input("Enter rebounds: ")), 
                int(input("Enter blocks: ")), 
                int(input("Enter steals: ")), 
                int(input("Enter missed shots excluding free throws: ")), 
                int(input("Enter missed free throws: ")), 
                int(input("Enter ball losses: ")), 
                int(input("Enter turnovers: ")), 
                bool(input("Result (True for W/False for L): ")))
            print("Added!")
            db.save()
            input()
            menu.clearScreen()

        elif user_choice == 2:
            allPoints = sum(game["points"] for game in games)
            allAssists = sum(game["assists"] for game in games)
            allRebounds = sum(game["rebounds"] for game in games)
            allBlocks = sum(game["blocks"] for game in games)
            allSteals = sum(game["steals"] for game in games)
            allMissed = sum(game["missed"] for game in games)
            allMissedFreeThrows = sum(game["missedFT"] for game in games)
            allTurnOvers = sum(game["turnovers"] for game in games)
            allGames = len(games)

            print(f'''
                Season Points : {allPoints}
                Season Assists : {allAssists}
                Season Rebounds : {allRebounds}
                Season Blocks : {allBlocks}
                Season Steals : {allSteals}
                Season Shots Missed : {allMissed}
                Season Free Throws Missed : {allMissedFreeThrows}
                Season Turnovers : {allTurnOvers}
                Points Per game : {allPoints / allGames}
                Assists Per game : {allAssists / allGames}
                Rebounds Per game : {allRebounds / allGames}
                Blocks Per game : {allBlocks / allGames}
                Steals Per game : {allSteals / allGames}
                Missed Shots Per game : {allMissed / allGames}
                Missed Free Throws Per game : {allMissedFreeThrows / allGames}
                Turnovers Per game : {allTurnOvers / allGames}
                Season Games : {allGames}
                ''')
            input()
            menu.clearScreen()

        elif user_choice == 4:
            menu.clearScreen()
            menu.showInfo(VERSION, True)
            input()
            menu.clearScreen()
        elif user_choice == 5:
            break

main()
db.save()
exit()