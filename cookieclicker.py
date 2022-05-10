# using turtle module
from tkinter import *
import turtle

# setup screen
window = turtle.Screen()
window.title("Cookie Clicker by Angel")
window.bgcolor("black")

#tell computer what you are using
window.register_shape("C:\\Users\\aesqu\\OneDrive\\Desktop\\Python\\Random Fun\\CookieClicker\\cookieIMG.gif")

# create cookie
cookie = turtle.Turtle()
cookie.shape("C:\\Users\\aesqu\\OneDrive\\Desktop\\Python\\Random Fun\\CookieClicker\\cookieIMG.gif")

# var to hold click multiplier and clicks
clickXAmt = 1
clicks = 0

# class to setup buttons
class Button(turtle.Turtle):
    def __init__(self,screen, text, x, y, w, h, color, i, penSize, a=None):
        turtle.Turtle.__init__(self)
        self.msg = text
        self.x = x
        self.y = y
        self.pensize = penSize
        self.width = w
        self.height = h
        self.colour = color
        self.action = a
        self.screen = screen
        self.i_color = i
        self.screen.tracer(0)
        self.ht() 
        self.color(self.colour)
        self.penup()
        self.begin_fill()
        self.goto(self.x, self.y)
        self.pendown()
        self.goto(self.x + self.width, self.y)
        self.goto(self.x + self.width, self.y + self.height)
        self.goto(self.x, self.y + self.height)
        self.goto(self.x, self.y)
        self.end_fill()
        self.penup()
        self.goto(self.x + self.width/2, self.y + self.height/3.5)
        self.color("black")
        self.write(self.msg, False, align="center", font=("Arial", self.pensize, "bold"))
        self.screen.update()

# draw on screen
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 300)
pen.write(f"Cookies: {clicks}", align="center", font=("Courier New", 32, "normal"))
pen2 = turtle.Turtle()
pen2.hideturtle()
pen2.color("white")
pen2.penup()
pen2.goto(330, 350)
pen2.write(f"Click Multiplier: x{clickXAmt}", align="center", font=("Courier New", 15, "normal"))

# function for button
def UpgradeOne(x, y):
    if x > -65 and x < 85 and y > -300 and y < -250:
        global clickXAmt
        clickXAmt += 1
        pen2.clear()
        pen2.write(f"Click Multiplier: x{clickXAmt}", align="center", font=("Courier New", 15, "normal"))       

button = Button(window, "Upgrade Click", -65, -300, 150, 50, "white", "#8470ff", 15, UpgradeOne)

# function to increment clicks and add to screen
def clicked(x, y):
    global clicks
    clicks += clickXAmt
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

# call function on click
cookie.onclick(clicked)
turtle.onscreenclick(UpgradeOne)

window.mainloop()