# using turtle module
import turtle

# setup screen
window = turtle.Screen()
window.title("Cookie Clicker by Angel")
window.bgcolor("black")

#tell computer what you are using
window.register_shape("cookieIMG.gif")

# create cookie
cookie = turtle.Turtle()
cookie.shape("cookieIMG.gif")

clicks = 0

# draw on screen
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 300)
pen.write(f"Cookies: {clicks}", align="center", font=("Courier New", 32, "normal"))

# function to increment clicks and add to screen
def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

# call function on click
cookie.onclick(clicked)

window.mainloop()