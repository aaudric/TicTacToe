# Creating the board with the variable tictactoe.
tictactoe = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]

# Creating the function print_grid to create a new line
# for each row on tictactoe.
def print_grid (right_on):
    print()
    for row in right_on:
        print(row)


def get_coord(s):
    n = s - 1
    col = n % 3
    row = n // 3
    return row,col

# Check for a winner.
def check_winner(tictactoe):
    # Check rows
    for row in tictactoe:
        if row.count('X') == 3:
            return 'X'
        elif row.count('O') == 3:
            return 'O'

    # Check columns
    for i in range(3):
        if tictactoe[0][i] == tictactoe[1][i] == tictactoe[2][i] and tictactoe[0][i] != '':
            return tictactoe[0][i]

    # Check diagonals
    if tictactoe[0][0] == tictactoe[1][1] == tictactoe[2][2] and tictactoe[0][0] != '':
        return tictactoe[0][0]
    elif tictactoe[0][2] == tictactoe[1][1] == tictactoe[2][0] and tictactoe[0][2] != '':
        return tictactoe[0][2]

    # No winner yet
    return None

# Check to see if tile is taken
def mark_cell(tictactoe, row, col, player):
    if isinstance(tictactoe[row][col], int):
        tictactoe[row][col] = player
        return True
    else:
        print("Case déja remplie.")
        return False

# Prints out the board, and then a line below it.
print_grid(tictactoe)   
print()

player = 'X'
# While loop to get what players turn it its.
while True:
    # While loop to get what tile player wants to play on.
    while True:
        location = input(f"[player {player}] Entrez la case où vous voulez jouer ")
        if not location.isdigit():
            print("Entrez un nombre.")
            # else jump into this long winded coordinate code.
            # this could be continue as well.
        else:
            turn1 = int(location)

            if turn1 < 1 or turn1 > 9:
                print("Entrez un nombre entre 1 et 9")
            else:
                row, col = get_coord(turn1)
                #tictactoe[row][col] = player

                check_tile = mark_cell(tictactoe, row, col, player)
                if check_tile:
                    # print out board with new tile marked.
                    print_grid(tictactoe)
                    print()

                    if player == 'X':
                        player = 'O'
                    else:
                        player = 'X'

                    winner = check_winner(tictactoe)
                    if winner:
                        print(f'{winner} a gagné !')
                        break

                    else:
                        print('Pas de vainqueur pour le moment.')
                        break

    if winner:
        break

            
            

                    
            
