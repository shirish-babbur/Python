from graphics import *

win = GraphWin("Drawing Plane")
win.setCoords(0.0,0.0,10.0,10.0)

message = Text(Point(5,0.5), "Click on three points")
message.draw(win)

#Take three points based on Mouse Clicks
p1 = win.getMouse()
p1.draw(win)

p2 = win.getMouse()
p2.draw(win)

p3 = win.getMouse()
p3.draw(win)

#Use points to draw a triangle
triangle = Polygon(p1, p2, p3)
triangle.setFill("peachpuff")
triangle.setOutline("cyan")
triangle.draw(win)

#wait for user to click to exit
message.setText("Click anywhere to exit!")
win.getMouse()
win.close()
