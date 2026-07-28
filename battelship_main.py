"""Console Battleship Game.

Two-player terminal implementation.
"""

BOARD_SIZE = 10
SHIP_SIZES = [5,4,3,2,2]

size = BOARD_SIZE
ship_size = SHIP_SIZES

p1_ships = []
p2_ships = []

def create_board():
    board = []
    for i in range(size) :
        row = []
        for j in range(size) :
            row.append("~")
        board.append(row)
    return board

def print_board(board):
    print(" ", end=" ")
    for i in range(size) : 
        print(i+1, end=" ")
    print("\n" , end="")
    for i in range(size):
        print(i + 1, end=" ")
        for j in range(size):
            print(board[i][j], end=" ")
        print()

def check_ship(board,row,col,ship_size,direction):
    
    for i in range(ship_size):

        if direction == "H":
            r = row
            c = col + i
        else:
            r = row + i
            c = col
        if r < 0 or r >= size or c < 0 or c >= size :
            return False

        for radif in range(r-1,r+2):
            for soton in range(c-1,c+2):
                if 0 <= radif < size and 0 <= soton < size :
                    if board[radif][soton] != "~" :
                        return False
    return True
    
def place_ship(board, ship_size , ship_list):

    while True:
        print_board(board)
        while True :
            row = int(input("start row : ")) - 1
            col = int(input("start col : ")) - 1
            direction = input("direction (H (Horizontal) / V (Vertical)): ").upper()
            if row < 0 or row >= size or col < 0 or col >= size or (direction != "H" and direction != "V"):
                print("ّInvalid row, column, or direction.")
            else :
                break

        if check_ship(board, row, col, ship_size,direction) == True :
            place_ship_list = []
            if direction == "H":

                for i in range(ship_size):
                    board[row][col] = "S"
                    place_ship_list.append([row,col])
                    col = col + 1
            else:
                for i in range(ship_size):
                    board[row][col] = "S"
                    place_ship_list.append([row,col])
                    row = row + 1
            ship_list.append(place_ship_list)
            break

        else:
            print("Invalid ship placement.")

def setup_board_and_player(name , ship_list) :
    print(f"Hello {name} , \n welcome to battleship game")
    board = create_board()

    for l in ship_size :
        print(f"\n put your ship in board \n ship size is {l} ")
        place_ship(board, l , ship_list)
    print_board(board)
    return board

def check_and_sink_ships(board, ship_list):
    for ship in ship_list:
        sink = True
        for place in ship:
            row = place[0]
            col = place[1]

            if board[row][col] != "X":
                sink = False

        if sink:
            for place in ship:
                row = place[0]
                col = place[1]

                for i in range(row-1, row+2):
                    for j in range(col-1, col+2):

                        if 0 <= i < size and 0 <= j < size:
                            if board[i][j] == "~":
                                board[i][j] = "O"
            print("Enemy ship sunk!")


def shoot(board , ship_list ) :
    while True :
        row = int(input("enter one row : ")) -1
        col = int(input("enter one col : ")) -1
        if row < 0 or row >= size or col < 0 or col >= size:
            print("Invalid coordinates.")
            continue

        if board[row][col] == "X" or board[row][col] == "O":
            print("This position has already been targeted.")
            continue
        break

    if board[row][col] == "S" :
        print("wow ! , Hit!")
        board[row][col] = "X"
        check_and_sink_ships(board, ship_list)
        return True
    
    elif board[row][col] == "~" :
        print("Miss!")
        board[row][col] = "O"
        return False

def count_ships(board):

    count = 0
    for i in range(size):
        for j in range(size):

            if board[i][j] == "S":
                count = count + 1

    return count

def print_enemy_board(board):
    print(" ", end=" ")
    for i in range(size) : 
        print(i+1, end=" ")
    print("\n" , end="")
    for i in range(size):
        print(i + 1, end=" ")
        for j in range(size):
            if board[i][j] == "S" :
                print("~", end=" ")
            else:
                print(board[i][j], end=" ")
        print()


def main():
    print("Starting Battleship...")
    name1 = input("Player 1 name: ")
    name2 = input("Player 2 name: ")

    p1 = setup_board_and_player(name1 , p1_ships)
    input("your frend turn , press the enter")
    print("\n"*25)
    p2 = setup_board_and_player(name2 , p2_ships)
    input("for Starting Battleship..., press enter")
    print("\n"*25)

    while True:
        while True:
            print(f"\n {name1} shoot")
            print_enemy_board(p2)
            shoot_direction = shoot(p2 , p2_ships)
            print_enemy_board(p2) 
        
            if count_ships(p2) == 0:
                break
            
            if shoot_direction :
                print(f"{name1} Hit! shoot again")
            else:
                break

        if count_ships(p2) == 0:
            print(f"{name1} win!")
            break

        input(f" {name1}، put enter , {name2} turn")
        print("\n" * 25)

        while True:
            print(f"\n {name2} shoot")
            print_enemy_board(p1)
            shoot_direction = shoot(p1 , p1_ships)
            print_enemy_board(p1) 
            if count_ships(p1) == 0:
                break
            
            if shoot_direction:
                print(f"{name2} Hit! shoot again")
            else:
                break 

        if count_ships(p1) == 0:
            print(f"{name2} win!")
            break
    
        input(f" {name2}، put enter , {name1} turn")
        print("\n" * 25)

if __name__ == '__main__':
    main()
