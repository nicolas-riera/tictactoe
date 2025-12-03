# Librairies
import time
import random

# Variables 

grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# All the possibles patterns to win
win_conditions = [
    # Horizontal
    [0, 1, 2],  
    [3, 4, 5],  
    [6, 7, 8],  

    # Vertical
    [0, 3, 6],  
    [1, 4, 7],  
    [2, 5, 8],  

    # Diagonal
    [0, 4, 8], 
    [2, 4, 6]  
]

# "Empties" the console
def clear():
    print("\n"*60)

def reset_grid():
    global grid # necessary to edit the global variable
    grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Main menu/Game mode selection        
def player_selection():
    clear()
    print("Tic Tac Toe")
    print("")
    print("1. Un Joueur")
    print("2. Deux Joueurs")
    print("")

    selection = input("")
    if selection == "1" or selection == "2":
        return int(selection)
    else:
        player_selection()

# Displays the grid in a formated way
def displaygrid_cli():
    clear()
    print("-------------")
    for i in range(0, len(grid), 3):
        line = "|"
        for j in range(i, i+3):
            match grid[j]:
                case "X":
                    line += " X "
                case "O" :
                    line += " O "
                case _:
                    if all(k == 0 for k in grid):
                        line += f" {j+1} "
                    else:
                        line += "   "
            line += "|"
        print(line)
        print("-------------")

# Lets you start a new game or stop the program
def replay():
    print("")
    match input("Vous voulez rejouer (Oui/Non) : ").lower():
        case "oui":
            reset_grid()
            return True
        case "non":
            return False
        case _:
            replay()

# Function that manages the placement of the symbols
def placesymbol(value):

    # Symbol assignation
    if value == "player1":
        symbol = "X"
    elif value == "player2":
        symbol = "O"

    # Players block
    if value == "player1" or value == "player2":
        print("")
        place = input("Joueur 1, où voulez-vous placer votre symbole (1-9) : ")
        match place:
            case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = symbol
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    displaygrid_cli()
                    placesymbol(value)
            case _:
                print("")
                print("Saisie incorrecte")
                time.sleep(3)
                displaygrid_cli()
                placesymbol(value)

    # Bot block                
    else:
        grid[int(value)] = "O"

# Algorithm for the bot to choose a cell

# Level 2
def bot_check_two_in_line(board, signe):
    for ligne in win_conditions:
            cases = [board[i] for i in ligne]
            if cases.count(signe) == 2 and cases.count(0) == 1:
                return ligne[cases.index(0)]
    return None

# Level 3
def minimax(board, is_maximizing):
    if checkvictory(board, "O", "bot", False)[0]:
        return 1
    elif checkvictory(board, "X", "player1", False)[0]:
        return -1
    elif 0 not in board:
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] = "O"
                score = minimax(board, False)
                board[i] = 0
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] = "X"
                score = minimax(board, True)
                board[i] = 0
                best_score = min(score, best_score)
        return best_score
    
def best_move(board):
    best_score = -float('inf')
    value = None
    for i in range(9):
        if board[i] == 0:
            board[i] = "O"
            score = minimax(board, False)
            board[i] = 0
            if score > best_score:
                best_score = score
                value = i
    return value

# Base function
def ordinateur(board, signe, cli_mode, ai_difficulty):
    if cli_mode:
        print("")
        print("L'ordinateur réfléchi...")
        time.sleep(2)

    # Level 1
    if ai_difficulty == 1:
        value = random.randint(0, 8)
        while board[value] != 0:
            value = random.randint(0, 8)

    # Level 2
    elif ai_difficulty == 2:
        # win if possible
        value = bot_check_two_in_line(board, signe)
        if value is None:
            # block player
            value = bot_check_two_in_line(board, "X")
        if value is None:
            value = random.randint(0, 8)
            while board[value] != 0:
                value = random.randint(0, 8)     

    # Level 3                      
    else:
        value = best_move(board)

    if 0 <= value <= 8:
        return value
    else:
        return False

# Checks if someone has won or not
def checkvictory(grid, symbol, player, cli_mode):
    for combo in win_conditions:
        if all(grid[i] == symbol for i in combo):
            if cli_mode:
                displaygrid_cli()
                print("")
                print(f"{player} a gagné !")
                time.sleep(1)
                return True
            else:
                return True, combo
    if cli_mode:
        return False
    else:
        return False, []

# Function that manages the other functions when playing in single-player mode
def player_solo_play():

    displaygrid_cli()
    placesymbol("player1")

    if checkvictory(grid, "X", "Joueur 1", True):
        return replay()

    if not(0 in grid):
        displaygrid_cli()
        print("")
        print("Égalité !")
        return replay()

    displaygrid_cli()
    placesymbol(ordinateur(grid, "O", True, 1))

    if checkvictory(grid, "O", "L'ordinateur", True):
        return replay()

    if 0 in grid:
        return True
    else:
        displaygrid_cli()
        print("")
        print("Égalité !")
        return replay()

# Function that manages the other functions when playing in two-player mode
def player_duo_play():

    displaygrid_cli()
    placesymbol("player1")

    if checkvictory(grid, "X", "Joueur 1", True):
        return replay()

    if not(0 in grid):
        displaygrid_cli()
        print("")
        print("Égalité !")
        return replay()

    displaygrid_cli()
    placesymbol("player2")

    if checkvictory(grid, "O", "Joueur 2", True):
        return replay()

    if 0 in grid:
        return True
    else:
        displaygrid_cli()
        print("")
        print("Égalité !")
        return replay()
