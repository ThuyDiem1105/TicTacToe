from tkinter import *

#Tạo cửa sổ game
root = Tk()
root.geometry("380x550")
root.title("TIC TAC TOE")

root.resizable(0,0) #Giúp cửa sổ game không thay đổi kích thước

#Tạo các frame trên cửa sổ game
frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1 , text="Tic Tac Toe" , font=("Arial" , 26) , bg="orange" , width=16 )
titleLabel.grid(row=0 , column=0)

optionFrame = Frame(root , bg="grey")
optionFrame.pack()

frame2 = Frame(root , bg="yellow")
frame2.pack()

board = { 1:" " , 2:" " , 3:" ",
          4:" " , 5:" " , 6:" ",
          7:" " , 8:" " , 9:" " }

turn = "x"
game_end = False
mode = "singlePlayer" #Chế độ mặc định khi vào game là người với máy

#Hàm chọn chế độ chơi
def changeModeToSinglePlayer(): 
    global mode 
    mode = "singlePlayer"
    singlePlayerButton["bg"] = "lightgreen"
    multiPlayerButton["bg"] = "lightgrey"

def changeModeToMultiplayer():
    global mode 
    mode = "multiPlayer"
    multiPlayerButton["bg"] = "lightgreen"
    singlePlayerButton["bg"] = "lightgrey"
singlePlayerButton = Button(optionFrame , text="SinglePlayer" , width=13 , height=1 , font=("Arial" , 15) , 
                            bg="lightgrey" , relief=RAISED , borderwidth=5 , command=changeModeToSinglePlayer)
singlePlayerButton.grid(row=0 , column=0 , columnspan=1 , sticky=NW) #sticky: Căn chỉnh nút trong ô lưới (NW - góc trên bên trái)

multiPlayerButton = Button(optionFrame , text="Multiplayer" , width=13 , height=1 , font=("Arial" , 15) , bg="lightgrey" , relief=RAISED , borderwidth=5 , command=changeModeToMultiplayer )
multiPlayerButton.grid(row=0 , column=1 , columnspan=1 , sticky=NW) #sticky: Căn chỉnh nút trong ô lưới (NW - góc trên bên trái)

#Cập nhật giao diện các nút trên bảng trò chơi
def updateBoard():
    for key in board.keys():
        buttons[key-1]["text"] = board[key] 

#Hàm kiểm tra thắng thua
def checkForWin(player):
    # Hàng
    if board[1] == board[2] and board[2] == board[3] and board[3] == player:
        return True
    
    elif board[4] == board[5] and board[5] == board[6] and board[6] == player:
        return True
    
    elif board[7] == board[8] and board[8] == board[9] and board[9] == player:
        return True

    # Cột
    elif board[1] == board[4] and board[4] == board[7] and board[7] == player:
        return True
    
    elif board[2] == board[5] and board[5] == board[8] and board[8] == player:
        return True
    
    elif board[3] == board[6] and board[6] == board[9] and board[9] == player:
        return True
    
    # Đường chéo
    elif board[1] == board[5] and board[5] == board[9] and board[9] == player:
        return True
    
    elif board[3] == board[5] and board[5] == board[7] and board[7] == player:
        return True
    

    return False

#Hàm kiểm tra hòa
def checkForDraw():
    for i in board.keys():
        if board[i] == " ":
            return False
    
    return True

#Hàm xóa tất cả và restart
def restartGame():
    global game_end #Đặt lại biến game_end bên ngoài hàm = cách sử dụng global
    game_end = False
    for button in buttons:
        button["text"] = " " #Xóa văn bản game hiện tại

    for i in board.keys():
        board[i] = " " #Xóa giá trị game hiện tại
    #Cập nhật tiêu đề trò chơi trên giao diện
    titleLabel = Label(frame1 , text="Tic Tac Toe" , font=("Arial" , 30) , bg="orange" , width=15 )
    titleLabel.grid(row=0 , column=0)

import random
#Máy tính chọn ngẫu nhiên 1 vị trống trên bảng để điền
def playComputer():
    # Tạo một danh sách chứa tất cả các vị trí trống trên bảng
    empty_positions = [key for key, value in board.items() if value == " "]
    
    # Chọn một vị trí ngẫu nhiên từ danh sách các vị trí trống
    selected_position = random.choice(empty_positions)
    
    # Đặt "o" vào vị trí đã chọn
    board[selected_position] = "o"

# Function to play
def play(event):
    global turn,game_end
    if game_end:
        return
    
    button = event.widget #Gán button là nút mà người dùng đã click vào
    buttonText = str(button) #Chuyển nút thành chuỗi mà buttonText[-1] là vị trí của nút đó
    clicked = buttonText[-1] #Gán click là vị trí nút mà người chơi đã click vào
    if clicked == "n" : #n là mã định danh của ô đầu tiên
        clicked = 1
    else :
        clicked = int(clicked)
    
    if button["text"] == " ":
        if turn == "x" :
            board[clicked] = turn
            if checkForWin(turn):
                winningLabel = Label(frame1 , text=f"{turn} wins the game", bg="orange", font=("Arial" , 26),width=16 )
                winningLabel.grid(row = 0 , column=0 , columnspan=3)
                game_end = True

            turn = "o"

            updateBoard()

            if mode == "singlePlayer":

                playComputer()

                if checkForWin(turn):
                    winningLabel = Label(frame1 , text=f"{turn} wins the game", bg="orange", font=("Arial" , 26),width=16 )
                    winningLabel.grid(row = 0 , column=0 , columnspan=3)
                    game_end = True

                turn = "x"

                updateBoard()

           
            
        else:
            board[clicked] = turn
            updateBoard()
            if checkForWin(turn):
                winningLabel = Label(frame1 , text=f"{turn} wins the game" , bg="orange", font=("Arial" , 26),width=16)
                winningLabel.grid(row = 0 , column=0 , columnspan=3)
                game_end = True
            turn = "x"

        
        if checkForDraw():
            drawLabel = Label(frame1 , text=f"Game Draw" , bg="orange", font=("Arial" , 26), width = 16)
            drawLabel.grid(row = 0 , column=0 , columnspan=3)

# Tic Tac Toe Board 

#  First row 

button1 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30) , bg="yellow" , relief=RAISED , borderwidth=5)
button1.grid(row = 0 , column=0)
button1.bind("<Button-1>" , play)

button2 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="yellow" , relief=RAISED , borderwidth=5 )
button2.grid(row = 0 , column=1)
button2.bind("<Button-1>" , play)

button3 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="yellow" , relief=RAISED , borderwidth=5 )
button3.grid(row = 0 , column=2)
button3.bind("<Button-1>" , play)

#  second row 

button4 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="yellow" , relief=RAISED , borderwidth=5 )
button4.grid(row = 1 , column=0)
button4.bind("<Button-1>" , play)

button5 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="yellow" , relief=RAISED , borderwidth=5 )
button5.grid(row = 1 , column=1)
button5.bind("<Button-1>" , play)

button6 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="yellow" , relief=RAISED , borderwidth=5 )
button6.grid(row = 1 , column=2)
button6.bind("<Button-1>" , play)

#  third row 

button7 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30) , bg="yellow" , relief=RAISED , borderwidth=5)
button7.grid(row = 2 , column=0)
button7.bind("<Button-1>" , play)

button8 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="yellow" , relief=RAISED , borderwidth=5 )
button8.grid(row = 2 , column=1)
button8.bind("<Button-1>" , play)

button9 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30) , bg="yellow" , relief=RAISED , borderwidth=5)
button9.grid(row = 2 , column=2)
button9.bind("<Button-1>" , play)

restartButton = Button(frame2 , text="Restart Game" , width=19 , height=1 , font=("Arial" , 20) , bg="Green" , relief=RAISED , borderwidth=5 , command=restartGame )
restartButton.grid(row=4 , column=0 , columnspan=3)

buttons = [button1 , button2 , button3 , button4 , button5 , button6 , button7 , button8, button9]

root.mainloop()