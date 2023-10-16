import random
from getkey import getkey, keys


score = 0
gameOver = False
randomNum = random.randint(1, 100)
failPercentage = 1

print("THE BUTTON GAME")

def button():
    global score
    global gameOver
    global randomNum
    global failPercentage

    while gameOver == False :

        if randomNum == failPercentage:
            gameOver = True
            print("GAME OVER")
        else:
            key = getkey("press enter to play")

            if key == keys.ENTER :
                score += 1
                if failPercentage < 100 :
                    failPercentage += 1
                    randomNum = random.randint(1, 100)
                    print("your score is:", score)

            elif key == keys.ESC :
                gameOver = True
                print("GAME OVER")

            else :
                print("press enter to play or esc to exit")



button()