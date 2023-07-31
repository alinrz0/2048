import tkinter as tk
import random

Move=True
SCORE=0
GRID_SZE=4
FONT="Arial"
FONT_SIZE = 36
BG_COLOR = "#FAF8EF"
TILE_COLORS = {
    0: "#FAF8EF",
    2: "#EEE4DA",
    4: "#EDE0C8",
    8: "#F2B179",
    16: "#F59563",
    32: "#F67C5F",
    64: "#F65E3B",
    128: "#EDCF72",
    256: "#EDCC61",
    512: "#EDC850",
    1024: "#EDC53F",
    2048: "#EDC22E",
}

numbers=[[0 for i in range(GRID_SZE)]for i in range(GRID_SZE)]
zero_list=[(i, j) for i in range(GRID_SZE) for j in range(GRID_SZE) if numbers[i][j] == 0]

root = tk.Tk()
root.maxsize(500,530)
root.minsize(500,530)
root.title("2048")

square_size = 125
canvas = tk.Canvas(root, width=530, height=530, bg=BG_COLOR)
canvas.pack()
score_text=canvas.create_text(40,15, text="Score: " +str(SCORE), font=(FONT, 10,"bold","italic"),fill="black")

def get_high_Score():
    f=open("high_score.txt")
    a=f.read()
    f.close()
    return a

HIGH_SCORE=int(get_high_Score())
high_score_text=canvas.create_text(250,15, text="high Score: " +str(HIGH_SCORE), font=(FONT, 10,"bold","italic"),fill="black")

def set_high_Score():
    with open("high_score.txt","w")as aa:
        aa.write(str(HIGH_SCORE))
        aa.close()


def restart():
    global numbers
    global SCORE
    numbers=[[0 for i in range(GRID_SZE)]for i in range(GRID_SZE)]
    SCORE=0
    global Move
    Move=True
    update()
button =tk.Button(canvas,text="play agin!",width=9,height=1,bg="#F0E68C",command=restart)
canvas.create_window(450,15,window=button)

def lose():
    for i in range(GRID_SZE):
        for j in range(GRID_SZE):
            if numbers[i][j]==0:
                return False
            if i+1<GRID_SZE and numbers[i][j]==numbers[i+1][j]:
                return False
            if i>0 and numbers[i][j]==numbers[i-1][j]:
                return False
            if j+1<GRID_SZE and numbers[i][j]==numbers[i][j+1]:
                return False
            if j>0 and numbers[i][j]==numbers[i][j-1]:
                return False
    return True



def update():
    global Move
    zero_list=[(i, j) for i in range(GRID_SZE) for j in range(GRID_SZE) if numbers[i][j] == 0]
    if zero_list and Move==True:
        grid=random.choice(zero_list)
        numbers[grid[0]][grid[1]]=2
    for i in range(GRID_SZE):
        for j in range(GRID_SZE):
            x1 = j * square_size
            y1 = i * square_size+30
            x2 = (j+1) * square_size
            y2 = (i+1) * square_size+30
            canvas.create_rectangle(x1, y1, x2, y2, outline="black",width=6,fill=TILE_COLORS[numbers[i][j]])
            text_x = (x1 + x2) / 2
            text_y = (y1 + y2) / 2
            if numbers[i][j]!=0:
                canvas.create_text(text_x, text_y, text=numbers[i][j], font=(FONT, FONT_SIZE,"bold"))
    if lose():
        canvas.create_text(250,250, text="Lose!", font=(FONT, 60,"bold","italic"),fill="red")
    global score_text
    global high_score_text
    canvas.delete(score_text)
    score_text=canvas.create_text(40,15, text="Score: " +str(SCORE), font=(FONT, 10,"bold","italic"),fill="black")
    global HIGH_SCORE
    if(SCORE>HIGH_SCORE):
        HIGH_SCORE=SCORE
        canvas.delete(high_score_text)
        high_score_text=canvas.create_text(250,15, text="Score: " +str(HIGH_SCORE), font=(FONT, 10,"bold","italic"),fill="black")
        set_high_Score()
        
    Move=False
    
update()


def move_up(event):
    global Move
    if event.keysym == "Up":
        for i in range(GRID_SZE):
            for j in range(GRID_SZE):
                if numbers[i][j]!=0:
                    temp=i
                    i-=1
                    while i>=0 and numbers[i][j]==0:
                        numbers[i][j]=numbers[i+1][j]
                        numbers[i+1][j]=0
                        i-=1
                        Move=True
                    if i>=0 and numbers[i+1][j]==numbers[i][j]:
                        numbers[i][j]*=2
                        numbers[i+1][j]=0 
                        global SCORE
                        SCORE+=numbers[i][j]
                        Move=True
                    i=temp
        update()
                
def move_down(event):
    global Move
    if event.keysym == "Down":
        for i in range(GRID_SZE):
            for j in range(GRID_SZE):
                if numbers[i][j]!=0:
                    temp=i
                    i+=1
                    while i<GRID_SZE and numbers[i][j]==0:
                        numbers[i][j]=numbers[i-1][j]
                        numbers[i-1][j]=0
                        Move=True
                        i+=1
                    if i<GRID_SZE and numbers[i-1][j]==numbers[i][j]:
                        numbers[i][j]*=2
                        numbers[i-1][j]=0 
                        global SCORE
                        SCORE+=numbers[i][j]
                        Move=True
                    i=temp
        update()
                
def move_left(event):
    global Move
    if event.keysym == "Left":
        for i in range(GRID_SZE):
            for j in range(GRID_SZE):
                if numbers[i][j]!=0:
                    temp=j
                    j-=1
                    while j>=0 and numbers[i][j]==0:
                        numbers[i][j]=numbers[i][j+1]
                        numbers[i][j+1]=0
                        Move=True
                        j-=1
                    if j>=0 and numbers[i][j+1]==numbers[i][j]:
                        numbers[i][j]*=2
                        numbers[i][j+1]=0 
                        global SCORE
                        SCORE+=numbers[i][j]
                        Move=True
                    j=temp
        update()
                
def move_right(event):
    global Move
    if event.keysym == "Right":
        for i in range(GRID_SZE):
            for j in range(GRID_SZE):
                if numbers[i][j]!=0:
                    temp=j
                    j+=1
                    while j<GRID_SZE and numbers[i][j]==0:
                        numbers[i][j]=numbers[i][j-1]
                        numbers[i][j-1]=0
                        Move=True
                        j+=1
                    if j<GRID_SZE and numbers[i][j-1]==numbers[i][j]:
                        numbers[i][j]*=2
                        numbers[i][j-1]=0 
                        global SCORE
                        SCORE+=numbers[i][j]
                        Move=True
                    j=temp
        update()

root.bind("<Left>",lambda event: move_left(event))
root.bind("<Right>",lambda event: move_right(event))
root.bind("<Up>",lambda event: move_up(event))
root.bind("<Down>",lambda event: move_down(event))

root.mainloop()