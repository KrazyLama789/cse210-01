#Tic-Tac-Toe rules.

#1. The game is played on a 3x3 grid.
#2. Player one uses x's. Player two uses o's.
#3. Players take turns putting their marks in empty squares.
#4. First to 3 marks in a row (vertical, horizontal, or diagonal) wins.
#5. If the game board is full, and no one won, it't a tie.

def main():
    turncount = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    gameboard = (f"{one}|{two}|{three} \n-+-+- \n{four}|{five}|{six} \n-+-+- \n{seven}|{eight}|{nine} \n")
    print(gameboard)
    while turncount <= 9:
        turncount += 1
    print("turn 9")
    
main()