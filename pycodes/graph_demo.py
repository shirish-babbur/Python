from graphics import *
from sys import argv

def investment_graph():
    principal = float(input("Enter the principal amount!\n>> "))
    inr = float(input("Enter anal interest rate!\n>> "))

    win = GraphWin("Investment Growth Chart", 320, 240)
    labels = [" 0.0k", " 2.5k", " 5.0k", " 7.5k", "10.0k"]
    p_start = 280

    for label in labels:
        p_start -= 50
        p = Point(20,p_start)
        text = Text(p, label)
        text.draw(win)

    p_rec_hor = Point(40,230)
    p_rec_ver = Point(65, (230 - principal * 0.02))
    rec = Rectangle(p_rec_hor,p_rec_ver)
    rec.setFill("blue")
    rec.draw(win)

    for i in range(10):
        principal += ((principal * 1 * inr) / 100)
        p_hor = Point((25 * i + 40), 230)
        p_ver = Point((25 * i + 40) + 25, (230 - principal * 0.02))
        rec = Rectangle(p_hor, p_ver)
        rec.setFill("blue")
        rec.draw(win)

    wait = input("press any key to close!")
    win.close()


investment_graph()
