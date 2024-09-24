# IMPORTING THE RANDOM MODULE FOR RANDOM NUMBERS FOR PILES
from random import randint,choice
from time import sleep
import sys

# SETTING UP GAME
numOfRockPiles = 4
rockPiles = []
for i in range(numOfRockPiles):
    rockPiles.append(randint(1,10)) # SETTING UP THE NUMBER OF ROCKS FOR EACH PILE
winnerDecided = False
currentPlayer = 1

# WELCOME STATEMENT
print('-'*48)
print("Welcome to the Game of Nim!")
print('-'*48)
print()

# INSTRUCTIONS
print("Here's how to play Nim:")
print('-'*48)
print(f"You will be a given {numOfRockPiles} piles of rocks, with each pile containing a number of rocks.")
print(f"You are able to take any number of rocks from the {numOfRockPiles} piles.")
print("The goal of this game is to not take the last rock present.")
print()
print("That is, if all the other piles have 0 rocks, and the current pile has one rock,")
print("and it is your turn, you will lose as you take the last rock.")
print()

# INPUTTING WHETHER THE USER WANTS TO PLAY AGAINST A COMPUTER OR PLAYER
enemyType = input("Do you want to play against another player or a computer? (P/C): ").lower()

if enemyType == "p":
    while winnerDecided == False:
        print(f"\nIt is currently Player {currentPlayer}'s turn.")

        print("\nHere's the amount of rocks in each pile:")
        for rockPile in range(numOfRockPiles):
            print(f"Rock Pile {rockPile+1} has {rockPiles[rockPile]} rocks.")

        userPileNum = int(input((f"\nPlayer {currentPlayer}, which pile would you like to take from? ")))

        if 1 <= userPileNum <= numOfRockPiles:
            numRockPile = rockPiles[userPileNum-1]
            takenRocks = int(input(f"How many rocks would you like to take from pile {userPileNum}? "))

            if takenRocks <= numRockPile: # SUBTRACTING 1 BECAUSE LISTS ARE ZERO-INDEXED
                numRockPile -= takenRocks
                rockPiles[userPileNum-1] = numRockPile # SETTING THE VALUE IN THE LIST TO THE NEW ROCK PILE
                print(f"\nPile {userPileNum} now has {numRockPile} rocks.")
                
                # CHECKING IF THE CURRENT PLAYER TOOK ALL THE ROCKS, THEY LOSE
                if sum(rockPiles) == 0:
                    print(f"Unfortunately Player {currentPlayer}, you took the last rock which means you lose.")
                    
                    if currentPlayer == 1:
                        print("Player 2 wins and Player 1 loses!")
                    
                    else:
                        print("Player 1 wins and Player 2 loses!")
                    winnerDecided = True

                # ADVANCING PLAYER TURNS
                if currentPlayer == 1:
                    currentPlayer = 2
    
                else:
                    currentPlayer = 1
else:
    while winnerDecided == False:
        if currentPlayer == 1:
            print("\nIt is currently your turn.")
        else:
            print("\nIt is currently the computer's turn.")

        print("\nHere's what the current piles look like:")
        for rockNum in range(numOfRockPiles):
            print(f"Rock Pile {rockNum+1} currently has {rockPiles[rockNum]} rocks.")

        if currentPlayer == 1:
            userPileNum = int(input("\nWhich pile would you like to take from? "))
            while not 1 <= userPileNum <= numOfRockPiles:
                userPileNum = int(input("\nWhich pile would you like to take from? "))

            numRockPile = rockPiles[userPileNum-1]
            takenRocks = int(input(f"How many rocks would you like to take from pile {userPileNum}? "))
            while not takenRocks <= numRockPile:
                takenRocks = int(input(f"How many rocks would you like to take from pile {userPileNum}? "))

            if takenRocks <= numRockPile:
                numRockPile -= takenRocks
                rockPiles[userPileNum-1] = numRockPile
                print(f"\nPile {userPileNum} now has {numRockPile} rocks.")

            if sum(rockPiles) == 0:
                print("\nUnfortunately, you took the last rock which means the computer wins!")
                winnerDecided = True

            currentPlayer = 2
    
        else:
            # CHECKING FOR A WIN ON CURRENT MOVE
            winningMoveFound = False
            pilesWithRocks = []
            for pileNum in range(numOfRockPiles):
                if rockPiles[pileNum] > 0:
                    pilesWithRocks.append(pileNum)

            if len(pilesWithRocks) == 1:
                pileNum = pilesWithRocks[0]
                computerPileDecision = pileNum+1
                if rockPiles[pileNum] == 1:
                    computerRemovalDecision = 1
                else:
                    computerRemovalDecision = rockPiles[pileNum]-1
                rockPiles[pileNum] -= computerRemovalDecision
                winningMoveFound = True

            elif len(pilesWithRocks) == 2:
                pileNum1,pileNum2 = pilesWithRocks[0],pilesWithRocks[1]
                if rockPiles[pileNum1] == 1:
                    computerPileDecision = pileNum2+1
                    computerRemovalDecision = rockPiles[pileNum2]
                    rockPiles[pileNum2] -= computerRemovalDecision
                    winningMoveFound = True

                elif rockPiles[pileNum2] == 1:
                    computerPileDecision = pileNum1+1
                    computerRemovalDecision = rockPiles[pileNum1]
                    rockPiles[pileNum1] -= computerRemovalDecision
                    winningMoveFound = True

            if winningMoveFound == False:

                computerPileDecision = -1
                computerRemovalDecision = -1
                
                for pileNum in range(numOfRockPiles):
                    originalNumOfRocks = rockPiles[pileNum]
                    currentNumOfRocks = rockPiles[pileNum]-1

                    while currentNumOfRocks >= 0:
                        curNimSum = currentNumOfRocks

                        for pileNum2 in range(numOfRockPiles):
                            if pileNum != pileNum2:
                                curNimSum ^= rockPiles[pileNum2]

                        if curNimSum == 0:
                            computerPileDecision = pileNum + 1
                            if currentNumOfRocks == 0 and len(pilesWithRocks)-1 <= 2:
                                computerRemovalDecision = 1
                            else:
                                computerRemovalDecision = originalNumOfRocks - currentNumOfRocks
                            rockPiles[pileNum] -= computerRemovalDecision
                            break

                        else:
                            currentNumOfRocks -= 1
                
                if computerPileDecision == -1:
                    computerPileDecision = choice(pilesWithRocks)
                    computerRemovalDecision = randint(1,rockPiles[computerPileDecision])
                    rockPiles[computerPileDecision] -= computerRemovalDecision
                    print("BEEN HERE BEFORE")
                
            print("\nThe computer is thinking")
            for thinkingDot in range(3):
                print('.')
                sleep(1)
                
            print(f"\nThe Computer has decided to remove rocks from pile {computerPileDecision}.")
            print(f"The Computer removed {computerRemovalDecision} rocks from pile {computerPileDecision}")
            
            if sum(rockPiles) == 0:
                print("Congratulations! You made the computer take the last rock. You Win!")
                winnerDecided = True
            currentPlayer = 1
            

