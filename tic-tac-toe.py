# The program must have a comment with assignment (make a funcitoning Tic-Tac-Toe game) and author names (Mary Goff).
# The program must have at least one if/then block.
# The program must have at least one while loop.
# The program must have more than one function.
# The program must have a function called main.

# A function with a refreshable game board.
def gameboard(numberlist):
    one, two, three, four, five, six, seven, eight, nine = numberlist
    gameboard = (
        f"\n{one}|{two}|{three} \n-+-+- \n{four}|{five}|{six} \n-+-+- \n{seven}|{eight}|{nine} \n")
    return gameboard
# A function to evaluate win conditions, and return the result.

def winconditions(numberlist, turn):
    win = False
    if numberlist[0] == turn and numberlist[1] == turn and numberlist[2] == turn:
        win = True
    elif numberlist[3] == turn and numberlist[4] == turn and numberlist[5] == turn:
        win = True
    elif numberlist[6] == turn and numberlist[7] == turn and numberlist[8] == turn:
        win = True
    elif numberlist[0] == turn and numberlist[3] == turn and numberlist[6] == turn:
        win = True
    elif numberlist[1] == turn and numberlist[4] == turn and numberlist[7] == turn:
        win = True
    elif numberlist[2] == turn and numberlist[5] == turn and numberlist[8] == turn:
        win = True
    elif numberlist[0] == turn and numberlist[4] == turn and numberlist[8] == turn:
        win = True
    elif numberlist[6] == turn and numberlist[4] == turn and numberlist[2] == turn:
        win = True
    else:
        return
    return win
# A funciton to play the game of Tic-Tak-Toe

def main():
    turncount = 0
    numberlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("\nWelcome to Tic-Tac-Toe")
    while turncount < 9:
        print(gameboard(numberlist))
        turn = ""
        if turncount % 2 == 0:
            turn = "X"
            turninput = int(input("It's X's turn. Choose a number(1-9):\n"))
            if type(numberlist[turninput-1]) == int:
                numberlist[turninput-1] = "X"
                if winconditions(numberlist, turn) == True:
                    print(gameboard(numberlist))
                    return print(f"{turn} Wins! Thanks for playing!")
            else:
                print("\nThat space is already taken. Try again.")
                turncount -= 1
        else:
            turn = "O"
            turninput = int(input("It's O's turn. Choose a number(1-9):\n"))
            if type(numberlist[turninput-1]) == int:
                numberlist[turninput-1] = "O"
                if winconditions(numberlist, turn) == True:
                    return print(f"{turn} Wins! Thanks for playing!")
            else:
                print("\nThat space is already taken. Try again.")
                turncount -= 1
        turncount += 1
main()