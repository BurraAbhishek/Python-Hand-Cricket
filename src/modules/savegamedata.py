import random
import string
import time
import json


def generateFilename(size):
    game_data_savename = ''.join([random.choice(string.ascii_uppercase
        + string.ascii_lowercase + string.digits) for n in range(12)])
    return game_data_savename


def getUniqueSavefile():
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


def saveGame(data):
    filename = getUniqueSavefile()
    savefile = open(filename, 'w')
    json.dump(data, savefile, indent=4)
    savefile.close()


def saveGameToID(data, gameid):
    filename = "saved_games/" + gameid + ".json"
    savefile = open(filename, 'w')
    json.dump(data, savefile, indent=4)
    savefile.close()
