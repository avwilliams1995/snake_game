from turtle import Turtle, Screen
import time
import random
screen = Screen()
class Snake:

    def __init__(self):
        screen = Screen()
        self.all_blocks = []
        self.score = 0
        with open('high_score.txt') as data:
            self.high_score = int(data.read())
        self.current_heading = 0
        self.first = Turtle('square')
        self.all_blocks.append(self.first)
        self.first.color('white')
        self.first.penup()
        self.first.goto(0, 0)
        self.food = Turtle('circle')
        self.food.color('yellow')
        self.food.penup()
        self.food.goto(random.choice(range(-200,200, 20)), random.choice(range(-200,200, 20)))
        self.create_snake()
        screen.title(f"Snake Score: {self.score} High score: {self.high_score}")
        self.block_count = 3
        
        
    def create_snake(self):
        for block in range(1, 3):
            new_block = Turtle('square')
            new_block.color('white')
            new_block.penup()
            new_block.goto(block*-20, 0)
            self.all_blocks.append(new_block)

    def new_block(self):
            new_block = Turtle('square')
            if self.all_blocks[-1].heading() == 90:
                new_block.goto(self.all_blocks[-1].xcor(), self.all_blocks[-1].ycor() - 20)
            elif self.all_blocks[-1].heading() == 270:
                new_block.goto(self.all_blocks[-1].xcor(), self.all_blocks[-1].ycor() + 20)
            elif self.all_blocks[-1].heading() == 0:
                new_block.goto(self.all_blocks[-1].xcor() - 20, self.all_blocks[-1].ycor())
            elif self.all_blocks[-1].heading() == 180:
                new_block.goto(self.all_blocks[-1].xcor() + 20, self.all_blocks[-1].ycor())
            new_block.color('white')
            new_block.penup()
            self.all_blocks.append(new_block)
            self.block_count+=1
              
    def create_food(self):
        self.food.goto(random.choice(range(-200,200, 20)), random.choice(range(-200,200, 20)))
        
    def up(self):
        if self.all_blocks[0].heading() != 270:
            self.current_heading = 90
            self.all_blocks[0].setheading(self.current_heading)
    def down(self):
        if self.all_blocks[0].heading() != 90:
            self.current_heading = 270
            self.all_blocks[0].setheading(self.current_heading)
    def left(self):
        if self.all_blocks[0].heading() != 0:
            self.current_heading = 180
            self.all_blocks[0].setheading(self.current_heading)
    def right(self):
        if self.all_blocks[0].heading() != 180:
            self.current_heading = 0
            self.all_blocks[0].setheading(self.current_heading)
    
    def wall_checker(self):
        if self.first.xcor() > 274:
            self.first.setheading(180)
        elif self.first.xcor() < -274:
            self.first.setheading(0)
        if self.first.ycor() > 274:
            self.first.setheading(270)
        elif self.first.ycor() < -274:
            self.first.setheading(90)

    def touch_check(self, block_count):
        for block in range(1, len(self.all_blocks)):
            if self.first.position() == self.all_blocks[block].position():
                print(f'Game Over! Your final score was {self.score}.')
                if self.score > self.high_score:
                    self.high_score = self.score
                    with open('high_score.txt', mode='w') as data:
                        data.write(f'{self.high_score}')
                exit()

    def move(self):
        self.touch_check(self.block_count)
        for block_num in range(len(self.all_blocks)-1, 0, -1):
            self.touch_check(block_num)
            new_x = self.all_blocks[block_num - 1].xcor()
            new_y = self.all_blocks[block_num - 1].ycor()
            self.all_blocks[block_num].goto(new_x, new_y)
            screen.listen()
            screen.onkey(fun=self.up, key="Up")
            screen.onkey(fun=self.down, key="Down")
            screen.onkey(fun=self.left, key="Left")
            screen.onkey(fun=self.right, key="Right")
            self.wall_checker()
            
        if self.first.distance(self.food) < 1:
                self.create_food()
                self.new_block()
                self.score +=1
                screen.title(f"Snake Score: {self.score} High score: {self.high_score}")
                # self.write("Top Score: {}".format(self.score), align="center", font=("Ariel", 20, "bold"))      
        self.first.fd(20)

    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        
        
            
        
        
        





