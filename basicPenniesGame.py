from random import randint

playerWins = 0
computerWins = 0

totalPennies = 20
numberOfPenniesQuestion = "How many pennies would you like to take, please pick a number between 1-5: "


def turn(playerSelected):
    global playerWins
    global computerWins

    if playerSelected:
        currentPennies = totalPennies
        while currentPennies > 1:
            numberSelected = int(raw_input(numberOfPenniesQuestion))

            if numberSelected < 0 or numberSelected > 5:
                print "That is not a valid entry"
                continue
            elif numberSelected == currentPennies - 1:
                playerWins += 1
                print "You win!\nThe current score is \nHuman: " + str(playerWins) + "\nComputer: " + str(computerWins)
                playAgain()
                break

            currentPennies = currentPennies - int(numberSelected)

            computerSelection = randint(1, 5)

            print "You selected " + str(
                numberSelected) + " pennies" + "\nThe number of pennies remaining in the pile is: " + \
                  str(currentPennies) + " " + (currentPennies * "o")

            if currentPennies <= 6:
                finalPick = (currentPennies - 1)
                currentPennies = currentPennies - finalPick
                computerWins += 1
                print "\nThe computer has selected " + str(
                    finalPick) + " pennies" + "\nThe number of pennies remaining in the pile is: " + \
                      str(currentPennies) + " " + (currentPennies * "o")

                print "You lose!\nThe current score is \nHuman: " + str(playerWins) + "\nComputer: " + str(computerWins)
                playAgain()
                break

            else:
                currentPennies = currentPennies - computerSelection

                print "\nThe computer has selected " + str(
                    computerSelection) + " pennies" + "\nThe number of pennies remaining in the pile is: " + \
                      str(currentPennies) + " " + (currentPennies * "o")


    else:
        currentPennies = totalPennies
        while currentPennies > 1:
            computerSelection = randint(1, 5)

            if currentPennies <= 6:
                finalPick = (currentPennies - 1)
                currentPennies = currentPennies - finalPick
                computerWins += 1
                print "\nThe computer has selected " + str(
                    finalPick) + " pennies" + "\nThe number of pennies remaining in the pile is: " + \
                      str(currentPennies) + " " + (currentPennies * "o")

                print "You lose!\nThe current score is \nHuman: " + str(playerWins) + "\nComputer: " + str(computerWins)
                playAgain()
                break

            else:
                currentPennies = currentPennies - computerSelection

                print "\nThe computer has selected " + str(
                    computerSelection) + " pennies" + "\nThe number of pennies remaining in the pile is: " + \
                      str(currentPennies) + " " + (currentPennies * "o")
            numberSelected = int(raw_input(numberOfPenniesQuestion))

            if numberSelected < 0 or numberSelected > 5:
                print "That is not a valid entry"
                continue
            elif numberSelected == currentPennies - 1:
                playerWins += 1
                print "You win!\nThe current score is \nHuman: " + str(playerWins) + "\nComputer: " + str(computerWins)
                playAgain()
                break

            currentPennies = currentPennies - int(numberSelected)

            print "You selected " + str(
                numberSelected) + " pennies" + "\nThe number of pennies remaining in the pile is: " + \
                  str(currentPennies) + " " + (currentPennies * "o")


def start_game():
    welcomeMessage = "\nWelcome to the Pennies game.\nWould you like to go first or would you like the computer to go first?." \
                     "\nPlease type 'me' to go first or 'computer' to let the computer take the first turn: "
    playerSelect = raw_input(welcomeMessage)

    if playerSelect == "me":
        turn(True)

    elif playerSelect == "computer":
        turn(False)

    else:
        print "Sorry thats not a valid entry, lets try again!"
        start_game()


def playAgain():
    playQuestion = "\nWould you like to play again? Please type Yes or No: "

    userSelection = raw_input(playQuestion)

    cleanedSelection = userSelection.lower()

    if cleanedSelection == "yes":
        start_game()
    else:
        print "Goodbye!"


start_game()
