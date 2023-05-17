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
    mirror = Oval(Point(475, 400), Point(525, 600))
    axis = Line(Point(0, 500), Point(1000, 500))
    objDistNum = 10
    objDistBox = Rectangle(Point(5, 5), Point(105, 55))
    objDistText = Text(Point(55, 30), objDistNum)
    imgDistNum = -15
    imgDistBox = Rectangle(Point(110, 5), Point(210, 55))
    imgDistText = Text(Point(160, 30), imgDistNum)
    focDistNum = (1 / objDistNum) + (1 / imgDistNum)
    focDistNum = 1 / focDistNum
    focDistBox = Rectangle(Point(215, 5), Point(315, 55))
    focDistText = Text(Point(265, 30), focDistNum)
    marks = []
    xMark = 0
    while xMark <= 1000:
        if xMark > 525 or xMark < 475:
            marks.append(Line(Point(xMark, 490), Point(xMark, 510)))
        xMark += 10
    mirror.draw(win)
    axis.draw(win)
    objDistBox.draw(win)
    objDistText.draw(win)
    imgDistBox.draw(win)
    imgDistText.draw(win)
    focDistBox.draw(win)
    focDistText.draw(win)
    for mark in marks:
        mark.draw(win)
    while True:
        click = win.getMouse()
        if pointIn(click, objDistBox):
            objDistNum += 1
        elif pointIn(click, imgDistBox):
            imgDistNum += 1
        elif pointIn(click, focDistBox):
            focDistNum += 1
        objDistNum = (1 / focDistNum) - (1 / imgDistNum)
        objDistNum = 1 / objDistNum
        imgDistNum = (1 / focDistNum) - (1 / objDistNum)
        imgDistNum = 1 / imgDistNum
        focDistNum = (1 / objDistNum) + (1 / imgDistNum)
        focDistNum = 1 / focDistNum
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
