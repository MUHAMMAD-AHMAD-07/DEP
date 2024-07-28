import random

class NimComputer:

    def __init__():

        marbleList=[3,5]
        player=1
        flag=0
        gameover=0
        computerWin=0;

        while True:
            print("Please select the Game Version: \n")
            print("1.Standard Version")
            print("2.Misere Version")
            version= int(input())
            if version in [1,2]:
                break
            else:
                print("Invalid Move !")

        if version == 1:
            flag=1

        while True:
            print()
            print("Current Status of marbles: ")
            print("1.Red marbles= " + str(marbleList[0]))
            print("2.Blue marbles= "+ str(marbleList[1])+"\n")

            if player%2==0 :
                print("Computer turn !")
                while True:
                    comMarbleType= random.randint(0,1)
                    if marbleList[comMarbleType]>0:
                        break
                comMarbleAmout= random.randint(1,marbleList[comMarbleType])
                marbleList[comMarbleType] -= comMarbleAmout

                if comMarbleType == 0:
                    print("Computer removed "+ str(comMarbleAmout) + " Red marbles !")
                else :
                    print("Computer removed "+ str(comMarbleAmout) + " Blue marbles !")
                print()
                print("Current Status of marbles: ")
                print("1.Red marbles= " + str(marbleList[0]))
                print("2.Blue marbles= "+ str(marbleList[1])+"\n")
                player+=1
                if marbleList[0] == 0 and marbleList[1] == 0:
                    gameover=1;
                    computerWin=1;        
            if gameover==0 :

                while True:
                    print("Player 1 turn !")    
                    marble_type= int(input("Enter 1 or 2 remove Red marbles or Blue marbles respectively:\n"))-1
                    if marble_type in [0,1]:
                        break;
                    else:
                        print("Invalid Move !") 

                while True:
                    marble_amount= int(input("Please enter amount of marbles you want to remove:\n"))
                    if marble_amount > marbleList[marble_type] or marble_amount < 1:
                        print("Invalid Move !")
                    else:
                        break;

                marbleList[marble_type]=marbleList[marble_type]-marble_amount;
        
            if marbleList[0] == 0 and marbleList[1] == 0:
                print()
                print("Game has Ended !")
                if flag==1:
                    if computerWin==1:
                        print("Computer Wins !")
                    else :
                        print("Human Wins !")
                else:
                    if computerWin==1:
                        print("Human Wins !")
                    else:
                        print("Computer Wins !")        
                break

            player+=1

    __init__()