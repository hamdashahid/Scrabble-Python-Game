import turtle
import graphic
from graphic import Turtle
from graphic import screen,p1_gotian_pos_x,p1_gotian_pos_y,p1_gotian,grid_x,grid_y
from graphic import p2_gotian_pos_x,p2_gotian_pos_y,p2_gotian
from graphic import p3_gotian_pos_x,p3_gotian_pos_y,p3_gotian
from graphic import p4_gotian_pos_x,p4_gotian_pos_y,p4_gotian
# from graphic import p1_gotis_allocate,p2_gotis_allocate,p3_gotis_allocate,p4_gotis_allocate
from data import game_data
import json
import os
import random

check1 = True
check2 = True
check3 = True
check4 = True

turnCount1 = 0
turnCount2 = 0
turnCount3 = 0
turnCount4 = 0

clicked1 = ""
clicked2 = ""
clicked3 = ""
clicked4 = ""

grid_x_temp = grid_x
grid_y_temp = grid_y
full_list=[[' ' for i in range(15)]for j in range(15)]

p1_placed = {"x" : [], "y":[],"grid_x":[] , "grid_y":[],"letter":[]}
p2_placed = {"x" : [], "y":[],"grid_x":[] , "grid_y":[],"letter":[]}
p3_placed = {"x" : [], "y":[],"grid_x":[] , "grid_y":[],"letter":[]}
p4_placed = {"x" : [], "y":[],"grid_x":[] , "grid_y":[],"letter":[]}

complete1 = False
complete2 = False
complete3 = False
complete4 = False

placed1 = True
placed2 = True
placed3 = True
placed4 = True

def click (x,y):
    global complete1
    global complete2
    global complete3
    global complete4
    
    if(complete1 == False):
        player1_turn(x,y)
    elif(complete2 == False):
        player2_turn(x,y)
    elif(complete3 == False):
        player3_turn(x,y)
    elif(complete4 == False):
        player4_turn(x,y) 
    gameOver()     

def need_index(x,y):
    #print(x,y)
    index_x=(x+320)//40
    index_y=-1*((y-270)//40)
    return int(index_x), int(index_y)

def player1_turn(x,y):
    global check1 
    global clicked1
    global complete1
    global complete2
    global placed1
    global full_list
    global turnCount1
    # (x,y)
    Turtle.penup()
    Turtle.goto(-600,40)
    # Turtle.pencolor("black")
    Turtle.pendown()
    Turtle.shape("arrow")
    Turtle.color("white")
    Turtle.shapesize(2,2)
    Turtle.forward(60)
    Turtle.stamp()
    Turtle.pendown()
    if(x >= -545 and x<= -525 and y >= 20 and y<= 60):
        complete1 = True  
        turnCount1+=1 
        complete2 = False 
#        p2_gotis_allocate()
        Turtle.penup()
        Turtle.goto(-600,40)
        # Turtle.pencolor("black")
        Turtle.pendown()
        Turtle.shape("arrow")
        Turtle.color("red")
        Turtle.shapesize(2,2)
        Turtle.forward(60)
        Turtle.stamp()
        Turtle.pendown()
        wordcheck(1)
        p1_placed["grid_x"]=[]
        p1_placed["grid_y"]=[]
    ch = graphic.sizeOfGotis*20
    for i in range(len(graphic.p1_gotian)):
        Turtle.penup()
        if (placed1 == True):
            if x >= p1_gotian_pos_x[i] - (ch/2) and x<= p1_gotian_pos_x[i]+(ch/2) and y >= p1_gotian_pos_y[i]-(ch/2) and y<=p1_gotian_pos_y[i]+(ch/2):
                Turtle.goto(p1_gotian_pos_x[i],p1_gotian_pos_y[i])
                Turtle.pendown()
                Turtle.color("black")
                Turtle.shape("square")
                Turtle.shapesize(graphic.sizeOfGotis)
                Turtle.stamp()
                Turtle.penup()
                clicked1 = graphic.p1_gotian[i]

                pos_x = p1_gotian_pos_x[i]
                pos_y = p1_gotian_pos_y[i]
                check1 = True
                placed1 = False
                p1_placed["x"].append(pos_x)
                p1_placed["y"].append(pos_y)
                graphic.p1_gotian.remove(clicked1)
                #p1_gotian_pos_x.remove(pos_x)
                #p1_gotian_pos_y.remove(pos_y)
                break
                
    Turtle.penup()
    if(check1 == True):
        for j in range(len(grid_x_temp)):
            if(x >= grid_x_temp[j] - 20 and x<=grid_x_temp[j]+20 and y>= grid_y_temp[j]-20 and y<= grid_y_temp[j]+20):
                Turtle.goto(grid_x_temp[j]-2,grid_y_temp[j]-10)
                Turtle.pendown()
                Turtle.color("black")
                Turtle.write(clicked1,font=graphic.Font_small)
                Turtle.penup()
                # ("yes")
#                print(x,y)
#                print(need_index(x,y))
                x1,y1=need_index(x,y)
                if full_list[x1][y1]==' ':
                    full_list[x1][y1]=clicked1
                p1_placed["grid_x"].append(grid_x_temp[j])
                p1_placed["grid_y"].append(grid_y_temp[j])
                p1_placed["letter"].append(clicked1)
                check1 = False
                clicked1 = ""
                placed1 = True
                #grid_x_temp.remove(grid_x_temp[j])
                #grid_y_temp.remove(grid_y_temp[j])
                # (p1_placed)
                # count+=1
                #print(x1,y1)
                #print(full_list)
                break
            
def player2_turn(x,y):
    Turtle.penup()
    Turtle.goto(430,40)
    # Turtle.pencolor("black")
    Turtle.pendown()
    Turtle.shape("arrow")
    Turtle.color("white")
    Turtle.shapesize(2,2)
    Turtle.forward(60)
    Turtle.stamp()
    Turtle.pendown()
    
    global check2 
    global clicked2
    global complete2
    global complete3
    global placed2
    global full_list
    global turnCount2
    if(x >= 485 and x<= 505 and y >= 20 and y<= 60):
        complete2 = True  
        turnCount2+=1
        complete3 = False  
#        p3_gotis_allocate()
        Turtle.penup()
        Turtle.goto(430,40)
        # Turtle.pencolor("black")
        Turtle.pendown()
        Turtle.shape("arrow")
        Turtle.color("red")
        Turtle.shapesize(2,2)
        Turtle.forward(60)
        Turtle.stamp()
        Turtle.pendown()
        wordcheck(2)
        p2_placed["grid_x"]=[]
        p2_placed["grid_y"]=[]
    ch = graphic.sizeOfGotis*20
    for i in range(len(graphic.p2_gotian_pos_x)):
        # ()
        Turtle.penup()
        if (placed2 == True):
            if x >= p2_gotian_pos_x[i] - (ch/2) and x<= p2_gotian_pos_x[i]+(ch/2) and y >= p2_gotian_pos_y[i]-(ch/2) and y<=p2_gotian_pos_y[i]+(ch/2):
                # ()
                Turtle.goto(p2_gotian_pos_x[i],p2_gotian_pos_y[i])
                Turtle.pendown()
                Turtle.color("black")
                Turtle.shape("square")
                Turtle.shapesize(graphic.sizeOfGotis)
                Turtle.stamp()
                Turtle.penup()
#                print(graphic.p2_gotian)
                clicked2 = graphic.p2_gotian[i]                
                pos_x = p2_gotian_pos_x[i]
                pos_y = p2_gotian_pos_y[i]
                # (p2_gotian[i])
                check2 = True
                placed2 = False
                p2_placed["x"].append(pos_x)
                p2_placed["y"].append(pos_y)
                graphic.p2_gotian.remove(clicked2)
                #p2_gotian_pos_x.remove(pos_x)
                #p2_gotian_pos_y.remove(pos_y)
                # (p2_gotian_pos_x[i] ,p2_gotian_pos_y[i] ,clicked2 ,p2_gotian[i] )
                # ()
                # ()
                break
                
    Turtle.penup()
    if(check2 == True):
        for j in range(len(grid_x_temp)):
            if(x >= grid_x_temp[j] - 20 and x<=grid_x_temp[j]+20 and y>= grid_y_temp[j]-20 and y<= grid_y_temp[j]+20):
                Turtle.goto(grid_x_temp[j]-2,grid_y_temp[j]-10)
                Turtle.pendown()
                Turtle.color("black")
                Turtle.write(clicked2,font=graphic.Font_small)
                Turtle.penup()
                # ("yes",clicked2)
                p2_placed["grid_x"].append(grid_x_temp[j])
                p2_placed["grid_y"].append(grid_y_temp[j])
                p2_placed["letter"].append(clicked2)
                x1,y1=need_index(x,y)
                if full_list[x1][y1]==' ':
                    full_list[x1][y1]=clicked2
                #grid_x_temp.remove(grid_x_temp[j])
                #grid_y_temp.remove(grid_y_temp[j])
                check2 = False
                clicked2 = ""
                placed2 = True
                # (p2_placed)
                # count+=1
                #print(full_list)
                break

def player3_turn(x,y):
    (x,y)
    Turtle.penup()
    Turtle.goto(-520,-250)
    # Turtle.pencolor("black")
    Turtle.pendown()
    Turtle.shape("arrow")
    Turtle.color("white")
    Turtle.shapesize(2,2)
    Turtle.forward(60)
    Turtle.stamp()
    Turtle.pendown()
    
    global check3 
    global clicked3
    global complete3
    global complete4
    global placed3
    global full_list
    global turnCount3
    if(x >= -465 and x<= -445 and y >= -270 and y<= -230):
        complete3 = True  
        complete4 = False
        turnCount3+=1
#        p4_gotis_allocate()
        Turtle.penup()
        Turtle.goto(-520,-250)
        # Turtle.pencolor("black")
        Turtle.pendown()
        Turtle.shape("arrow")
        Turtle.color("red")
        Turtle.shapesize(2,2)
        Turtle.forward(60)
        Turtle.stamp()
        Turtle.pendown()
        wordcheck(3)
        p3_placed["grid_x"]=[]
        p3_placed["grid_y"]=[]
    ch = graphic.sizeOfGotis*20
    for i in range(len(graphic.p3_gotian_pos_x)):
        Turtle.penup()
        if (placed3 == True):
            if x >= p3_gotian_pos_x[i] - (ch/2) and x<= p3_gotian_pos_x[i]+(ch/2) and y >= p3_gotian_pos_y[i]-(ch/2) and y<=p3_gotian_pos_y[i]+(ch/2):
                Turtle.goto(p3_gotian_pos_x[i],p3_gotian_pos_y[i])
                Turtle.pendown()
                Turtle.color("black")
                Turtle.shape("square")
                Turtle.shapesize(graphic.sizeOfGotis)
                Turtle.stamp()
                Turtle.penup()
                clicked3 = graphic.p3_gotian[i]
                pos_x = p3_gotian_pos_x[i]
                pos_y = p3_gotian_pos_y[i]
                check3 = True
                placed3 = False
                p3_placed["x"].append(pos_x)
                p3_placed["y"].append(pos_y)
                graphic.p3_gotian.remove(clicked3)
                #p3_gotian_pos_x.remove(pos_x)
                #p3_gotian_pos_y.remove(pos_y)
                break
                
    Turtle.penup()
    if(check3 == True):
        for j in range(len(grid_x_temp)):
            if(x >= grid_x_temp[j] - 20 and x<=grid_x_temp[j]+20 and y>= grid_y_temp[j]-20 and y<= grid_y_temp[j]+20):
                Turtle.goto(grid_x_temp[j]-2,grid_y_temp[j]-10)
                Turtle.pendown()
                Turtle.color("black")
                Turtle.write(clicked3,font=graphic.Font_small)
                Turtle.penup()
                # ("yes")
                p3_placed["grid_x"].append(grid_x_temp[j])
                p3_placed["grid_y"].append(grid_y_temp[j])
                p3_placed["letter"].append(clicked3)
                x1,y1=need_index(x,y)
                if full_list[x1][y1]==' ':
                    full_list[x1][y1]=clicked3
                #grid_x_temp.remove(grid_x_temp[j])
                #grid_y_temp.remove(grid_y_temp[j])
                check3 = False
                clicked3 = ""
                placed3 = True
                # (p3_placed)
                # count+=1
                #print(full_list)
                break

def player4_turn(x,y):
    # (x,y)
    Turtle.penup()
    Turtle.goto(430,-250)
    # Turtle.pencolor("black")
    Turtle.pendown()
    Turtle.shape("arrow")
    Turtle.color("white")
    Turtle.shapesize(2,2)
    Turtle.forward(60)
    Turtle.stamp()
    Turtle.pendown()
    global check4 
    global clicked4
    global complete4
    global complete1
    global placed4
    global full_list
    global turnCount4
    
    if(x >= 485 and x<= 505 and y >= -270 and y<= -230):
        complete4 = True  
        turnCount4+=1 
        complete1 = False 
#        p1_gotis_allocate()
        Turtle.penup()
        Turtle.goto(430,-250)
        # Turtle.pencolor("black")
        Turtle.pendown()
        Turtle.shape("arrow")
        Turtle.color("red")
        Turtle.shapesize(2,2)
        Turtle.forward(60)
        Turtle.stamp()
        Turtle.pendown()
        wordcheck(4)
        p4_placed["grid_x"]=[]
        p4_placed["grid_y"]=[]
    ch = graphic.sizeOfGotis*20
    for i in range(len(graphic.p4_gotian_pos_x)):
        Turtle.penup()
        if (placed4 == True):
            if x >= p4_gotian_pos_x[i] - (ch/2) and x<= p4_gotian_pos_x[i]+(ch/2) and y >= p4_gotian_pos_y[i]-(ch/2) and y<=p4_gotian_pos_y[i]+(ch/2):
                Turtle.goto(p4_gotian_pos_x[i],p4_gotian_pos_y[i])
                Turtle.pendown()
                Turtle.color("black")
                Turtle.shape("square")
                Turtle.shapesize(graphic.sizeOfGotis)
                Turtle.stamp()
                Turtle.penup()
                clicked4 = graphic.p4_gotian[i]
                pos_x = p4_gotian_pos_x[i]
                pos_y = p4_gotian_pos_y[i]
                check4 = True
                placed4 = False
                p4_placed["x"].append(pos_x)
                p4_placed["y"].append(pos_y)
                graphic.p4_gotian.remove(clicked4)
                #p4_gotian_pos_x.remove(pos_x)
                #p4_gotian_pos_y.remove(pos_y)
                break
                
    Turtle.penup()
    if(check4 == True):
        for j in range(len(grid_x_temp)):
            if(x >= grid_x_temp[j] - 20 and x<=grid_x_temp[j]+20 and y>= grid_y_temp[j]-20 and y<= grid_y_temp[j]+20):
                Turtle.goto(grid_x_temp[j]-2,grid_y_temp[j]-10)
                Turtle.pendown()
                Turtle.color("black")
                Turtle.write(clicked4,font=graphic.Font_small)
                Turtle.penup()
                # ("yes")
                p4_placed["grid_x"].append(grid_x_temp[j])
                p4_placed["grid_y"].append(grid_y_temp[j])
                p4_placed["letter"].append(clicked4)
                x1,y1=need_index(x,y)
                if full_list[x1][y1]==' ':
                    full_list[x1][y1]=clicked4
#                grid_x_temp.remove(grid_x_temp[j])
#                grid_y_temp.remove(grid_y_temp[j])
                check4 = False
                clicked4 = ""
                placed4 = True
                # (p4_placed)
                # count+=1
                #print(full_list)
                break

formed_already=[]
formed=False

def wordcheck(ii):
    global formed_already
    global formed
    #<======================================== CHECK HORIZONTALLY ==========================================>
    formed=False
    a=""
    strr=""
    for j in range(15):
        for i in range(15):
            if full_list[i][j]!=' ':
                a+=full_list[i][j]
            else:
                for b in game_data["words"]:
                    if(b == a) and a not in formed_already :
                        print("YAHOOOO " , b)
                        formed=True
                        strr=a
                        formed_already.append(a)
                a=""        
                
        
        
#<================================== CHECK VERTICALLY ==================================>
   
    a=""
    for i in range(15):
        for j in range(15):
            if full_list[i][j]!=' ':
                a+=full_list[i][j]
            else:
                for b in game_data["words"]:
                    if(b == a) and a not in formed_already:
                        strr=a
                        print("YAHOOOO " , b)
                        formed=True
                        formed_already.append(a)
                        
                a=""
    
    if not formed:
        undo(ii)
    else:
        addNewGotis(ii, strr)
        # formed = False


def undo(player = 1):
    global p1_gotian
    global p2_gotian
    global p3_gotian
    global p4_gotian
    Turtle.penup()
    if player == 1:
        for i in range(len(p1_placed["grid_x"])):
            Turtle.penup()
#            Turtle.goto(p1_placed["x"][i],p1_placed["y"][i])
#            Turtle.pendown()
#            Turtle.color(random.choice(graphic.colors))
#            Turtle.shape("square")
#            Turtle.shapesize(1.5)
#            Turtle.stamp()
            
#            Turtle.penup()
#            Turtle.goto(p1_placed["x"][i]-2,p1_placed["y"][i]-10)
#            Turtle.color("black")
#            Turtle.write(p1_placed["letter"][i],font=graphic.Font_small)
            Turtle.goto(p1_placed["grid_x"][i],p1_placed["grid_y"][i])
            Turtle.pendown()
            Turtle.color(random.choice(graphic.colors))
            Turtle.shape("square")
            Turtle.shapesize(2)
            Turtle.stamp()

#            graphic.p1_gotian=graphic.p1_gotian_temp
            
            x1,y1 = need_index(p1_placed["grid_x"][i],p1_placed["grid_y"][i])
            full_list[x1][y1]=' '
        graphic.p1_gotian_pos_x=[]
        graphic.p1_gotian_pos_y=[]
        graphic.p1_gotis_allocate(0,"")
               
    elif player == 2:
        for i in range(len(p2_placed["grid_x"])):
            Turtle.penup()
#            Turtle.goto(p2_placed["x"][i],p2_placed["y"][i])
#            Turtle.pendown()
#            Turtle.color(random.choice(graphic.colors))
#            Turtle.shape("square")
#            Turtle.shapesize(1.5)
#            Turtle.stamp()
#            Turtle.goto(p2_placed["x"][i]-2,p2_placed["y"][i]-10)
#            Turtle.color("black")
#            Turtle.write(p2_placed["letter"][i],font=graphic.Font_small)
            
            Turtle.penup()
            Turtle.goto(p2_placed["grid_x"][i],p2_placed["grid_y"][i])
            Turtle.pendown()
            Turtle.color(random.choice(graphic.colors))
            Turtle.shape("square")
            Turtle.shapesize(2)
            Turtle.stamp()
            
            graphic.p2_gotian=graphic.p2_gotian_temp

            x1,y1 = need_index(p2_placed["grid_x"][i],p2_placed["grid_y"][i])
            full_list[x1][y1]=' '
        graphic.p2_gotian_pos_x=[]
        graphic.p2_gotian_pos_y=[]
        graphic.p2_gotis_allocate(0,"")
            
    elif player == 3:
        for i in range(len(p3_placed["grid_x"])):
            Turtle.penup()
#            Turtle.goto(p3_placed["x"][i],p3_placed["y"][i])
#            Turtle.pendown()
#            Turtle.color(random.choice(graphic.colors))
#            Turtle.shape("square")
#            Turtle.shapesize(1.5)
#            Turtle.stamp()
#            Turtle.goto(p3_placed["x"][i]-2,p3_placed["y"][i]-10)
#            Turtle.color("black")
#            Turtle.write(p3_placed["letter"][i],font=graphic.Font_small)
            
            Turtle.penup()
            Turtle.goto(p3_placed["grid_x"][i],p3_placed["grid_y"][i])
            Turtle.pendown()
            Turtle.color(random.choice(graphic.colors))
            Turtle.shape("square")
            Turtle.shapesize(2)
            Turtle.stamp()

            graphic.p3_gotian=graphic.p3_gotian_temp

            x1,y1 = need_index(p3_placed["grid_x"][i],p3_placed["grid_y"][i])
            full_list[x1][y1]=' '
        graphic.p3_gotian_pos_x=[]
        graphic.p3_gotian_pos_y=[]
        graphic.p3_gotis_allocate(0,"")
        
    elif player == 4: 
        for i in range (len(p4_placed["grid_x"])):
            Turtle.penup()
#            Turtle.goto(p4_placed["x"][i],p4_placed["y"][i])
#            Turtle.pendown()
#            Turtle.color(random.choice(graphic.colors))
#            Turtle.shape("square")
#            Turtle.shapesize(1.5)
#            Turtle.stamp()
#            Turtle.goto(p4_placed["x"][i]-2,p4_placed["y"][i]-10)
#            Turtle.color("black")
#            Turtle.write(p4_placed["letter"][i],font=graphic.Font_small)
            
            
            Turtle.penup()
            Turtle.goto(p4_placed["grid_x"][i],p4_placed["grid_y"][i])
            Turtle.pendown()
            Turtle.color(random.choice(graphic.colors))
            Turtle.shape("square")
            Turtle.shapesize(2)
            Turtle.stamp()

            graphic.p4_gotian=graphic.p4_gotian_temp

            x1,y1 = need_index(p4_placed["grid_x"][i],p4_placed["grid_y"][i])
            full_list[x1][y1]=' '
        graphic.p4_gotian_pos_x=[]
        graphic.p4_gotian_pos_y=[]
        graphic.p4_gotis_allocate(0,"")

    graphic.draw_lines()
    #print(full_list)
                   
def addNewGotis(player = 1 , word = ""):
    Turtle.penup()
    if player == 1:
        graphic.p1_gotian_pos_x=[]
        graphic.p1_gotian_pos_y=[]
        graphic.p1_gotis_allocate(2,word)
            
        for x in word :
            for a in game_data["alphabet_score"]  :
                if (a["alphabet"] == x):
                    graphic.p1_score += a["score"]  
        
        graphic.p1_scoreCalc()
        wordFileHandling(word,graphic.p1_score,graphic.Player1)
                    
    elif player == 2:       
        graphic.p2_gotian_pos_x=[]
        graphic.p2_gotian_pos_y=[]
        graphic.p2_gotis_allocate(2,word)
            
        for x in word :
            for a in game_data["alphabet_score"]  :
                if (a["alphabet"] == x):
                    graphic.p2_score += a["score"]  
        
        graphic.p2_scoreCalc()
        wordFileHandling(word,graphic.p2_score,graphic.Player2)
        
    elif player == 3:
        graphic.p3_gotian_pos_x=[]
        graphic.p3_gotian_pos_y=[]
        graphic.p3_gotis_allocate(2,word)
            
        for x in word :
            for a in game_data["alphabet_score"]  :
                if (a["alphabet"] == x):
                    graphic.p3_score += a["score"]  
        
        graphic.p3_scoreCalc()
        wordFileHandling(word,graphic.p3_score,graphic.Player3)
        
    elif player == 4:
        graphic.p4_gotian_pos_x=[]
        graphic.p4_gotian_pos_y=[]
        graphic.p4_gotis_allocate(2,word)
            
        for x in word :
            for a in game_data["alphabet_score"]  :
                if (a["alphabet"] == x):
                    graphic.p4_score += a["score"]  
        
        graphic.p4_scoreCalc()
        wordFileHandling(word,graphic.p4_score,graphic.Player4)
        
def wordFileHandling(word,score,name):
    str = f"{name}.json"
    data = {f"{word}" : score}
    
    if not os.path.exists(str):
        with open(str,'w') as file:
            json.dump(data,file)
            file.write('\n')

    else:
        with open(str, 'r+') as file:
            previous_data = json.load(file)
            previous_data[word] = score
            file.seek(0)
            json.dump(previous_data, file)
            file.write('\n')
            file.truncate()

winner = "draw"
dict = {}
max = 0

def gameOver():
    print("hi")
    global turnCount1
    global turnCount2
    global turnCount3
    global turnCount4
    if ((turnCount1 == 5 and turnCount2 == 5 and turnCount3 == 5 and turnCount4 == 5)  or (len(graphic.letters) == 0)):
        global max
        global winner
        global dict
        
        # if
        if graphic.p1_score > max:
            max = graphic.p1_score
            winner = graphic.Player1
            
        elif graphic.p2_score > max:
            max = graphic.p2_score
            winner = graphic.Player2
            
        elif graphic.p3_score > max:
            max = graphic.p3_score
            winner = graphic.Player3
            
        elif graphic.p4_score > max:
            max = graphic.p4_score
            winner = graphic.Player4
         
        if graphic.p1_score == graphic.p2_score or graphic.p1_score == graphic.p3_score or graphic.p1_score == graphic.p4_score:
            if graphic.p2_score == graphic.p3_score or graphic.p2_score == graphic.p4_score or graphic.p3_score == graphic.p4_score:
                # str = f"{winner}.json"
                # with open(str,'r') as file:
                #     dict = json.load(file)
                
                with open("winner.txt" , 'a') as file:
                    file.write(f"DRAW!!\n {graphic.Player1} score : {graphic.p1_score} \n")
                    file.write(f"{graphic.Player2} score : {graphic.p2_score} \n")
                    file.write(f"{graphic.Player3} score : {graphic.p3_score} \n")
                    file.write(f"{graphic.Player4} score : {graphic.p4_score} \n")
                    # for keys in dict :
                    #     file.ap(f"{keys} : {dict[keys]} \n")
                
        else:
                 
            str = f"{winner}.json"
                
            with open(str,'r') as file:
                dict = json.load(file)
            
            with open("winner.txt" , 'a') as file:
                file.write(f"{winner}\n")
                for keys in dict :
                    file.write(f"{keys} : {dict[keys]} \n")
                    
        screen.bye()            
                
           

screen.onclick(click,1)

screen.mainloop()