import data_handler

db = data_handler
games = data_handler.db["games"]

def statsReview():
    allPoints = sum(game["points"] for game in games)
    allAssists = sum(game["assists"] for game in games)
    allRebounds = sum(game["rebounds"] for game in games)
    allBlocks = sum(game["blocks"] for game in games)
    allSteals = sum(game["steals"] for game in games)
    allMissed = sum(game["missed"] for game in games)
    allMissedFreeThrows = sum(game["missedFT"] for game in games)
    allTurnOvers = sum(game["turnovers"] for game in games)
    allGames = len(games)
    efficiency = calculateEfficiency(allPoints, allRebounds, allAssists, allSteals, allBlocks, allMissed, allMissedFreeThrows, allTurnOvers)

    print(f'''
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
                ''')
    
def addMatch():
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

def calculateEfficiency(points, rebounds, assists, steals, blocks, missed, missedFT, turnovers):
    efficiency = (points + rebounds + assists + steals + blocks) - (missed + missedFT + turnovers)
    return efficiency

def showStats(matchIndex):
    print(f'''
Points : {str(games[matchIndex]["points"])}
Assists : {str(games[matchIndex]["assists"])}
Rebounds : {str(games[matchIndex]["rebounds"])}
Blocks : {str(games[matchIndex]["blocks"])}
Steals : {str(games[matchIndex]["steals"])}
Shots Missed : {str(games[matchIndex]["missed"])}
Free Throws Missed : {str(games[matchIndex]["missedFT"])}
Turnovers : {str(games[matchIndex]["turnovers"])}
''')