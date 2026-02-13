import json

try:
    with open('data.json', 'r', encoding='utf-8') as f:
        db = json.load(f)
except FileNotFoundError:
    player = input("Enter your name: ")
    db = {"player": player, "games": []}

def add_match(name, date, points, assists, rebounds, blocks, steals, missed, missedFT, losses, TO, Result):
    new_game = {
        "name": str(name),
        "date": str(date),
        "points": int(points),
        "assists": int(assists),
        "rebounds": int(rebounds),
        "blocks": int(blocks),
        "steals": int(steals),
        "missed": int(missed),
        "missedFT": int(missedFT),
        "losses": int(losses),
        "turnovers": int(TO),
        "Won": bool(Result)
                }

    db["games"].append(new_game)
    
def calculateSeasonStatistics(allpoints, allassists, allrebounds, allblocks, allsteals, allmissed, allmissedFT, allTO, games):
    pointsPerGame = allpoints / games
    assistsPerGame = allassists / games
    reboundsPerGame = allrebounds / games
    blocksPerGame = allblocks / games
    stealsPerGame = allsteals / games
    missedPerGame = allmissed / games
    missedFreeThrowsPerGame = allmissedFT / games
    turnoversPerGame = allTO / games

def save():
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent = 4)