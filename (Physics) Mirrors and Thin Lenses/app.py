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
    objHeightNum = 5
    objHeightBox = Rectangle(Point(320, 5), Point(420, 55))
    objHeightText = Text(Point(370, 30), objHeightNum)
    objHeightDownBox = Rectangle(Point(320,60),Point(370,85))
    objHeightUpBox = Rectangle(Point(370,60),Point(420,85))
    imgHeightNum = -1*imgDistNum*objHeightNum/objDistNum
    imgHeightNum = round(imgHeightNum,3)
    imgHeightBox = Rectangle(Point(425, 5), Point(525, 55))
    imgHeightText = Text(Point(475, 30), imgHeightNum)
    imgHeightDownBox = Rectangle(Point(425,60),Point(475,85))
    imgHeightUpBox = Rectangle(Point(475,60),Point(525,85))
    magNum = -1*imgDistNum/objDistNum
    magNum = round(magNum,3)
    magBox = Rectangle(Point(530, 5), Point(630, 55))
    magText = Text(Point(580, 30), magNum)
    magDownBox = Rectangle(Point(530,60),Point(580,85))
    magUpBox = Rectangle(Point(580,60),Point(630,85))
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
    objHeightBox.draw(win)
    objHeightText.draw(win)
    objHeightDownBox.draw(win)
    objHeightDownBox.setFill("red")
    objHeightUpBox.draw(win)
    objHeightUpBox.setFill("green")
    imgHeightBox.draw(win)
    imgHeightText.draw(win)
    imgHeightDownBox.draw(win)
    imgHeightDownBox.setFill("red")
    imgHeightUpBox.draw(win)
    imgHeightUpBox.setFill("green")
    magBox.draw(win)
    magText.draw(win)
    magDownBox.draw(win)
    magDownBox.setFill("red")
    magUpBox.draw(win)
    magUpBox.setFill("green")
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
            imgDistNum =  (1 / focDistNum) - (1 / objDistNum)
            imgDistNum = 1/ imgDistNum
        elif pointIn(click, objHeightDownBox):
            objHeightNum -= 1
            imgHeightNum = magNum*objHeightNum
        elif pointIn(click, objHeightUpBox):
            objHeightNum += 1
            imgHeightNum = magNum*objHeightNum
        elif pointIn(click, imgHeightDownBox):
            imgHeightNum -= 1
            objHeightNum = imgHeightNum/magNum
        elif pointIn(click, imgHeightUpBox):
            imgHeightNum += 1
            objHeightNum = imgHeightNum/magNum
        elif pointIn(click, magDownBox):
            magNum -= 1
            imgHeightNum = magNum*objHeightNum
        elif pointIn(click, magUpBox):
            magNum += 1
            imgHeightNum = magNum*objHeightNum
        objDistNum = round(objDistNum,3)
        imgDistNum = round(imgDistNum,3)
        focDistNum = round(focDistNum,3)
        objHeightNum = round(objHeightNum,3)
        imgDistNum = round(imgHeightNum,3)
        magNum = round(magNum,3)
        objDistText.undraw()
        objDistText = Text(Point(55, 30), objDistNum)
        objDistText.draw(win)
        imgDistText.undraw()
        imgDistText = Text(Point(160, 30), imgDistNum)
        imgDistText.draw(win)
        focDistText.undraw()
        focDistText = Text(Point(265, 30), focDistNum)
        focDistText.draw(win)
        objHeightText.undraw()
        objHeightText = Text(Point(370, 30), objHeightNum)
        objHeightText.draw(win)
        imgHeightText.undraw()
        imgHeightText = Text(Point(475, 30), imgHeightNum)
        imgHeightText.draw(win)
        magText.undraw()
        magText = Text(Point(580, 30), magNum)
        magText.draw(win)


main()
