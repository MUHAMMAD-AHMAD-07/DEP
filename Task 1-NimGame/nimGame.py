class NimPlayer:

    def __init__():

        marbleList=[3,5]
        player=1
        flag=0

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
                print("Player 2 turn !")
            elif player%2 !=0 :
                print("Player 1 turn !")

            while True:    
                marble_type= int(input("Enter 1 or 2 remove Red marbles or Blue marbles respectively:\n"))-1
                if marble_type in [0,1]:
                    break;
                else:
                    print("Invalid Move !") 

            while True:
                marble_amount= int(input("Please enter amount of marbles you want to remove:\n"))
                if marble_amount > marbleList[marble_type] or marble_amount < 1:
                    print("Invalid Move !")
                else: break;
                
            marbleList[marble_type]=marbleList[marble_type]-marble_amount;

            if marbleList[0] == 0 and marbleList[1] == 0:
                print()
                print("Game has Ended !")
                if flag==1:
                    if player%2==0 :
                        print("Player 2 Wins !")
                    elif player%2 !=0 :
                        print("Player 1 Wins !")
                else:
                    if player%2==0 :
                        print("Player 1 Wins !")
                    elif player%2 !=0 :
                        print("Player 2 Wins !")        
                print()
                print("Final Status of marbles: ")
                print("1.Red marbles= " + str(marbleList[0]))
                print("2.Blue marbles= "+ str(marbleList[1])+"\n")
                break

            player+=1

    __init__()