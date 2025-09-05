
# Ігрове поле
import random
from colorama import Fore

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

turn = 0
victory = False


vsAI = int(input("Грати прот комп'ютера 0 - ні 1 - так: "))


while True:

    # Перевірка рядків
    for row in board:
        if row.count("X") == len(row):
            victory = "X"
        if row.count("O") == len(row):
            victory = "O"

    # Перевірка стовпців
    rotate_board = [row for row in zip(*board)]

    for row in rotate_board:
        if row.count("X") == len(row):
            victory = "X"
        if row.count("O") == len(row):
            victory = "O"

    # Перевірка діагоналей
    diagonal1 = [board[i][i] for i in range(len(board))]
    diagonal2 = [board[i][len(board)-1-i] for i in range(len(board))]

    if diagonal1.count("X") == len(diagonal1):
        victory = "X"

    if diagonal2.count("X") == len(diagonal2):
        victory = "X"

    if diagonal1.count("O") == len(diagonal1):
        victory = "O"

    if diagonal2.count("O") == len(diagonal2):
        victory = "O"



    # Додавання кольору
    if victory:
        for i, row in enumerate(board):
            for j, el in enumerate(row):
                if el == victory:
                    board[i][j] = Fore.GREEN + el + Fore.RESET
                

    # Вивід поля
    line = "   ---------"
    print("   0  1  2  ")
    print(line)

    y = 0
    for row in board:
        print(str(y)+" |", end=" ")
        for el in row:
            print(el + "|", end=" ")
        print()
        print(line)
        y += 1

    if victory:
        print(f"{victory} переміг")
        break
    elif turn == len(board)*len(board):
        print(f"Нечия")
        break

    # Хід гравця
    player = "X" if turn % 2 else "O"
    
    if vsAI and player == "O":
        
        # Доповнення рядка O
        x = -1
        y = -1
        for i, row in enumerate(board):
            if row.count("O") == len(row)-1:
                try:
                    j = row.index(" ")
                    x = i
                    y = j
                    break
                except:
                    pass
                
        if x == -1 and y == -1:
            x = random.randint(0, len(board)-1)
            y = random.randint(0, len(board)-1)
    else:
        x = int(input("Введіть координату X: "))
        y = int(input("Введіть координату Y: "))

    if board[x][y] != " ":
        print("Клітинка зайнята")
        continue

    

    board[x][y] = player

    turn += 1
