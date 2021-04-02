#!/bin/python3
######################################################
# Project: A Simple Scrolling Game
# Name:  Baig, Mirza
# URL: https://trinket.io/library/trinkets/f0b4a70f9e

# Description: n this game, the player tries to avoid "harm" and collect "benefit." 
# The player character is positioned near the left edge of the screen and will move up
# and down based on the user pressing the up and down arrow keys. With the collision with harm,
# it reduces game lives. The player score increases with collision with benefit character.
# The game ends with a message displayed when lives reach 0. 

######################################################

import turtle
import random
import math

#initialize values and variables
s = turtle.Screen()
s.setup(500,500)
s_width = 500
s_height = 500
total_score = 0
s.bgpic("windows.png")

# create dictionaries for the characters in our program
benefit_character = {"turtle": turtle.Turtle(), "width": 50, "height": 86, "shape":"good_char.png"}
harm_character = {"turtle": turtle.Turtle(), "width": 56, "height": 107, "shape": "bad_char.png"}
main_character = {"turtle": turtle.Turtle(), "width": 52, "height": 77, "shape": "main_char.png"}

#creating shortcut for the turtle name
m = main_character["turtle"]
h = harm_character["turtle"]
b = benefit_character["turtle"]

#turtle creater for use of writing score, lives, and game over
t = turtle.Turtle()
t.hideturtle()
t.penup()


#add characters image/shape to screen
s.addshape(main_character["shape"])
s.addshape(harm_character["shape"])
s.addshape(benefit_character["shape"])

#associate shape with the turtle
m.shape(main_character["shape"])
h.shape(harm_character["shape"])
b.shape(benefit_character["shape"])

#penup for all characters
m.penup()
h.penup()
b.penup()

#setting tracer to 0
m.tracer(0)
h.tracer(0)
b.tracer(0)
t.tracer(0)

#when "up" pressed on keyboard
def up():
  if m.ycor() + 154/3 > 250 :
    m.forward(0)
    m.update()
  else:
    m.forward(10)
    m.update()

#when "down" pressed on keyboard
def down():
  if m.ycor()- 154/3 < -250:
    m.backward(0)
    m.update()
  else:
    m.backward(10)
    m.update()

#setting up main character position and heading
def main_character_setup(heading,x,y):
  m.setheading(heading)
  m.setpos(x,y)
  m.update()
  
#setting up benefit character position and heading
def benefit_character_setup(heading,x,y):
  b.setheading(heading)
  b.setpos(x,y)
  b.update()

#setting up harm character position and heading
def harm_character_setup(heading,x,y):
  h.setheading(heading)
  h.setpos(x,y)
  h.update()

# controls the movement and collision of the three characters as well as scoring and lives
def benefit_harm_character_movement():
  global total_score #using global variable total_score created earlier 
  lives = 3
  while lives >= 1:
    b.setx(b.xcor() - 2)
    h.setx(h.xcor() - 3)
    
    #collision detection betwen main and good/benefit character.
    #X-coor had to match. Y-coor were given more scope by adding and subtracting to ycor value to accomdate the height of character/image.
    if m.xcor() == b.xcor() and (m.ycor() - 60 <= b.ycor() and m.ycor() + 60 >= m.ycor()) :
      b.hideturtle()
      b.setx(250)
      b.sety(random.randint(-160,160)) #sets to random y pos
      b.showturtle()
      total_score += 100 #score increases by 100 when colliding with benefit
      
    #checks if it crosses left boundary for benefit character
    elif b.xcor() <= -(s_width/2) - 50:
      b.setx(250)
      b.sety(random.randint(-160,160))
      
    #collision detection betwen main and harm character
    #X-coor had to match. Y-coor were given more scope by adding and subtracting to ycor value to accomdate the height of character/image.
    elif m.xcor() == h.xcor() and (m.ycor() - 76 <= h.ycor() and m.ycor() + 76 >= h.ycor()) :
      h.hideturtle()
      h.setx(250)
      h.sety(random.randint(-130,130)) #sets to random y pos
      h.showturtle()
      lives -= 1
      
    #checks if it crosses left boundary for harm character
    elif h.xcor() <= -(s_width/2) - 56:
      h.setx(250)
      h.sety(random.randint(-130,130)) #sets to random y pos
    else:
      pass
    
    #clearing and writing new score and lives every time through the loop
    t.clear()
    t.hideturtle()
    t.goto(125,220)
    t.write("Score: "+ str(total_score), font=("Arial", 14, "bold"))
    t.goto(35,220)
    t.write("Lives: "+ str(lives), font=("Arial", 14, "bold"))
    t.update()
    b.update()
    h.update()

#clears up the screen of other characters and writing game over and total score
def game_over():
  s.bgcolor("red")
  t.hideturtle()
  t.clear()
  m.hideturtle()
  b.hideturtle()
  h.hideturtle()
  t.goto(-130,10)
  t.write("GAME OVER", font=("Arial", 32, "BOLD"))
  t.goto(-70,-40)
  t.write("Score: " + str(total_score), font=("Arial", 18, "normal"))
  t.update()
  
  
def main():
  s.listen() #listening for keyboard press
  s.onkey(up, "Up") #calls up function and moves up when up key pressed
  s.onkey(down, "Down") #calls down function and moves down when down key pressed
  main_character_setup(90,-224,211) #sets main character 
  benefit_character_setup(90,250,-50) #sets benefit character 
  harm_character_setup(90,250,50) #sets harm character 
  benefit_harm_character_movement() #operates the loop and collision of main with benefit/harm
  game_over() #game over screen with total score

main()









































