from graphics import *


def main():
    types = {
        "1": conMirror,
        #'2': divMirror,
        #'3': conLens,
        #'4': divLens
    }
    print("Choose your mirror/lens: ")
    print("1: Concave/Converging Mirror")
    print("2: Convex/Diverging Mirror")
    print("3: Converging Thin Lens")
    print("4: Diverging Thin Lens")
    # choice = input()
    conMirror()


# Preconditions: Point 1 of rect should have x and y values less than Point 2 x and y values
def pointIn(p, rect):
    if (
        p.getX() > rect.getP1().getX()
        and p.getX() < rect.getP2().getX()
        and p.getY() > rect.getP1().getY()
        and p.getY() < rect.getP2().getY()
    ):
        return True
    return False


def conMirror():
    win = GraphWin("Converging Mirror", 1000, 1000)
    win.setBackground("white")
    mirror = Oval(Point(500, 400), Point(600, 600))
    whiteOut = Oval(Point(525,400),Point(600,600))
    axis = Line(Point(0, 500), Point(1000, 500))
    objDistNum = 10
    objDistBox = Rectangle(Point(5, 5), Point(105, 55))
    objDistText = Text(Point(55, 30), objDistNum)
    objDistDownBox = Rectangle(Point(5,60),Point(55,85))
    objDistUpBox = Rectangle(Point(55,60),Point(105,85))
    imgDistNum = -15
    imgDistBox = Rectangle(Point(110, 5), Point(210, 55))
    imgDistText = Text(Point(160, 30), imgDistNum)
    imgDistDownBox = Rectangle(Point(110,60),Point(160,85))
    imgDistUpBox = Rectangle(Point(160,60),Point(210,85))
    focDistNum = (1 / objDistNum) + (1 / imgDistNum)
    focDistNum = round(1 / focDistNum,3)
    focDistBox = Rectangle(Point(215, 5), Point(315, 55))
    focDistText = Text(Point(265, 30), focDistNum)
    focDistDownBox = Rectangle(Point(215,60),Point(265,85))
    focDistUpBox = Rectangle(Point(265,60),Point(315,85))
    marks = []
    xMark = 0
    while xMark <= 1000:
        if xMark > 500 or xMark < 500:
            marks.append(Line(Point(xMark, 490), Point(xMark, 510)))
        xMark += 10
    mirror.draw(win)
    whiteOut.setOutline("white")
    whiteOut.setFill("white")
    whiteOut.draw(win)
    axis.draw(win)
    objDistBox.draw(win)
    objDistText.draw(win)
    objDistDownBox.draw(win)
    objDistDownBox.setFill("red")
    objDistUpBox.draw(win)
    objDistUpBox.setFill("green")
    imgDistBox.draw(win)
    imgDistText.draw(win)
    imgDistDownBox.draw(win)
    imgDistDownBox.setFill("red")
    imgDistUpBox.draw(win)
    imgDistUpBox.setFill("green")
    focDistBox.draw(win)
    focDistText.draw(win)
    focDistDownBox.draw(win)
    focDistDownBox.setFill("red")
    focDistUpBox.draw(win)
    focDistUpBox.setFill("green")
    for mark in marks:
        mark.draw(win)
    while True:
        click = win.getMouse()
        if pointIn(click, objDistDownBox):
            objDistNum -= 1
            imgDistNum = (1 / focDistNum) - (1 / objDistNum)
            imgDistNum = 1 / imgDistNum
            focDistNum = (1 / objDistNum) + (1 / imgDistNum)
            focDistNum = round(1 / focDistNum,3)
        elif pointIn(click, objDistUpBox):
            objDistNum += 1
            imgDistNum = (1 / focDistNum) - (1 / objDistNum)
            imgDistNum = 1 / imgDistNum
            focDistNum = (1 / objDistNum) + (1 / imgDistNum)
            focDistNum = round(1 / focDistNum,3)
        elif pointIn(click, imgDistDownBox):
            imgDistNum -= 1
            objDistNum = (1 / focDistNum) - (1 / imgDistNum)
            objDistNum = 1 / objDistNum
            focDistNum = (1 / objDistNum) + (1 / imgDistNum)
            focDistNum = round(1 / focDistNum,3)
        elif pointIn(click, imgDistUpBox):
            imgDistNum += 1
            objDistNum = (1 / focDistNum) - (1 / imgDistNum)
            objDistNum = 1 / objDistNum
            focDistNum = (1 / objDistNum) + (1 / imgDistNum)
            focDistNum = round(1 / focDistNum,3)
        elif pointIn(click, focDistDownBox):
            focDistNum -= 1
            objDistNum = (1 / focDistNum) - (1 / imgDistNum)
            objDistNum = 1 / objDistNum
            imgDistNum = (1 / focDistNum) - (1 / objDistNum)
            imgDistNum = 1 / imgDistNum
        elif pointIn(click, focDistUpBox):
            focDistNum += 1
            objDistNum = (1 / focDistNum) - (1 / imgDistNum)
            objDistNum = 1 / objDistNum
            imgDistNum = (1 / focDistNum) - (1 / objDistNum)
            imgDistNum = 1 / imgDistNum
        objDistNum = round(objDistNum,3)
        imgDistNum = round(imgDistNum,3)
        focDistNum = round(focDistNum,3)
        objDistText.undraw()
        objDistText = Text(Point(55, 30), objDistNum)
        objDistText.draw(win)
        imgDistText.undraw()
        imgDistText = Text(Point(160, 30), imgDistNum)
        imgDistText.draw(win)
        focDistText.undraw()
        focDistText = Text(Point(265, 30), focDistNum)
        focDistText.draw(win)


main()
