
import random as rn
import time
from pythonImp import easy_implementation as game

def random_approach(runs = 1000):

    points = []
    amountOf2048 = 0
    highestBox = 0
    for i in range(runs):
        a_game = game()
        finished = False

        while not finished:
            move = rn.choice(['w','a','s','d'])
                                        # oneStep = False, move = None, verbose = True
            finished = a_game.run(oneStep=True, move=move, verbose=False)
            #time.sleep(0.2)
        points.append(a_game.points)
        if a_game.cracked_2048 == True:
            amountOf2048 += 1
        highestBox = a_game.highest_box
    return (amountOf2048, points, highestBox)
