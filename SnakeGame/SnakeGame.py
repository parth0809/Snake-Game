from turtle import Turtle,Screen, position
import time
import random
import turtle


class snake:
    turtleobj=[]
    def __init__(self,screen):
        screen= Screen()
        screen.tracer(0)
        for i in range(3):
            t=Turtle(shape="square")
            t.color("white")
            t.penup()
            t.goto(-20*i,0)
            self.turtleobj.append(t)        
    def move_snake(self):
        screen.update()
        time.sleep(0.1)
        for seg_num in range(len(self.turtleobj)-1,0,-1):
            newx=self.turtleobj[seg_num-1].xcor()
            newy=self.turtleobj[seg_num-1].ycor()
            self.turtleobj[seg_num].goto(newx,newy)
        self.turtleobj[0].forward(20)
    def up(self):
        if(self.turtleobj[0].heading()!=-90):
            self.turtleobj[0].setheading(90)
    def down(self):
        if(self.turtleobj[0].heading()!=90):
            self.turtleobj[0].setheading(-90)
    def left(self):
        if(self.turtleobj[0].heading()!=0):
            self.turtleobj[0].setheading(180)
    def right(self):
        if(self.turtleobj[0].heading()!=180):
            self.turtleobj[0].setheading(0)
    def inc_size(self):
        i=self.turtleobj[-1].position()
        t=Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(i)
        self.turtleobj.append(t)



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.x=random.randint(-280,280)
        self.y=random.randint(-280,280)
        self.goto(self.x,self.y)
    def refresh(self):
        self.penup()
        self.x=random.randint(-280,280)
        self.y=random.randint(-280,280)
        self.goto(self.x,self.y)




class scoreboad(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()  
        self.score=0
        self.penup()
        self.color("white")
        self.goto(0,250)
        self.write(f"Score : {self.score}",align="center",font=("Arial",24,"normal"))
    def inc_score(self):
        self.score+=1 
        self.clear()
        self.write(f"Score : {self.score}",align="center",font=("Arial",24,"normal"))
    
    def gameover(self):
       self.goto(0,0)
       self.write("Game Over ",align="center",font=("Arial",24,"normal"))




screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
s=snake(screen)
food=Food()
screen.listen()
screen.onkey(fun=s.up,key="Up")
screen.onkey(fun=s.down,key="Down")
screen.onkey(fun=s.left,key="Left")
screen.onkey(fun=s.right,key="Right")
gameover=False
score=scoreboad()



while(not gameover):
    s.move_snake()
    if snake.turtleobj[0].distance(food)<15:
        food.refresh()
        s.inc_size()
        score.inc_score()

    if(snake.turtleobj[0].xcor()>280 or snake.turtleobj[0].ycor()>280 or snake.turtleobj[0].xcor()<-280 or snake.turtleobj[0].ycor()<-280):
        gameover=True
        score.gameover()
    for segment in s.turtleobj[1:]:
        if(snake.turtleobj[0].distance(segment)<10):
            gameover=True
            score.gameover()


screen.exitonclick()  