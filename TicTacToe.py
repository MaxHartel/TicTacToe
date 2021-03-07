import time

TL = 0
TM = 0
TR = 0
ML = 0
MM = 0
MR = 0
BL = 0
BM = 0
BR = 0
TIE = 0
TurnCounter = 0
board = ["__","__","__","__","__","__","  ","  ","  "]

print("lets play tic tac toe!")
print("I'll be X's you be O's")
print("Type these phrases to place your O's:\n 'TR' = Top Right\n 'TM' = Top Middle\n 'TL' = Top Left\n 'MR' = Middle Right\n 'MM' = Middle Middle\n 'ML' = Middle Left\n 'BR' = Bottom Right \n 'BM' = Bottom Middle\n 'BL' = Bottom Left")
print("\n I'll take the first move \n\n")
print(" Thinking... \n")
time.sleep(0.5)
            
def tableset():
    print("\n"+board[0]+"|"+board[1]+"|"+board[2]+"\n"+board[3]+"|"+board[4]+"|"+board[5]+"\n"+board[6]+"|"+board[7]+ "|"+ board[8])

def TicTacToe(x):
    global TL
    global TM
    global TR
    global ML
    global MM
    global MR
    global BL
    global BM
    global BR
    global TurnCounter
    global TIE
    if x == "TL" and board[0] == "__":
        board[0] = "O_"
        TurnCounter += 1
        TL += 1
        tableset()
    if x == "TM" and board[1] == "__":
        board[1] = "O_"
        TurnCounter += 1
        TM += 1
        tableset()
    if x == "TR"and board[2] == "__":
        board[2] = "O_"
        TurnCounter += 1
        TR += 1
        tableset()
    if x == "ML" and board[3] == "__":
        board[3] = "O_"
        TurnCounter += 1
        ML += 1
        tableset()
    if x == "MM" and board[4] == "__":
        board[4] = "O_"
        TurnCounter += 1
        MM += 1
        tableset()
    if x == "MR" and board[5] == "__":
        board[5] = "O_"
        TurnCounter += 1
        MR += 1
        tableset()
    if x == "BM" and board[7] == "  ":
        board[7] = "O "
        TurnCounter += 1
        BM += 1
        tableset()
    if x == "BR" and board[8] == "  ":
        board[8] = "O "
        TurnCounter += 1
        BR += 1
        tableset()
    if TurnCounter == 1:
        if board[7] != "O " and board[8] != "0 ":
            print("\n\n Thinking... \n")
            time.sleep(1)
            BR += 2
            board[8] = "X "
            tableset()
        if board[7] == "O " or board[8] == "0_":
            print("\n\n Thinking... \n")
            time.sleep(2)
            TL += 2
            board[0] = "X_"
            tableset()
    if TurnCounter == 2:
        if board[7] != "O " and board[8] == "X ":
            print("\n\n Thinking... \n")
            time.sleep(1)
            BM += 2
            board[7] = "X "
            tableset()
        elif board[3] != "O_" and board[0] == "X_":
            print("\n\n Thinking... \n")
            time.sleep(1)
            ML += 2
            board[3] = "X_"
            tableset()
        elif board[4] == "__":
            print("\n\n Thinking... \n")
            time.sleep(1)
            MM += 2
            board[4] = "X_"
            tableset()
        elif board[4] == "O_" and board[7] == "O ":
            print("\n\n Thinking... \n")
            time.sleep(1)
            TM += 2
            board[1] = "X_"
            tableset()
        elif board[4] == "O_" and board[3] == "O_":
            print("\n\n Thinking... \n")
            time.sleep(1)
            ML += 2
            board[5] = "X_"
            tableset()
        elif board[7] == "O " and board[8] == "X ":
            print("\n\n Thinking... \n")
            time.sleep(1)
            TR += 2
            board[2] = "X_"
            tableset()
        elif board[3] == "O_" and board[0] == "X_":
            print("\n\n Thinking... \n")
            time.sleep(1)
            BR += 2
            board[8] = "X "
            tableset()
    if TurnCounter == 3:
        if board[4] == "O_" and board[3] == "O_":
            print("\n\n Thinking... \n")
            time.sleep(1)
            ML += 2
            board[5] = "X_"
            tableset()
        elif board[4] == "O_" and board[5] == "O_" and board[0] == "__":
            print("\n\n Thinking... \n")
            time.sleep(1)
            TL += 2
            board[0] = "X_"
            tableset()
        elif board[8] == "X " and board[4] == "X_":
            if board[0] == "__":
                print("\n\n Thinking... \n")
                time.sleep(1)
                TL += 2
                board[0] = "X_"
                tableset()
            elif board[2] == "__":
                print("\n\n Thinking... \n")
                time.sleep(1)
                TR += 2
                board[2] = "X_"
                tableset()
            else:
                print("\n\n Thinking... \n")
                time.sleep(1)
                for i in range(len(board)):
                        if board[i] == "__" or board[i] == "  ":
                            if i == 3:
                                ML += 2
                            if i == 5:
                                MR += 2
                                board[i] =  "X_"
                                tableset()
                                break            
        if board[0] == "X_" and board[4] == "X_":
            if board[8] == "  ":
                print("\n\n Thinking... \n")
                time.sleep(1)
                BR += 2
                board[8] = "X "
                tableset()
            else:
                print("\n\n Thinking... \n")
                time.sleep(1)
                TR += 2
                board[2] = "X_"
                tableset()
        elif board[4] != "O_" and board[3] != "O_":
            print("\n\n Thinking... \n")
            time.sleep(1)
            for s in range(9):
                if board[s] == "__" or board[s] == "  ":
                    if s == 0:
                        TL += 2
                    if s == 2:
                        TR += 2
                    board[s] =  "X_"
                    tableset()
                    break
    if TurnCounter == 4:
        print("\n\n Thinking... \n")
        time.sleep(1)
        for u in range(len(board)):
                if board[u] == "__" or board[u] == "  ":
                    if u == 3:
                        ML += 2
                    if u == 5:
                        MR += 2
                    board[u] =  "X_"
                    tableset()
                    break
    if TurnCounter == 4 and ML + MM + MR != 3 and TR + MR + BR != 6 and TL + ML + BL != 6:
        print("Its a Tie, Try Again?")
        TIE += 1

    
def WinChecker():
    global TL
    global TM
    global TR
    global ML
    global MM
    global MR
    global BL
    global BM
    global BR
    global TIE
    board[6] = "X "
    tableset()
    BL += 2
    while True:
        if TL + TM + TR == 6 or ML + MM + MR == 6 or BL + BM + BR == 6 or TL + ML + BL == 6 or TM + MM + BR == 6 or TR + MR + BR == 6 or TL + MM + BR == 6 or TR + MM + BL == 6:
            print("You Lost :( ")
            break
        elif TIE > 0:
            break
        elif ML + MM + MR == 3:
            print("You Win :)")
            break
        else:
            x = input("")
            TicTacToe(x)
        


WinChecker()

while True:
    d = input("Would You Like To Play Again? (Y/N)")
    if d == "Y":
        TL = 0
        TM = 0
        TR = 0
        ML = 0
        MM = 0
        MR = 0
        BL = 0
        BM = 0
        BR = 0
        TIE = 0
        TurnCounter = 0
        for p in range(len(board)):
            if p < 6:
                board[p] = "__"
            if p >= 6:
                board[p] = "  "
        WinChecker()
    if d == "N":
        break




        
