from graphics import *

types = {
    1: "Converging Mirror",
    2: "Diverging Mirror",
    3: "Converging Thin Lens",
    4: "Diverging Thin Lens",
}


def main():
    mirrorLens()


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


def mirrorLens():
    print("Choose your mirror/lens: ")
    print("1: Concave/Converging Mirror")
    print("2: Convex/Diverging Mirror")
    print("3: Converging Thin Lens")
    print("4: Diverging Thin Lens")
    choice = int(input())
    win = GraphWin(types[choice], 1000, 1000)
    win.setBackground("white")
    invalText = Text(Point(500,120),"Invalid Value Inputted")
    invalText.setTextColor("red")
    if choice == 1:
        mirror = Oval(Point(500, 400), Point(600, 600))
        mirror.draw(win) 
        whiteOut = Oval(Point(525, 400), Point(600, 600))
        whiteOut.setOutline("white")
        whiteOut.setFill("white")
        whiteOut.draw(win)
    if choice == 2:
        mirror = Oval(Point(400, 400), Point(500, 600))
        mirror.draw(win) 
        whiteOut = Oval(Point(400, 400), Point(475, 600))
        whiteOut.setOutline("white")
        whiteOut.setFill("white")
        whiteOut.draw(win)
    if choice == 3:
        mirror = Oval(Point(475, 400), Point(525, 600))
        mirror.draw(win) 
    if choice == 4:
        mirror1 = Oval(Point(450, 400), Point(475, 600))
        whiteOut1 = Rectangle(Point(450,399),Point(465,599))
        mirLineTop = Line(Point(465, 400), Point(510, 400))
        mirLineBottom = Line(Point(465, 600), Point(510, 600))
        mirror2 = Oval(Point(500, 400),Point(525, 600))
        whiteOut2 = Rectangle(Point(510,399),Point(525,599))
        mirror1.draw(win)
        whiteOut1.setOutline("white")
        whiteOut1.setFill("white")
        whiteOut1.draw(win)
        mirLineTop.draw(win)
        mirLineBottom.draw(win)
        mirror2.draw(win)
        whiteOut2.setOutline("white")
        whiteOut2.setFill("white")
        whiteOut2.draw(win)
    axis = Line(Point(0, 500), Point(1000, 500))
    objDistNum = 10
    objDistBox = Rectangle(Point(5, 5), Point(105, 55))
    objDistText = Text(Point(55, 30), objDistNum)
    objDistEnter = Entry(Point(55, 30), 10)
    objDistDownBox = Rectangle(Point(5, 60), Point(55, 85))
    objDistUpBox = Rectangle(Point(55, 60), Point(105, 85))
    objDistTitle = Text(Point(55,100),"p")
    if choice == 1 or choice == 3:
        focDistNum = 30
    if choice == 2 or choice == 4:
        focDistNum = -30
    focDistBox = Rectangle(Point(215, 5), Point(315, 55))
    focDistText = Text(Point(265, 30), focDistNum)
    focDistEnter = Entry(Point(265, 30), 10)
    focDistDownBox = Rectangle(Point(215, 60), Point(265, 85))
    focDistUpBox = Rectangle(Point(265, 60), Point(315, 85))
    focDistTitle = Text(Point(265,100),"f")
    imgDistNum = (1-focDistNum) - (1-objDistNum)
    imgDistNum = round(1 / imgDistNum, 3)
    imgDistBox = Rectangle(Point(110, 5), Point(210, 55))
    imgDistText = Text(Point(160, 30), imgDistNum)
    imgDistEnter = Entry(Point(160, 30), 10)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    imgDistDownBox = Rectangle(Point(110, 60), Point(160, 85))
    imgDistUpBox = Rectangle(Point(160, 60), Point(210, 85))
    imgDistTitle = Text(Point(160,100),"q")
    objHeightNum = 5
    objHeightBox = Rectangle(Point(320, 5), Point(420, 55))
    objHeightText = Text(Point(370, 30), objHeightNum)
    objHeightEnter = Entry(Point(370, 30), 10)
    objHeightDownBox = Rectangle(Point(320, 60), Point(370, 85))
    objHeightUpBox = Rectangle(Point(370, 60), Point(420, 85))
    objHeightTitle = Text(Point(370,100),"hₒ")
    imgHeightNum = -1 * imgDistNum * objHeightNum / objDistNum
    imgHeightNum = round(imgHeightNum, 3)
    imgHeightBox = Rectangle(Point(425, 5), Point(525, 55))
    imgHeightText = Text(Point(475, 30), imgHeightNum)
    imgHeightEnter = Entry(Point(475, 30), 10)
    imgHeightDownBox = Rectangle(Point(425, 60), Point(475, 85))
    imgHeightUpBox = Rectangle(Point(475, 60), Point(525, 85))
    imgHeightTitle = Text(Point(475,100),"hᵢ")
    magNum = -1 * imgDistNum / objDistNum
    magNum = round(magNum, 3)
    magBox = Rectangle(Point(530, 5), Point(630, 55))
    magText = Text(Point(580, 30), magNum)
    magEnter = Entry(Point(580, 30), 10)
    magDownBox = Rectangle(Point(530, 60), Point(580, 85))
    magUpBox = Rectangle(Point(580, 60), Point(630, 85))
    magTitle = Text(Point(580,100), "M")
    obj = Rectangle(
        Point(500 - objDistNum * 3 - 5, 500),
        Point(500 - objDistNum * 3 + 5, 500 - objHeightNum * 3),
    )
    if choice == 1 or choice == 2:
            img = Rectangle(
            Point(500 - imgDistNum * 3 - 5, 500),
            Point(500 - imgDistNum * 3 + 5, 500 - imgHeightNum * 3),
        )
    else:
        img = Rectangle(
        Point(500 + imgDistNum * 3 - 5, 500),
        Point(500 + imgDistNum * 3 + 5, 500 - imgHeightNum * 3),
    )
    focPointLeft = Circle(Point(500 - focDistNum * 3, 500), 5)
    focPointRight = Circle(Point(500 + focDistNum * 3, 500), 5)
    marks = []
    xMark = 0
    while xMark <= 1000:
        if (choice == 1 or choice == 2) and (xMark > 500 or xMark < 500):
            marks.append(Line(Point(xMark, 490), Point(xMark, 510)))
        elif choice == 3 and (xMark<475 or xMark>525):
            marks.append(Line(Point(xMark, 490), Point(xMark, 510)))
        elif choice == 4 and (xMark<475 or xMark>500):
            marks.append(Line(Point(xMark, 490), Point(xMark, 510)))
        xMark += 10
    axis.draw(win)
    objDistBox.draw(win)
    objDistText.draw(win)
    objDistDownBox.draw(win)
    objDistDownBox.setFill("red")
    objDistUpBox.draw(win)
    objDistUpBox.setFill("green")
    objDistTitle.draw(win)
    imgDistBox.draw(win)
    imgDistText.draw(win)
    imgDistDownBox.draw(win)
    imgDistDownBox.setFill("red")
    imgDistUpBox.draw(win)
    imgDistUpBox.setFill("green")
    imgDistTitle.draw(win)
    focDistBox.draw(win)
    focDistText.draw(win)
    focDistDownBox.draw(win)
    focDistDownBox.setFill("red")
    focDistUpBox.draw(win)
    focDistUpBox.setFill("green")
    focDistTitle.draw(win)
    objHeightBox.draw(win)
    objHeightText.draw(win)
    objHeightDownBox.draw(win)
    objHeightDownBox.setFill("red")
    objHeightUpBox.draw(win)
    objHeightUpBox.setFill("green")
    objHeightTitle.setTextColor("blue")
    objHeightTitle.draw(win)
    imgHeightBox.draw(win)
    imgHeightText.draw(win)
    imgHeightDownBox.draw(win)
    imgHeightDownBox.setFill("red")
    imgHeightUpBox.draw(win)
    imgHeightUpBox.setFill("green")
    imgHeightTitle.setTextColor("red")
    imgHeightTitle.draw(win)
    magBox.draw(win)
    magText.draw(win)
    magDownBox.draw(win)
    magDownBox.setFill("red")
    magUpBox.draw(win)
    magUpBox.setFill("green")
    magTitle.draw(win)
    focPointLeft.draw(win)
    focPointLeft.setFill("black")
    focPointRight.draw(win)
    focPointRight.setFill("black")
    obj.setFill("blue")
    obj.draw(win)
    img.setFill("red")
    img.draw(win)
    for mark in marks:
        mark.draw(win)
    while True:
        click = win.getMouse()
        if pointIn(click, objDistDownBox):
            if objDistNum - 1 <= 0:
                invalText.draw(win)
                win.getMouse()
                invalText.undraw()
            else:
                objDistNum -= 1
                imgDistNum = (1 / focDistNum) - (1 / objDistNum)
                imgDistNum = 1 / imgDistNum
                focDistNum = (1 / objDistNum) + (1 / imgDistNum)
        elif pointIn(click, objDistUpBox):
            objDistNum += 1
            imgDistNum = (1 / focDistNum) - (1 / objDistNum)
            imgDistNum = 1 / imgDistNum
            focDistNum = (1 / objDistNum) + (1 / imgDistNum)
        elif pointIn(click, imgDistDownBox):
            if (1 / focDistNum) - (1 / (imgDistNum - 1) <= 0):
                invalText.draw(win)
                win.getMouse()
                invalText.undraw()
            else:
                imgDistNum -= 1
                objDistNum = (1 / focDistNum) - (1 / imgDistNum)
                objDistNum = 1 / objDistNum
                focDistNum = (1 / objDistNum) + (1 / imgDistNum)
        elif pointIn(click, imgDistUpBox):
            if (1 / focDistNum) - (1 / (imgDistNum + 1) <= 0):
                invalText.draw(win)
                win.getMouse()
                invalText.undraw()
            else:
                imgDistNum += 1
                objDistNum = (1 / focDistNum) - (1 / imgDistNum)
                objDistNum = 1 / objDistNum
                focDistNum = (1 / objDistNum) + (1 / imgDistNum)
        elif pointIn(click, focDistDownBox):
            if ((focDistNum - 1 <= 0 and (choice == 1 or choice == 3)) or (focDistNum - 1 >= 0 and (choice == 2 or choice == 4))):
                invalText.draw(win)
                win.getMouse()
                invalText.undraw()
            else:
                focDistNum -=1
                imgDistNum = (1 / focDistNum) - (1 / objDistNum)
                imgDistNum = 1 / imgDistNum
                objDistNum = (1 / focDistNum) - (1 / imgDistNum)
                objDistNum = 1 / objDistNum
        elif pointIn(click, focDistUpBox):
            if ((focDistNum + 1 <= 0 and (choice == 1 or choice == 3)) or (focDistNum + 1 >= 0 and (choice == 2 or choice == 4))):
                invalText.draw(win)
                win.getMouse()
                invalText.undraw()
            else:
                focDistNum += 1
                imgDistNum = (1 / focDistNum) - (1 / objDistNum)
                imgDistNum = 1 / imgDistNum
                objDistNum = (1 / focDistNum) - (1 / imgDistNum)
                objDistNum = 1 / objDistNum
        elif pointIn(click, objHeightDownBox):
            if objHeightNum - 1 <= 0:
                invalText.draw(win)
                win.getMouse()
                invalText.undraw()
            else:
                objHeightNum -= 1
                imgHeightNum = magNum * objHeightNum
        elif pointIn(click, objHeightUpBox):
            objHeightNum += 1
            if objHeightNum <= 0:
                objHeightNum = 1
            imgHeightNum = magNum * objHeightNum
        elif pointIn(click, imgHeightDownBox):
            if (imgHeightNum -1) / magNum <= 0 or imgHeightNum -1 == 0:
                invalText.draw(win)
                win.getMouse()
                invalText.undraw()
            else:    
                imgHeightNum -= 1
                objHeightNum = imgHeightNum / magNum
        elif pointIn(click, imgHeightUpBox):
            if (imgHeightNum +1) / magNum <= 0 or imgHeightNum + 1 == 0:
                invalText.draw(win)
                win.getMouse()
                invalText.undraw()
            else:
                imgHeightNum += 1
                objHeightNum = imgHeightNum / magNum
            if objHeightNum <= 0:
                objHeightNum = 1
                imgHeightNum = magNum * objHeightNum
        elif pointIn(click, magDownBox):
            if magNum - 1 == 0:
                invalText.draw(win)
                win.getMouse()
                invalText.undraw()
            else:
                magNum -= 1
                imgHeightNum = magNum * objHeightNum
        elif pointIn(click, magUpBox):
            if magNum + 1 == 0:
                invalText.draw(win)
                win.getMouse()
                invalText.undraw()
            else:
                magNum += 1
                imgHeightNum = magNum * objHeightNum
        elif pointIn(click, objDistBox):
            objDistText.undraw()
            objDistEnter.draw(win)
            while objDistEnter.getText() == "":
                win.checkMouse()
            win.getMouse()
            if float(objDistEnter.getText()) <= 0:
                invalText.draw(win)
                win.getMouse()
                invalText.undraw()
            else:
                objDistNum = float(objDistEnter.getText())
                imgDistNum = (1 / focDistNum) - (1 / objDistNum)
                imgDistNum = 1 / imgDistNum
                focDistNum = (1 / objDistNum) + (1 / imgDistNum)
            objDistEnter.undraw()
            objDistText.draw(win)
        elif pointIn(click, imgDistBox):
            imgDistText.undraw()
            imgDistEnter.draw(win)
            while imgDistEnter.getText() == "":
                win.checkMouse()
            win.getMouse()
            if (1 / focDistNum) - (1 / float(imgDistEnter.getText())) or float(imgDistEnter.getText()) == 0:
                invalText.draw(win)
                win.getMouse()
                invalText.undraw()
            else:
                imgDistNum = float(imgDistEnter.getText())
                objDistNum = (1 / focDistNum) - (1 / imgDistNum)
                objDistNum = 1 / objDistNum
                focDistNum = (1 / objDistNum) + (1 / imgDistNum)
            imgDistEnter.undraw()
            imgDistText.draw(win)
        elif pointIn(click, focDistBox):
            focDistText.undraw()
            focDistEnter.draw(win)
            while focDistEnter.getText() == "":
                win.checkMouse()
            win.getMouse()
            if ((float(focDistEnter.getText()) <= 0 and (choice == 1 or choice == 3)) or (float(focDistEnter.getText()) >= 0 and (choice == 2 or choice == 4))):
                invalText.draw(win)
                win.getMouse()
                invalText.undraw()
            else:
                focDistNum = float(focDistEnter.getText())
                imgDistNum = (1 / focDistNum) - (1 / objDistNum)
                imgDistNum = 1 / imgDistNum
                objDistNum = (1 / focDistNum) - (1 / imgDistNum)
                objDistNum = 1 / objDistNum
            focDistEnter.undraw()
            focDistText.draw(win)
        elif pointIn(click, objHeightBox):
            objHeightText.undraw()
            objHeightEnter.draw(win)
            while objHeightEnter.getText() == "":
                win.checkMouse()
            win.getMouse()
            if float(objHeightEnter.getText()) <= 0:
                invalText.draw(win)
                win.getMouse()
                invalText.undraw()
            else:
                objHeightNum = float(objHeightEnter.getText())
                imgHeightNum = magNum * objHeightNum
            objHeightEnter.undraw()
            objHeightText.draw(win)
        elif pointIn(click, imgHeightBox):
            imgHeightText.undraw()
            imgHeightEnter.draw(win)
            while imgHeightEnter.getText() == "":
                win.checkMouse()
            win.getMouse()
            if float(imgHeightEnter.getText()) / magNum <= 0 or float(imgHeightEnter.getText()) == 0:
                invalText.draw(win)
                win.getMouse()
                invalText.undraw()
            else:
                imgHeightNum = float(imgHeightEnter.getText())
                objHeightNum = imgHeightNum / magNum
            imgHeightEnter.undraw()
            imgHeightText.draw(win)
        elif pointIn(click, magBox):
            magText.undraw()
            magEnter.draw(win)
            while magEnter.getText() == "":
                win.checkMouse()
            win.getMouse()
            if float(magEnter.getText()) == 0:
                invalText.draw(win)
                win.getMouse()
                invalText.undraw()
            else:
                magNum = float(magEnter.getText())
                imgHeightNum = magNum * objHeightNum
            if objHeightNum <= 0:
                objHeightNum = 1
                imgHeightNum = magNum * objHeightNum
            magEnter.undraw()
            magText.draw(win)
        objDistNum = round(objDistNum, 3)
        imgDistNum = round(imgDistNum, 3)
        focDistNum = round(focDistNum, 3)
        objHeightNum = round(objHeightNum, 3)
        imgHeightNum = round(imgHeightNum, 3)
        magNum = round(magNum, 3)
        objDistText.undraw()
        objDistText = Text(Point(55, 30), objDistNum)
        objDistText.draw(win)
        objDistEnter = Entry(Point(55, 30), 10)
        imgDistText.undraw()
        imgDistText = Text(Point(160, 30), imgDistNum)
        imgDistText.draw(win)
        imgDistEnter = Entry(Point(160, 30), 10)
        focDistText.undraw()
        focDistText = Text(Point(265, 30), focDistNum)
        focDistText.draw(win)
        focDistEnter = Entry(Point(265, 30), 10)
        objHeightText.undraw()
        objHeightText = Text(Point(370, 30), objHeightNum)
        objHeightText.draw(win)
        objHeightEnter = Entry(Point(370, 30), 10)
        imgHeightText.undraw()
        imgHeightText = Text(Point(475, 30), imgHeightNum)
        imgHeightText.draw(win)
        imgHeightEnter = Entry(Point(475, 30), 10)
        magText.undraw()
        magText = Text(Point(580, 30), magNum)
        magText.draw(win)
        magEnter = Entry(Point(580, 30), 10)
        focPointLeft.undraw()
        focPointLeft = Circle(Point(500 - focDistNum * 3, 500), 5)
        focPointLeft.draw(win)
        focPointLeft.setFill("black")
        focPointRight.undraw()
        focPointRight = Circle(Point(500 + focDistNum * 3, 500), 5)
        focPointRight.draw(win)
        focPointRight.setFill("black")
        obj.undraw()
        obj = Rectangle(
        Point(500 - objDistNum * 3 - 5, 500),
        Point(500 - objDistNum * 3 + 5, 500 - objHeightNum * 3),
    )
        obj.setFill("blue")
        obj.draw(win)
        img.undraw()
        if choice == 1 or choice == 2:
            img = Rectangle(
            Point(500 - imgDistNum * 3 - 5, 500),
            Point(500 - imgDistNum * 3 + 5, 500 - imgHeightNum * 3),
        )
        else:
            img = Rectangle(
            Point(500 + imgDistNum * 3 - 5, 500),
            Point(500 + imgDistNum * 3 + 5, 500 - imgHeightNum * 3),
        )
        img.setFill("red")
        img.draw(win)


main()
