#Guess the number game
#Import necesary modules
import random
import time
#pick a number
number=random.randint(1,100)

def intro():
    print("May I ask u ur name pls?????")
    global name
    name=input()#asks for name
    print(name +",we are going to play a game!!!!!!.I am thinking of a number between 1 to 100")
    if(number%2==0):
        x='even'
    else:
        x='odd'
    print("\nThis is an {} number".format(x))
    time.sleep(1.5)
    print("Go ahead.Guess!")

def pick():
    guessesTaken=0
    #if number taken is less than 6 
    while guessesTaken<6:
        time.sleep(.25)
        #insert pplace to enter guess
        enter=input("Guess: ")
        #Check if a nnumber was entered
        try:
            guess=int(enter)
            
            if guess<=100 and guess>=1:
                guessesTaken=guessesTaken+1
                if guessesTaken<6:
                    if guess<number:
                        print("THE GUESS U ENTERED IS TOO SMALL..........")
                    if guess>number:
                        print("THE GUESS U ENTERED IS TOO BIG.........")
                    if guess !=number:
                        time.sleep(.5)
                        print("TRY AGAIN")
                    if guess==number:
                        break
            if guess>100 or guess<1:
                print("Silly goose!That number is not in the range")
                time.sleep(.25)
                print("Plese enter a number between 1 to 100")

        except:print("I don't think that"+enter+"is a number...sorry")

    if guess==number:
        guessesTaken=str(guessesTaken)
        print('Good job,{}!You have guessed my number in {} guesses! '.format(name,guessesTaken))
    if guess!=number:
        print('Nope.the number i was thinking of was'+str(number))
playagain="yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes" or playagain=="YES" or playagain=="Y":
    intro()
    pick()
    print("Do u want to play again")
    playagain=input()

    



