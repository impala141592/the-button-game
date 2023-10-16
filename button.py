import random
from getkey import getkey, keys


score = 0
gameOver = False
randomNum = random.randint(1, 100)
failPercentage = 1


def button():
    global score
    global gameOver
    global randomNum
    global failPercentage
    
    while gameOver == False :
        key = getkey("press enter to play")
        if key == keys.ENTER :
            score += 1
            if failPercentage < 100 :
                failPercentage += 1
                randomNum = random.randint(1, 100)
                print("your score is:", score)  



button()