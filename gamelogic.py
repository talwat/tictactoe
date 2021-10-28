def game_logic(state, button_pressed):
    global backround
    backround = ""
    global symbols
    symbols = ("x", "o")
    global cells
    cells = [
        [symbols[1], backround, backround], 
        [backround, backround, backround], 
        [backround, backround, backround]
    ]
    turn = False

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

def convert(input):
    temp = 0
    temp2 = 0
    for i in range(input):
        temp = temp + 1
        if temp > 2:
            temp2 = temp2 + 1
            temp = 0
    finalOutput = (temp2, temp)
    return finalOutput