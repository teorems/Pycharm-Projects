cells = [" " for x in range(9)]

coordinates = {(1, 1): cells[6], (2, 1): cells[7], (3, 1): cells[8], (1, 2): cells[3],
               (2, 2): cells[4], (3, 2): cells[5], (1, 3): cells[0], (2, 3): cells[1],
               (3, 3): cells[2]}


def verify():
    global coordinates

    row1 = [coordinates.get((1, 1)), coordinates.get((2, 1)), coordinates.get((3, 1))]
    row2 = [coordinates.get((1, 2)), coordinates.get((2, 2)), coordinates.get((3, 2))]
    row3 = [coordinates.get((1, 3)), coordinates.get((2, 3)), coordinates.get((3, 3))]
    col1 = [coordinates.get((1, 1)), coordinates.get((1, 2)), coordinates.get((1, 3))]
    col2 = [coordinates.get((2, 1)), coordinates.get((2, 2)), coordinates.get((2, 3))]
    col3 = [coordinates.get((3, 1)), coordinates.get((3, 2)), coordinates.get((3, 3))]
    diag1 = [coordinates.get((1, 1)), coordinates.get((2, 2)), coordinates.get((3, 3))]
    diag2 = [coordinates.get((1, 3)), coordinates.get((2, 2)), coordinates.get((3, 1))]
    tot_lines = [row1, row2, row3, col1, col2, col3, diag1, diag2]

    def check(line):
        if "X" in line:
            return line[0] == line[1] == line[2]
        elif "O" in line:
            return line[0] == line[1] == line[2]
        else:
            return False

    for line in tot_lines:
        if check(line):
            if "X" in line:
                print("X wins")
                return True
            elif "O" in line:
                print("O wins")
                return True
    count = 0
    for c, v in coordinates.items():
        if (" " or "_") in v:
                count += 1
    if count == 0:
        print("Draw")
        return True


while True:
    print("---------")
    print("|", coordinates.get((1, 3)), coordinates.get((2, 3)), coordinates.get((3, 3)), "|")
    print("|", coordinates.get((1, 2)), coordinates.get((2, 2)), coordinates.get((3, 2)), "|")
    print("|", coordinates.get((1, 1)), coordinates.get((2, 1)), coordinates.get((3, 1)), "|")
    print("---------")
    if verify():
        break
    move = input("Enter the coordinates:")
    if not move.replace(" ", "").isdigit():
        print("You should enter numbers!")
        continue
    if (int(move[0]) or int(move[2])) > 3:
        print("Coordinates should be from 1 to 3!")
        continue
    move = tuple(int(x) for x in move.split())
    if move in coordinates:
        if coordinates[move] == "_" or coordinates[move] == " ":
            coordinates[move] = "X"
        elif coordinates[move] == "X" or coordinates[move] == "O":
            print("This cell is occupied! Choose another one!")
            continue
    print("---------")
    print("|", coordinates.get((1, 3)), coordinates.get((2, 3)), coordinates.get((3, 3)), "|")
    print("|", coordinates.get((1, 2)), coordinates.get((2, 2)), coordinates.get((3, 2)), "|")
    print("|", coordinates.get((1, 1)), coordinates.get((2, 1)), coordinates.get((3, 1)), "|")
    print("---------")
    if verify():
        break
    while True:
        move = input("Enter the coordinates:")
        if not move.replace(" ", "").isdigit():
            print("You should enter numbers!")
            continue
        if (int(move[0]) or int(move[2])) > 3:
            print("Coordinates should be from 1 to 3!")
            continue
        move = tuple(int(x) for x in move.split())
        if move in coordinates:
            if coordinates[move] == "_" or coordinates[move] == " ":
                coordinates[move] = "O"
                break
            elif coordinates[move] == "X" or coordinates[move] == "O":
                print("This cell is occupied! Choose another one!")
                continue
