def main():
    turn = raw_input(
        "Welcome to the pennies game!\nPlease select who you would like to go first?\nPlease enter 'h' for human or 'c' for computer: ").lower()

    numberOfGames = input('How many games would you like to play?')

    printDivide()

    score = {'Human': 0, 'Computer': 0}

    match = {'score': score, 'games': numberOfGames, 'turn': turn}

    playMatch(match)


def playMatch(match):

    display_match_score(match)

    if match['games'] > 0:
        winner = play_game(20, match['turn'])
        if winner == 'h':
            score = {'Human': match['score']['Human'] + 1, 'Computer': match['score']['Computer']}
        else:
            score = {'Human': match['score']['Human'], 'Computer': match['score']['Computer'] + 1}

        match = {'score': score, 'games': match['games'] - 1, 'turn': togglePlayer(match['turn'])}

        playMatch(match)
    else:
        print "Match Over"


def printDivide():
    print "--------------------"

def togglePlayer(player):
    return 'c' if player == 'h' else 'h'

def display_match_score(match):
    print "{0} games remaining".format(match['games'])
    print "It is {0}'s turn".format(match['turn'])
    print "Human {0} : {1} Computer".format(match['score']['Human'], match['score']['Computer'])
    print


def display_game_score(took, remaining):
    print "{0} coins taken".format(took)
    print "There are {0} coins remaining".format(remaining)
    print


def play_game(pennies, turn):
    if pennies == 1:
        print "{0} loses".format(turn)
        return togglePlayer(turn)

    if turn == 'h':
        take = get_move_from_human(pennies)
    else:
        take = get_move_from_computer(pennies)

    remaining = pennies - take
    display_game_score(take, remaining)

    other_player = togglePlayer(turn)
    return play_game(remaining, other_player)





def get_move_from_human(n):
    print "HUMAN'S TURN"

    print 'There are ' + str(n) + ' coins remaining'
    humanChoice = input('Please pick a number between 1 - 5')

    while humanChoice < 0 or humanChoice > 5:
        print "That is not a valid entry"
        humanChoice = input('Please pick a number between 1 - 5')

    return humanChoice


def get_move_from_computer(n):
    print "COMPUTER'S TURN"



    return 1


main()
