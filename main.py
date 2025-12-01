# Librairies
import random
import time

# Variables 
grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Functions

# Empties the console
def clear():
    for i in range(60):
        print("")
        
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

def displaygrid_cli():
    clear()
    global grid
    print("-------------")
    for i in range(0, len(grid), 3):
        line = "| "
        for j in range(i, i+3):
            match grid[j]:
                case "X":
                    line += " X "
                case "O" :
                    line += " O "
                case _:
                    line += "   "
        line += " |"
        print(line)
    print("-------------")

def replay():
    displaygrid_cli()
    print("")
    match input("Vous voulez rejouer (Oui/Non) : ").lower():
        case "oui":
            global grid
            grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            return True
        case "non":
            return False
        case _:
            replay()

def placesymbol(value):

    global grid

    if value == "player1":
        print("")
        place = input("Joueur 1, où voulez-vous placer votre symbole (1-9) : ")
        match place:
            case "1":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case "2":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case "3":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case "4":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case "5":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case "6":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case "7":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case "8":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case "9":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case _:
                print("")
                print("Saisie incorrecte")
                time.sleep(3)
                player_solo_play()
    elif value == "player2":
        print("")
        place = input("Joueur 2, où voulez-vous placer votre symbole (1-9) : ")
        match place:
            case "1":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case "2":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case "3":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case "4":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case "5":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case "6":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case "7":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case "8":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case "9":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case _:
                print("")
                print("Saisie incorrecte")
                time.sleep(3)
                player_solo_play()
    else:
        grid[int(value)] = "O"

def ordinateur(board, signe):

    print("")
    print("L'ordinateur réfléchi...")
    time.sleep(2)
    value = random.randint(0, 8)
    while board[value] != 0:
        value = random.randint(0, 8)

    if 0 <= value <= 8:
        return value
    else:
        return False
    
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

def checkvictory(grid, symbol, player):
    for combo in win_conditions:
        if all(grid[i] == symbol for i in combo):
            print(f"{player} a gagné !")
            return True
    return False

def player_solo_play():

    global grid

    displaygrid_cli()
    placesymbol("player1")

    if checkvictory(grid, "X", "Joueur 1"):
        return replay()

    if not(0 in grid):
        print("")
        print("Égalité !")
        return replay()

    displaygrid_cli()
    placesymbol(ordinateur(grid, "O"))

    if checkvictory(grid, "O", "L'ordinateur"):
        return replay()

    if 0 in grid:
        return True
    else:
        print("")
        print("Égalité !")
        return replay()

# Main program

if player_selection() == 1:
    while True:
        if player_solo_play():
            continue
        else:
            break

else:
    while True:
        print("")