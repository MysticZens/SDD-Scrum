import random
import math
import csv

size = 20
turn = 0
coin = 16
emptyBuilding = "   "
gridList = []

rowList = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
           "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
columnList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
highscorefile = "Highscore.csv"
validation = True
score = 0


buildingList = ["R", "I", "C", "O", "*"]
buildingNameList = ["a Residential", "an Industry", "a Commercial", "a Park", "a Road"]

def createMap(size, gridList):
    # Create List for number of rows and columns
    rowList = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
               "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
    columnList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                  "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
    index = 0

    # This is the horizontal borders you see in the map
    border_horizontal = "  " + ("+-----" * size) + "+"

    # Lettering for the rows
    rowLetters = " "

    for a in range(size):
        rowLetters += "    {:1s} ".format(rowList[a])

    # Print the rows and columns of the map itself
    print(rowLetters)
    for x in range(size):
        print(border_horizontal)
        print("{:>2}".format(columnList[x]), end="")

        for y in range(size):
            print("| {:^3s} ".format(gridList[index]), end="")
            index += 1

        print("|")

    print(border_horizontal)


def adjacentEmptyValidation(locationIndex, validation, size, turn, gridList):
    # Define variable
    multiples = []

    # Right side

    if locationIndex < size ** 2:

        if gridList[locationIndex] != emptyBuilding:

            for b in range(size - 1, size ** 2, size):
                multiples.append(b)

            # Check if location at right border
            if locationIndex - 1 not in multiples:
                
                return

            multiples.clear()

    # Left side
    if locationIndex > 0:

        if gridList[locationIndex - 2] != emptyBuilding:

            for c in range(0, size ** 2, size):
                multiples.append(c)

            # Check if location at left border
            if locationIndex - 1 not in multiples:
                
                return

            multiples.clear()

    # Up
    # Check if location at up border
    if locationIndex - 1 - size >= 0:

        if gridList[locationIndex - 1 - size] != emptyBuilding:
            
            return 
    # Down
    # Check if location at up border
    if locationIndex - 1 + size < size ** 2:

        if gridList[locationIndex - 1 + size] != emptyBuilding:
            
            return 

    count = 0
    for i in range(len(gridList)):
        if gridList[i] == emptyBuilding:
            count += 1

    if (count == size ** 2):
        return

    if gridList[locationIndex - 1] == emptyBuilding:
        validation = False
        print("You must build next to an existing building.")

    return validation


def calculateScores(size, turn, gridList):
    # Use the same adjacency check from AdjacentValidation
    # Define variable
    # Will define if adjacent side is near a corner
    adjacent = [emptyBuilding, emptyBuilding, emptyBuilding, emptyBuilding]
    multiples = []
    score = 0


    # Loop for each element in gridList
    for index in range(len(gridList)):

        # Right side
        if index + 1 < size ** 2:

            for b in range(size - 1, size ** 2, size):
                multiples.append(b)

            # Check if location at right border
            if index not in multiples:
                adjacent[0] = gridList[index + 1]


            multiples.clear()

        # Left side
        if index >= 0:

            for c in range(0, size ** 2, size):
                multiples.append(c)

            # Check if location at left border
            if index not in multiples:

                adjacent[1] = gridList[index - 1]


            multiples.clear()

        # Up
        # Check if location at up border
        if index - size > 0:

            adjacent[2] = gridList[index - size]


        # Down
        # Check if location at up border
        if index + size < size ** 2:

            adjacent[3] = gridList[index + size]

        # Calculate point for beach
        if gridList[index] == "R":
            if adjacent[0] == "I" or adjacent[0] == "R" or adjacent[0] == "C": 
                score += 1

            if adjacent[1] == "I" or adjacent[1] == "R" or adjacent[1] == "C":
                score += 1

            if adjacent[2] == "R" or adjacent[2] == "C":
                score += 1

            if adjacent[3] == "R" or adjacent[3] == "C":
                score += 1

            if adjacent[0] == "O": 
                score += 1

            if adjacent[1] == "O":
                score += 1

            if adjacent[2] == "O":
                score += 1

            if adjacent[3] == "O":
                score += 1


        # Calculate point for factories
        elif gridList[index] == "I":
            score += 1

        # Calculate points for houses
        elif gridList[index] == "C":
            if adjacent[0] == "C": 
                score += 1
            
            if adjacent[1] == "C":
                score += 1

            if adjacent[2] == "C":
                score += 1

            if adjacent[3] == "C":
                score += 1

        elif gridList[index] == "O":
            if adjacent[0] == "O": 
                score += 1

            if adjacent[1] == "O":
                score += 1

            if adjacent[2] == "O":
                score += 1

            if adjacent[3] == "O":
                score += 1

        # Calculate points for Highway
        elif gridList[index] == "*":
            if adjacent[0] == "*":
                score += 1
            if adjacent[1] == "*":
                score += 1

    return score

def calculateCoins(size, turn, gridList):
    # Use the same adjacency check from AdjacentValidation
    # Define variable
    # Will define if adjacent side is near a corner
    adjacent = [emptyBuilding, emptyBuilding, emptyBuilding, emptyBuilding]
    multiples = []
    coin = 0

    # Loop for each element in gridList
    for index in range(len(gridList)):

        # Right side
        if index + 1 < size ** 2:

            for b in range(size - 1, size ** 2, size):
                multiples.append(b)

            # Check if location at right border
            if index not in multiples:
                adjacent[0] = gridList[index + 1]


            multiples.clear()

        # Left side
        if index >= 0:

            for c in range(0, size ** 2, size):
                multiples.append(c)

            # Check if location at left border
            if index not in multiples:

                adjacent[1] = gridList[index - 1]


            multiples.clear()

        # Up
        # Check if location at up border
        if index - size > 0:

            adjacent[2] = gridList[index - size]


        # Down
        # Check if location at up border
        if index + size < size ** 2:

            adjacent[3] = gridList[index + size]





        # Calculate point for factories
        if gridList[index] == "I":
            if adjacent[0] == "R": 
                coin += 1

            if adjacent[1] == "R":
                coin += 1

            if adjacent[2] == "R":
                coin += 1

            if adjacent[3] == "R":
                coin += 1
                            
            '''industrialScoreList.append(1)

            if len(industrialScoreList) <= 4:

                for x in range(len(industrialScoreList)):
                    industrialScoreList[x] = len(industrialScoreList)'''


        # Calculate points for houses
        elif gridList[index] == "C":
            if adjacent[0] == "R": 
                coin += 1

            if adjacent[1] == "R":
                coin += 1

            if adjacent[2] == "R":
                coin += 1

            if adjacent[3] == "R":
                coin += 1
                        
            '''for x in adjacent:

                if x == "FAC":
                    houseScore = 1
                    break

                elif x == "HSE" or x == "SHP":
                    houseScore += 1

                elif x == "BCH":
                    houseScore += 2

                else:
                    continue

            houseScoreList.append(houseScore)
            houseScore = 0'''

    return coin

# Main Menu
print("Welcome, mayor of Ngee Ann City!\
     \n----------------------------")

while True:
    print("\n1. Start new game\
           \n2. Load save game\
           \n3. Show high scores\
           \n\
           \n0. Exit")

    while True:
        # Ask for an input from the player
        playerChoice = input("Your choice? ")

        # quit game
        if playerChoice == "0":
            quit()

        # Load Saved Game
        elif playerChoice == "2":
            print('Not implemented.')

        # Show highscores
        elif playerChoice == "3":
            print('Not implemented.')
        # Check the input the player has put in
        # Check if the player starts a new game
        elif playerChoice == "1":
            turn = 0
            gridList = []

            # Create an element for each tile in map in gridList
            for x in range(size ** 2):
                gridList.append(emptyBuilding)

            break

        else:
            print("Please input another value.")

    # Loop Turns until player wants to stop or Game Ends
    while True:

        # Print turn number
        if playerChoice == "1" or playerChoice == "2" or playerChoice == "4":
            turn += 1

        print("\nTurn", turn)

        # End of game Sequence
        if (all(item is not emptyBuilding for item in gridList) and emptyBuilding not in gridList) or coin <= 0:

            # Print final message
            print("\nFinal layout of Ngee Ann City: ")

            # Create Map
            createMap(size, gridList)

            break

        # Print the map
        print("Coins: " + str(coin))
        print("Current score: " + str(score))
        createMap(size, gridList)

        # Create the randomiser for the houses
        if playerChoice == "1" or playerChoice == "2":
            randint1 = random.randint(0, len(buildingList) - 1)
            randint2 = random.randint(0, len(buildingList) - 1)

            building1 = buildingList[randint1]
            building2 = buildingList[randint2]
            building_name1 = buildingNameList[randint1]
            building_name2 = buildingNameList[randint2]

        # Print the instructions
        print("1. Build {:1s}\
             \n2. Build {:1s}\
             \n3. Save game\
             \n4. Destroy building\
             \n0. Exit to main menu".format(building_name1 + " (" + building1 + ")", building_name2 + " (" + building2 + ")"))

        # Ask input from player
        playerChoice = input("Please enter your choice? ")

        # check if player wants to build
        if playerChoice == "1" or playerChoice == "2":

            # Check where to build
            # Input validation
            while True:
                try:
                    location = input("Where do you want to build a building? ")

                except:
                    print("Please enter a valid input.")
                    continue

                if rowList.count(location[0]) == 0:
                    print("Please enter a valid input.")
                    continue

                elif location[1].isnumeric() == False:
                    print("Please enter a valid input.")
                    continue

                elif location[1] == "0":
                    print("Please enter a valid input.")
                    continue

                else:
                    break

            # Translate input to location on map
            if len(location) == 2:
                locationIndex = (rowList.index(
                    location[0]) + 1) + ((int(location[1]) - 1) * size)

            elif len(location) == 3:
                locationIndex = (rowList.index(
                    location[0]) + 1) + ((int(location[1:3]) - 1) * size)

            # Validate placement
            # If location is adjacent.
            validation = adjacentEmptyValidation(
                locationIndex, validation, size, turn, gridList)

            # If location is occupied
            if gridList[locationIndex - 1] != emptyBuilding:
                print("This location is already occupied.")
                validation = False

            while validation == False:
                location = input("Where do you want to build a building? ")
                if len(location) == 2:
                    locationIndex = (rowList.index(
                    location[0]) + 1) + ((int(location[1]) - 1) * size)
                    

                elif len(location) == 3:
                    locationIndex = (rowList.index(
                        location[0]) + 1) + ((int(location[1:3]) - 1) * size)                
                validation = adjacentEmptyValidation(
                    locationIndex, validation, size, turn, gridList)

                if gridList[locationIndex - 1] != emptyBuilding:
                    print("This location is already occupied.")
                    validation = False
                    continue

            # Place the building on mapGrid
            if (playerChoice == "1"):
                gridList[locationIndex - 1] = building1

            else:
                gridList[locationIndex - 1] = building2
            score += calculateScores(size, turn, gridList)
            coin += calculateCoins(size, turn, gridList)
            coin -= 1
            
        # Save the game
        elif playerChoice == "3":
            print("Not implemented.")
            break

        elif playerChoice == "4":
            if turn <= 1:
                print("No buildings have been built yet!")

            else:
                while True:
                    try:
                        location = input("Where do you want to remove the building? ")
                    
                    except:
                        print("Please enter a valid input.")
                        continue

                    if rowList.count(location[0]) == 0:
                        print("Please enter a valid input.")
                        continue

                    elif location[1].isnumeric() == False:
                        print("Please enter a valid input.")
                        continue

                    elif location[1] == "0":
                        print("Please enter a valid input.")
                        continue

                    else:
                        break

                if len(location) == 2:
                    locationIndex = (rowList.index(
                        location[0]) + 1) + ((int(location[1]) - 1) * size)
                    
                elif len(location) == 3:
                    locationIndex = (rowList.index(
                        location[0]) + 1) + ((int(location[1:3]) - 1) * size)

                validation = True
                
                if gridList[locationIndex - 1] == emptyBuilding:
                    print("There is no building to destroy in this location " + location + ". Please try again.")
                    validation = False

                while validation == False:
                    location = input("Where do you want to remove the building? ")
                    if len(location) == 2:
                        locationIndex = (rowList.index(
                        location[0]) + 1) + ((int(location[1]) - 1) * size)

                    elif len(location) == 3:
                        locationIndex = (rowList.index(
                            location[0]) + 1) + ((int(location[1:3]) - 1) * size)

                    if gridList[locationIndex - 1] == emptyBuilding:
                        print("There is no building to destroy in this location " + location + ". Please try again.")
                        validation = False
                        continue

                    else:
                        validation = True
                score -= calculateScores(size, turn, gridList)    
                gridList[locationIndex - 1] = emptyBuilding
                score += calculateScores(size, turn, gridList)
                coin -= 1

        # Exit to main menu
        elif playerChoice == "0":
            print("-------------------------")
            print(" Returning to main menu! ")
            print("-------------------------")
            break

         # For input validation
        else:
            print("Please enter a valid input.")
