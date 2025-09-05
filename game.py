

# Ігрове поле
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

turn = 0
while True:
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

    # Хід гравця
    x = int(input("Введіть координату X: "))
    y = int(input("Введіть координату Y: "))

    if board[x][y] != " ":
        print("Клітинка зайнята")
        continue

    player = "X" if turn % 2 else "O"

    board[x][y] = player

    turn += 1
