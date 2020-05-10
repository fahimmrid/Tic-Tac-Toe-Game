# Fahim's colorful bulletproof Tic Tac toe Game with all cases (as multiple problems and bugs can arise) considered and fixed

section = ["\033[95m0", "\033[94m1", "\033[93m2",
           "\033[92m3", "\033[91m4", "\033[96m5",
           "\033[36m6", "\033[95m7", "\033[95m8"]  # color indexes

game_done = True  # the key "flag" to indicate when game is over and a player wins
max_turn = 9 #ultimately look this off as it was pointless


# only function not used, however a key can be  used to display the rules if wanted
def rules():
    print ("Each player needs to match their symbol three times by row, colum or diagonally")
    print ("You cannot Override a position that has been taken by your opponents")
    print ("If no 3 mathces is by by the time board is full.. Tie will be concluded ")

def play_grid():  # setting up the grids for game
    print ("==|| Welcome to <Fahim> Tic Tac Toe game ||==")
    print (section[0] + "|" + section[1] + "|" + section[2])
    print (section[3] + "|" + section[4] + "|" + section[5])
    print (section[6] + "|" + section[7] + "|" + section[8])


def main_action():  # main function where the game excution is called

    play_grid ()

    while (game_done):
        start_game ()


def winner(player):  # the various ways a player can win - row/coloums/diagnal matches or TIES
    global game_done

    if (section[0] == section[1] == section[2]) or (section[3] == section[4] == section[5]) or (
            section[6] == section[7] == section[8]):
        print ("== You win Player " + player + " (by row matches) ==")
        game_done = False

    elif (section[0] == section[3] == section[6]) or (section[1] == section[4] == section[7]) or (
            section[2] == section[5] == section[8]):
        print ("== You win Player " + player + " (by column matches) ==")
        game_done = False

    elif (section[0] == section[4] == section[8]) or (section[2] == section[4] == section[6]):
        print ("== You win Player " + player + " (by diagonal matches) ==")
        game_done = False

    elif ((section[0] == "X" or section[0] == "O") and (section[1] == "X" or section[1] == "O") and (section[2] == "X" or section[2] == "O") and
        (section[3] == "X" or section[3] == "O") and (section[4] == "X" or section[4] == "O") and (section[5] == "X" or section[5] == "O") and
        (section[6] == "X" or section[6] == "O") and (section[7] == "X" or section[7] == "O") and (section[8] == "X" or section[8] == "O")):
        print("== Game has been TIED!! ==")    #I could potentially use a much simpler hack to crack the tie portion (which I left till end)
        game_done = False                      #I considered the corner case when a player can will on the very last spot on the game


def start_game():  # where the game is started and executed
    turn_switch = True

    while game_done:
        symbol = input ("\033[91mSelect a number (0-8) to place your move : ")
        while symbol not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            # so if someone presses a letter and then presses a letter again by mistake..
            # handle multiple (non-int) isses repeatdly unlike a conditional statement
            symbol = input ("Error: Select only from 0-8 : ")
        try:
            symbol = int (symbol)
        except TypeError:
            print ("Could not convert data to an integer.")

        # im using a flag to rotate between players (since its only 2) and covering any error cases that can happen during game
        if turn_switch:
            if section[symbol] == "O" or section[symbol] == "X":
                print ("Error: Select position that is Not taken! ")
            else:
                section[symbol] = "X"
                play_grid ()
                winner ("X")
                turn_switch = False

        else:
            if section[symbol] == "X" or section[symbol] == "O":
                print ("Error: Select position that is Not taken! ")
            else:
                section[symbol] = "O"
                play_grid ()
                winner ("O")
                turn_switch = True

main_action ()
