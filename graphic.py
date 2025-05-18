from turtle import Turtle,Screen
import turtle
import random
from data import game_data
# from string import len

letters = game_data["gotian"]
#<========================================= SCREEN SETUP ============================>
screen = Screen()
screen.setup(width = 1920, height= 1080, startx= 0 , starty=0)
screen.title("Hamda's Scrabble Game")
screen.bgcolor("black")
colors = [
    "orange",
    "blue",
    "green",
    "red",
    "brown",
    "gray",
    "yellow",
    "cyan",
    "crimson",
    "darkseagreen",
    "darkgreen",
    "burlywood",
    "aqua",
    "blueviolet",
    "darkmagenta",
    "darkolivegreen",
    "darkslateblue",
    "darkturquoise",
    "darkorange",
    "gold",
    "indigo",
    "lavender",
    "maroon",
    "navy",
    "olive",
    "purple",
    "violet",
    "teal",
    "turquoise",
    "silver",
    "lime",
    "magenta",
    "coral",
    "salmon"
]
    

Turtle = Turtle()


#<============================== INPUTS AND FORMATS ===============================>
Font_large = ("Times New Roman" , 18,'bold')
Font_small = ("Times New Roman" , 15,'bold')
        
Player1 = screen.textinput("Player 1 ","Name: ")  
Player2 = screen.textinput("Player 2 ","Name: ")  
Player3 = screen.textinput("Player 3 ","Name: ")  
Player4 = screen.textinput("Player 4 ","Name: ")  

# if Player1 == Player2 :
#     Player2.capitalize()
# if Player2 == Player3 :
#     Player3    



nOfGotis = 5
sizeOfGotis = 1.5

p1_gotian = []
p2_gotian = []
p3_gotian = []
p4_gotian = []

p1_gotian_temp = []
p2_gotian_temp = []
p3_gotian_temp = []
p4_gotian_temp = []

p1_score = 0
p2_score = 0
p3_score = 0
p4_score = 0

p1_gotian_pos_x = []
p1_gotian_pos_y = []

p2_gotian_pos_x = []
p2_gotian_pos_y = []

p3_gotian_pos_x = []
p3_gotian_pos_y = []

p4_gotian_pos_x = []
p4_gotian_pos_y = []

grid_x = []
grid_y = []

# p1_clicked = {"x":[] ,"y":[]}
# p1_clicked["x"] = []
# p1_clicked["y"] = []

#<================================= BOARD CREATION ===================================>
Turtle.hideturtle()
Turtle.speed(0)
i = -300
j = -270
for y in range (0,15):
    for x in range (0,15):
        Turtle.penup()
        Turtle.goto(i,j)
        grid_x.append(i)
        grid_y.append(j)
        Turtle.pendown()
        Turtle.shape("square")
        Turtle.shapesize(2,2)
        Turtle.color(random.choice(colors))
        Turtle.stamp()
        Turtle.penup()
        i+=40
        # Turtle.forward(40)
    i = -300
    j+= 40
    Turtle.penup()

#<============================================= GRID CREATION =================================>

def draw_lines():
    grid = turtle.Turtle()

    i=-320
    j=-290
    length = 600
    grid.hideturtle()
    grid.speed(0)
    grid.penup()
    grid.goto(i,j)
        
    for rows in range(0,16):
        grid.penup()
        grid.pencolor("black")
        grid.pensize(5)
        grid.goto(i,j)
        grid.pendown()
        grid.forward(length)
        j+=40  
        # grid.penup()
        # grid.left(90)
        
    i=-320
    j=-290
    len = 600 
    grid.penup()
    grid.left(90)
    for column in range(0,16):
        grid.penup()
        grid.pencolor("black")
        grid.pensize(5)
        grid.goto(i,j)
        grid.pendown()
        grid.forward(length)
        i+=40

draw_lines()
#<================================ PLAYER 1 =======================================>
def p1_gotis_allocate(n, wordd):   
    global p1_gotian 
    global p1_gotian_temp
    p1_gotian = []
    Turtle.penup()
    Turtle.goto(-600,200)
    Turtle.pencolor("white")
    Turtle.pendown()
    Turtle.write("Player 1:",font=Font_large)

    Turtle.penup()
    Turtle.goto(-550,150)
    Turtle.pencolor("burlywood")
    Turtle.pendown()
    Turtle.write(Player1,font=Font_large)

    Turtle.penup()
    Turtle.goto(-600,110)
    Turtle.pencolor("crimson")
    Turtle.pendown()
    Turtle.write("Score: ",font=Font_small)

    Turtle.penup()
    Turtle.goto(-520,110)
    Turtle.pencolor("white")
    Turtle.pendown()
    Turtle.write((p1_score),font=Font_small)

    if n==1:  
        for x in range(nOfGotis):
            a = random.choice(letters)
            letters.remove(a)
            if(a == '-'):
                a = screen.textinput("blank tile:","letter: ")  
                # if(str(len(a)) > 1):
                #a = a[0:1]
                p1_gotian.append(a)
            else:
                p1_gotian.append(a)    
            p1_gotian_temp.append(a)
    elif n==2:
        x=0
        for let in p1_gotian_temp:
            if let in wordd:
                a = random.choice(letters)
                letters.remove(a)
                if(a == '-'):
                    a = screen.textinput("blank tile:","letter: ")  
                    p1_gotian.append(a)
                else:
                    p1_gotian.append(a)
            else:
                p1_gotian.append(p1_gotian_temp[x])
            x+=1          
    else:
        for i in range(nOfGotis):
            p1_gotian.append(p1_gotian_temp[i])
#    print(p1_gotian)    
#    print(p1_gotian)
    Turtle.hideturtle()
    Turtle.speed(0)

    Turtle.penup()
    i = -600
    j = 80
    Turtle.goto(i,j)
#    p1_gotian_pos_x=[]
#    p1_gotian_pos_y=[]
    for x in range (0 , len(p1_gotian)):
        Turtle.penup()
        Turtle.goto(i,j)
        Turtle.pendown()
        Turtle.shape("square")
        Turtle.shapesize(sizeOfGotis)
        Turtle.color(random.choice(colors))
        Turtle.stamp()
        Turtle.penup()
        p1_gotian_pos_x.append(i)
        p1_gotian_pos_y.append(j)
        Turtle.goto(i-2,j-10)
        Turtle.pencolor("black")
        Turtle.pendown()
        Turtle.write(p1_gotian[x],font=Font_small)
        i+=35

def p1_scoreCalc():
    
    Turtle.penup()
    Turtle.goto(-520,110)
    Turtle.pencolor("black")
    Turtle.pendown()
    Turtle.write("0000000",font=Font_small)
    
    
    Turtle.penup()
    Turtle.goto(-520,110)
    Turtle.pencolor("white")
    Turtle.pendown()
    Turtle.write((p1_score),font=Font_small)
        

#<================================ PLAYER 2 ========================================>

def p2_gotis_allocate(n, wordd):
    global p2_gotian 
    global p2_gotian_temp
    p2_gotian = []
    Turtle.penup()
    Turtle.goto(350,200)
    Turtle.pencolor('white')
    Turtle.pendown()
    Turtle.write("Player 2:",font=Font_large)

    Turtle.penup()
    Turtle.goto(400,150)
    Turtle.pencolor("burlywood")
    Turtle.pendown()
    Turtle.write(Player2,font=Font_large)

    Turtle.penup()
    Turtle.goto(350,110)
    Turtle.pencolor("crimson")
    Turtle.pendown()
    Turtle.write("Score: ",font=Font_small)

    Turtle.penup()
    Turtle.goto(430,110)
    Turtle.pencolor("white")
    Turtle.pendown()
    Turtle.write((p2_score),font=Font_small)

    if n==1:  
        for x in range(nOfGotis):
            a = random.choice(letters)
            letters.remove(a)
            if(a == '-'):
                a = screen.textinput("blank tile:","letter: ")  
                # if(str(len(a)) > 1):
                #a = a[0:1]
                p2_gotian.append(a)
            else:
                p2_gotian.append(a)    
            p2_gotian_temp.append(a)
    elif n==2:
        x=0
        for let in p2_gotian_temp:
            if let in wordd:
                a = random.choice(letters)
                letters.remove(a)
                if(a == '-'):
                    a = screen.textinput("blank tile:","letter: ")  
                    p2_gotian.append(a)
                else:
                    p2_gotian.append(a)
            else:
                p2_gotian.append(p2_gotian_temp[x])
            x+=1  
    else:
        for i in range(nOfGotis):
            p2_gotian.append(p2_gotian_temp[i])
#    print(p2_gotian)    

    Turtle.hideturtle()
    Turtle.speed(0)

    Turtle.penup()
    i = 350
    j = 80
    Turtle.goto(i,j)

    for x in range (0 , nOfGotis):
        Turtle.penup()
        Turtle.goto(i,j)
        Turtle.pendown()
        Turtle.shape("square")
        Turtle.shapesize(sizeOfGotis)
        Turtle.color(random.choice(colors))
        Turtle.stamp()
        Turtle.penup()
        p2_gotian_pos_x.append(i)
        p2_gotian_pos_y.append(j)
        Turtle.goto(i-2,j-10)
        Turtle.pencolor("black")
        Turtle.pendown()
        Turtle.write(p2_gotian[x],font=Font_small)
        i+=35

def p2_scoreCalc():
    Turtle.penup()
    Turtle.goto(430,110)
    Turtle.pencolor("black")
    Turtle.pendown()
    Turtle.write(000000,font=Font_small)
    
    Turtle.penup()
    Turtle.goto(430,110)
    Turtle.pencolor("white")
    Turtle.pendown()
    Turtle.write((p2_score),font=Font_small)


#<============================= PLAYER 3 ===========================================>
def p3_gotis_allocate(n, wordd):
    global p3_gotian
    global p3_gotian_temp 
    p3_gotian = []
    Turtle.penup()
    Turtle.goto(-600,-50)
    Turtle.pencolor("white")
    Turtle.pendown()
    Turtle.write("Player 3:",font=Font_large)

    Turtle.penup()
    Turtle.goto(-550,-100)
    Turtle.pencolor("burlywood")
    Turtle.pendown()
    Turtle.write(Player3,font=Font_large)

    Turtle.penup()
    Turtle.goto(-600,-140)
    Turtle.pencolor("crimson")
    Turtle.pendown()
    Turtle.write("Score: ",font=Font_small)

    Turtle.penup()
    Turtle.goto(-520,-140)
    Turtle.pencolor("white")
    Turtle.pendown()
    Turtle.write((p3_score),font=Font_small)

    if n==1:  
        for x in range(nOfGotis):
            a = random.choice(letters)
            letters.remove(a)
            if(a == '-'):
                a = screen.textinput("blank tile:","letter: ")  
                # if(str(len(a)) > 1):
                #a = a[0:1]
                p3_gotian.append(a)
            else:
                p3_gotian.append(a)    
            p3_gotian_temp.append(a)
    elif n==2:
        x=0
        for let in p3_gotian_temp:
            if let in wordd:
                a = random.choice(letters)
                letters.remove(a)
                if(a == '-'):
                    a = screen.textinput("blank tile:","letter: ")  
                    p3_gotian.append(a)
                else:
                    p3_gotian.append(a)
            else:
                p3_gotian.append(p3_gotian_temp[x])
            x+=1  
    else:
        for i in range(nOfGotis):
            p3_gotian.append(p3_gotian_temp[i])      
#    print(p3_gotian)   


    Turtle.hideturtle()
    Turtle.speed(0)

    Turtle.penup()
    i = -600
    j = -170
    Turtle.goto(i,j)

    for x in range (0 , nOfGotis):
        Turtle.penup()
        Turtle.goto(i,j)
        Turtle.pendown()
        Turtle.shape("square")
        Turtle.shapesize(sizeOfGotis)
        Turtle.color(random.choice(colors))
        Turtle.stamp()
        Turtle.penup()
        p3_gotian_pos_x.append(i)
        p3_gotian_pos_y.append(j)
        Turtle.goto(i-2,j-10)
        Turtle.pencolor("black")
        Turtle.pendown()
        Turtle.write(p3_gotian[x],font=Font_small)
        i+=35

def p3_scoreCalc():
    Turtle.penup()
    Turtle.goto(-520,-140)
    Turtle.pencolor("black")
    Turtle.pendown()
    Turtle.write("00000",font=Font_small)

    Turtle.penup()
    Turtle.goto(-520,-140)
    Turtle.pencolor("white")
    Turtle.pendown()
    Turtle.write((p3_score),font=Font_small) 

#<============================ PLAYER 4 ============================================>
def p4_gotis_allocate(n, wordd):
    global p4_gotian 
    global p4_gotian_temp
    p4_gotian = []
    Turtle.penup()
    Turtle.goto(350,-50)
    Turtle.pencolor('white')
    Turtle.pendown()
    Turtle.write("Player 4:",font=Font_large)

    Turtle.penup()
    Turtle.goto(400,-100)
    Turtle.pencolor("burlywood")
    Turtle.pendown()
    Turtle.write(Player4,font=Font_large)
    
    Turtle.penup()
    Turtle.goto(350,-140)
    Turtle.pencolor("crimson")
    Turtle.pendown()
    Turtle.write("Score: ",font=Font_small)

    Turtle.penup()
    Turtle.goto(430,-140)
    Turtle.pencolor("white")
    Turtle.pendown()
    Turtle.write((p1_score),font=Font_small)
    
    if n==1:  
        for x in range(nOfGotis):
            a = random.choice(letters)
            letters.remove(a)
            if(a == '-'):
                a = screen.textinput("blank tile:","letter: ")  
                # if(str(len(a)) > 1):
                #a = a[0:1]
                p4_gotian.append(a)
            else:
                p4_gotian.append(a)    
            p4_gotian_temp.append(a)
    elif n==2:
        x=0
        for let in p4_gotian_temp:
            if let in wordd:
                a = random.choice(letters)
                letters.remove(a)
                if(a == '-'):
                    a = screen.textinput("blank tile:","letter: ")  
                    p4_gotian.append(a)
                else:
                    p4_gotian.append(a)
            else:
                p4_gotian.append(p4_gotian_temp[x])
            x+=1 
    else:
        for i in range(nOfGotis):
            p4_gotian.append(p4_gotian_temp[i])  
#    print(p4_gotian)    

    Turtle.hideturtle()
    Turtle.speed(0)

    Turtle.penup()
    i = 350
    j = -170
    Turtle.goto(i,j)

    for x in range (0 , nOfGotis):
        Turtle.penup()
        Turtle.goto(i,j)
        Turtle.pendown()
        Turtle.shape("square")
        Turtle.shapesize(sizeOfGotis)
        Turtle.color(random.choice(colors))
        Turtle.stamp()
        Turtle.penup()
        p4_gotian_pos_x.append(i)
        p4_gotian_pos_y.append(j)    
        Turtle.goto(i-2,j-10)
        Turtle.pencolor("black")
        Turtle.pendown()
        Turtle.write(p4_gotian[x],font=Font_small)
        i+=35

def p4_scoreCalc():
    Turtle.penup()
    Turtle.goto(430,-140)
    Turtle.pencolor("black")
    Turtle.pendown()
    Turtle.write("000000",font=Font_small)
    
    Turtle.penup()
    Turtle.goto(430,-140)
    Turtle.pencolor("white")
    Turtle.pendown()
    Turtle.write((p4_score),font=Font_small)

#<===================================== CALLS =========================>

p1_gotis_allocate(1,"")
p2_gotis_allocate(1,"")
p3_gotis_allocate(1,"")
p4_gotis_allocate(1,"")


# print()
# print(p1_gotian_pos_x)
# print()
# print(p1_gotian_pos_y)
# clicked = ""
# check = False
# def place(x,y):
#     print("GRID: ",x,y)

    # return    


# Screen.exitonclick()

# print(p1_clicked)
# print(len(p1_clicked["x"]))
# size = len(p1_clicked["x"])
# for i in range(0,size):
#     Turtle.penup()
#     Turtle.goto(p1_clicked["x"][i] ,p1_clicked["y"][i])
#     Turtle.clear()
# print(letters)



