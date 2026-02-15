from pip._internal.utils.misc import tabulate

import data_handler

db = data_handler
games = data_handler.db["games"]


def stats_review():
    allPoints = sum(game["points"] for game in games)
    allAssists = sum(game["assists"] for game in games)
    allRebounds = sum(game["rebounds"] for game in games)
    allBlocks = sum(game["blocks"] for game in games)
    allSteals = sum(game["steals"] for game in games)
    allMissed = sum(game["missed"] for game in games)
    allMissedFreeThrows = sum(game["missedFT"] for game in games)
    allTurnOvers = sum(game["turnovers"] for game in games)
    allGames = len(games)
    efficiency = calculate_efficiency(allPoints, allRebounds, allAssists, allSteals, allBlocks, allMissed,
                                      allMissedFreeThrows, allTurnOvers)
    if allGames == 0:
        print("You have no saved games.")
        return '''
Points : {allPoints}
Assists : {allAssists}
Rebounds : {allRebounds}
Blocks : {allBlocks}
Steals : {allSteals}
Shots Missed : {allMissed}
Free Throws Missed : {allMissedFreeThrows}
Turnovers : {allTurnOvers}
Points Per game : {allPoints / allGames}
Assists Per game : {allAssists / allGames}
Rebounds Per game : {allRebounds / allGames}
Blocks Per game : {allBlocks / allGames}
Steals Per game : {allSteals / allGames}
Missed Shots Per game : {allMissed / allGames}
Missed Free Throws Per game : {allMissedFreeThrows / allGames}
Turnovers Per game : {allTurnOvers / allGames}
Games : {allGames}
Efficiency : {efficiency}
'''
    table = [["Points", allPoints, allPoints / allGames], ["Assists", allAssists, allAssists / allGames],
             ["Rebounds", allRebounds, allRebounds / allGames], ["Blocks", allBlocks, allBlocks / allGames],
             ["Steals", allSteals, allSteals / allGames], ["Missed", allMissed, allMissed / allGames],
             ["Missed Free Throws", allMissedFreeThrows, allMissedFreeThrows / allGames],
             ["Turnovers", allTurnOvers, allTurnOvers / allGames]]

    print(f"{'STAT':<20} {'ALL-TIME':<10} {'PER-GAME'}")
    print("─" * 35)
    for stat, ag, pg in table:
        print(f"{stat:<20} {ag:<10} {pg}")
    print("─" * 35)
    print(f"Games: {allGames}\nEfficiency: {efficiency}")
    print("─" * 35)


def add_match():
    db.add_match(input("Enter name for a match: "),
                 input("Enter date: "),
                 int(input("Enter points: ")),
                 int(input("Enter assists: ")),
                 int(input("Enter rebounds: ")),
                 int(input("Enter blocks: ")),
                 int(input("Enter steals: ")),
                 int(input("Enter missed shots excluding free throws: ")),
                 int(input("Enter missed free throws: ")),
                 int(input("Enter turnovers: ")),
                 bool(input("Result (True for W/False for L): ")))


def calculate_efficiency(points, rebounds, assists, steals, blocks, missed, missedFT, turnovers):
    efficiency = (points + rebounds + assists + steals + blocks) - (missed + missedFT + turnovers)
    return efficiency


def show_stats(matchIndex):
    table = [["Points", str(games[matchIndex]["points"])], ["Assists", str(games[matchIndex]["assists"])],
             ["Rebounds", str(games[matchIndex]["rebounds"])], ["Blocks", str(games[matchIndex]["blocks"])],
             ["Steals", str(games[matchIndex]["steals"])], ["Missed", str(games[matchIndex]["missed"])],
             ["Missed Free Throws", str(games[matchIndex]["missedFT"])],
             ["Turnovers", str(games[matchIndex]["turnovers"])], ["Won", str(games[matchIndex]["Won"])]]
    print(f"{'STAT':<20} {'VALUE'}")
    print("─" * 35)
    for stat, value in table:
        print(f"{stat:<20} {value}")
    print("─" * 35)
