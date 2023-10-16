import random
from getkey import getkey, keys
import datetime

score = 0
gameOver = False
failPercentage = 1
randomNum = random.randint(failPercentage, 100)

print('\033[36;1m' + "THE BUTTON GAME" + '\033[m')
print("\n • hit" + "\033[1m" , "ENTER" , '\033[m' + "to get 1 point \n • everytime you hit enter you also increase your odds to lose by 1% \n • to exit hit" + "\033[1m" , "ESCAPE" , '\033[m' + "\n ")

def button():
    global score
    global gameOver
    global randomNum
    global failPercentage

    name = input('\33[36;1m' + "enter your name to proceed: " + '\033[m')

    while gameOver == False :

        if randomNum == failPercentage:
            gameOver = True
            print('\33[31;1m' + "GAME OVER \n" + '\033[m')
            with open('scoreboard.txt', 'a') as file:
                file.write(str(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) + " " + name + ": " + str(score) + "\n")
            with open('scoreboard.txt', 'r') as file:
                print(file.read())

        elif failPercentage == 100 :
            gameOver = True
            print('\033[36;1m' + "YOU WIN!" + '\033[m')
            with open('scoreboard.txt', 'a') as file:
                file.write(str(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) + " " + name + ": " + str(score) + "\n")
            with open('scoreboard.txt', 'r') as file:
                print(file.read())

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
                print('\33[31;1m' + "GAME OVER \n" + '\033[m')
                with open('scoreboard.txt', 'r') as file:
                    print(file.read())

            else :
                print("press enter to play or esc to exit")



button()