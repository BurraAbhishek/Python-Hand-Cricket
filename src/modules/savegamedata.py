import random
import string
import json


def generateFilename(size: int) -> str:
    game_data_savename = ''.join([random.choice(string.ascii_uppercase
        + string.ascii_lowercase + string.digits) for _ in range(size)])
    return game_data_savename


def getUniqueSavefile() -> str:
    gamefile = generateFilename(16)
    filename = "saved_games/" + gamefile + ".json"
    result = False
    try:
        f = open(filename, 'r')
        f.close()
    except:
        result = True
    if result:
        result_file = filename
    else:
        result_file = getUniqueSavefile()
    return result_file


def saveGame(data: dict) -> None:
    filename = getUniqueSavefile()
    savefile = open(filename, 'w')
    json.dump(data, savefile, indent=4)
    savefile.close()


def saveGameToID(data: dict, gameid: str) -> None:
    filename = "saved_games/" + gameid + ".json"
    savefile = open(filename, 'w')
    json.dump(data, savefile, indent=4)
    savefile.close()
