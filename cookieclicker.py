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

# var to hold click multiplier clicks and upgrade check amount
clickXAmt = 1
clicks = 0
upgradeCheck = 100


# class to setup buttons
class Button(turtle.Turtle):
    def __init__(self,screen, text, x, y, w, h, color, i, penSize):
        turtle.Turtle.__init__(self)
        self.msg = text
        self.x = x
        self.y = y
        self.pensize = penSize
        self.width = w
        self.height = h
        self.colour = color
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
pen.write(f"Cookies: {clicks}", align="center", font=("Courier New", 28, "normal"))
penMulti = turtle.Turtle()
penMulti.hideturtle()
penMulti.color("white")
penMulti.penup()
penMulti.goto(330, 350)
penMulti.write(f"Click Multiplier: x{clickXAmt}", align="center", font=("Courier New", 15, "normal"))
penUpgrade = turtle.Turtle()
penUpgrade.hideturtle()
penUpgrade.color("red")
penUpgrade.penup()
penUpgrade.goto(0, -250)
button = Button(window, "Upgrade Click", -65, -300, 150, 50, "white", "#8470ff", 15)

# function for button
def UpgradeOne(x, y):
    if x > -65 and x < 85 and y > -300 and y < -250:
        global clickXAmt, upgradeCheck, clicks
        if clicks >= upgradeCheck:
            clickXAmt += 1
            clicks -= upgradeCheck
            upgradeCheck += 50
            pen.clear()
            pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 28, "normal"))          
            penMulti.clear()
            penMulti.write(f"Click Multiplier: x{clickXAmt}", align="center", font=("Courier New", 15, "normal"))
        else:                        
            penUpgrade.write(f"Upgrade costs: {upgradeCheck} clicks", align="center", font=("Courier New", 15, "normal"))
        
# function to increment clicks and add to screen
def clicked(x, y):
    global clicks
    clicks += clickXAmt
    pen.clear()
    penUpgrade.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 28, "normal"))

# call function on click
cookie.onclick(clicked)
turtle.onscreenclick(UpgradeOne)

window.mainloop()