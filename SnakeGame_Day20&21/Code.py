# Snake game using Python's Turtle module
from snake import Snake
from scoreboard import Scoreboard
from turtle import Screen
from food import Food 
import time,random,tkinter.messagebox as mb
def refresh(food):
  food.goto(random.randint(-280,280),random.randint(-180,180))
scr=Screen()
food=Food()
scr.bgcolor("black")
scr.setup(600,400)
scr.title("Hungry Snake")
scr.tracer(0)
snake=Snake()
score=Scoreboard("./SnakeGame_Day20&21/HighScore.txt")
scr.update()
scr.listen()
game_is_on=True
c=0
scr.onkey(snake.move_up,"Up")  
scr.onkey(snake.move_down,"Down")
scr.onkey(snake.move_left,"Left")
scr.onkey(snake.move_right,"Right")

while game_is_on:
  scr.update()
  time.sleep(0.1)
  snake.move_forward()
  if snake.lst[0].distance(food.xcor(),food.ycor())<15:
    food.refresh()
    score.refresh()
    snake.refresh()
  snake.check_wall()
  game_is_on=snake.check_collision()
score.display_high_score()
mb.showinfo("Game Over",f"Your score: {score.sums}")
scr.exitonclick()
