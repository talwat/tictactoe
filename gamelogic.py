backround = ""
symbols = ("x", "o")
cells = [
    [backround, backround, backround], 
    [backround, backround, backround], 
    [backround, backround, backround]
]
turn = False

def cellChange(turn, button_pressed):
    index = [(int)(button_pressed[0]), (int)(button_pressed[1])]
    if(turn):
        cells[index[0]][index[1]] = symbols[1]
    else:
        cells[index[0]][index[1]] = symbols[0]

def turnChange():
    global turn
    if turn:
        turn = False
    else:
        turn = True

def checkCells():
    for symbol in symbols:
        for x in cells:
            if x[0] == symbol and x[1] == symbol and x[2] == symbol:
                return symbol + ".True"
        for x in range(len(cells)):
            if cells[0][x] == symbol and cells[1][x] == symbol and cells[2][x] == symbol:
                return symbol + ".True"

        if cells[0][0] == symbol and cells[1][1] == symbol and cells[2][2] == symbol:
            return symbol + ".True"
        elif cells[2][0] == symbol and cells[1][1] == symbol and cells[0][2] == symbol:
            return symbol + ".True"
    return "false"

def start():
    global cells
    cells = [
        [backround, backround, backround], 
        [backround, backround, backround], 
        [backround, backround, backround]
    ]
    global turn
    turn = False