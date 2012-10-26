

from graphics import*


def isBetween(x,end1,end2):
    return end1 <=x <= end2 or end2 <=x <= end1

def isInside(point,rect):
    pt1=rect.getP1()
    pt2=rect.getP2()
    return isBetween(point.getX(),pt1.getX(), pt2.getX()) and \
           isBetween(point.getY(),pt1.getY(), pt2.getY())


def makeRect(corner,width,height,weight,element,win):
    '''Return a Rectangle drawn in win with the upper left corner and element
        name specified''' 
     
    corner2=corner.clone()
    corner2.move(width, -height)
    rect= Rectangle(corner, corner2)  
    rect.draw(win)
    return rect 

def getChoice(elementPairs,win):
    point=win.getMouse() 
    for (atom,weight,element) in elementPairs:
        if isInside(point,atom):
            return (point.x,point.y,weight,element)

         
def getEnter(newRectEnter,win2):
    point2=win2.getMouse()
    if isInside(point2,newRectEnter):
        return newRectEnter


def getQuit(quitBox,win2):
    point=win2.getMouse()
    if isInside(point, quitBox):
        return quitBox

def mainQuit(qMain,win):
    point3=win.getMouse()
    if isInside(point3, qMain):
        return qMain

def main():

    win=GraphWin('Periodic Table of Elements', 700, 700)
    win.yUp()

    rectTitle=Rectangle(Point(5,660), Point(695,630))
    rectTitle.draw(win)
    title= Text(Point(350,640), 'Periodic Table of Elements.')
    title.draw(win) 

    elementPairs=list()
    elementSetup=[(8,580, 1.008, 'H'), (654,580, 4.003, 'He'), \
                  (8,542, 6.95, 'Li'), (8,504, 22.99, 'Na'), (8,466,39.10, 'K'), \
                  (8, 428, 85.47, 'Rb'), (8,390, 132.91, 'Cs'), (8, 352, 223, 'Fr'), \
                  (84,276,138.9,'La'), (84,238,227,'Ac'), (46, 542, 9.01, 'Be'), \
                  (46, 504, 24.31, 'Mg'), (46, 466, 40.08, 'Ca'), (46,428, 87.62, 'Sr'), \
                  (46, 390, 137.3, 'Ba'), (46, 352, 226, 'Ra'), (84, 466, 44.96, 'Sc'),\
                  (84, 428, 88.91, 'Y'), (122, 466, 47.88, 'Ti'), (122, 428, 91.22, 'Zr'),\
                  (122, 390, 178.5, 'Hf'), (122, 352, 257, 'Rf'), (160,466, 50.94, 'V'),\
                  (160,428, 92.91, 'Nb'), (160, 390, 180.9, 'Ta'), (160, 352, 260, 'Db'),\
                  (160, 276, 140.91, 'Pr'), (160, 238, 231.03, 'Pa'), (122, 276, 140.1, 'Ce'),\
                  (122, 238, 232, 'Th'), (198, 466, 52.00, 'Cr'), (198,428, 95.94, 'Mo'), \
                  (198, 390, 183.9, 'W'), (198, 352, 263, 'Sg'), (198, 276, 144.2, 'Nd'), \
                  (198, 238, 238, 'U'), (236, 466, 54.94, 'Mn'), (236, 428, 98, 'Tc'), \
                  (236, 390, 186.2, 'Re'), (236, 352, 265, 'Bh'), (236, 276, 147, 'Pm'), \
                  (236, 238, 237, 'Np'),(274, 466, 55.85, 'Fe'), (274, 428, 101.1, 'Ru'), \
                  (274, 390, 190.2, 'Os'), (274, 352, 265, 'Hs'), (274, 276, 150.4, 'Sm'), \
                  (274, 238, 242, 'Pu'), (312, 466, 58.47, 'Co'), (312, 428, 102.91, 'Rh'), \
                  (312, 390, 190.2, 'Ir'), (312, 352, 266, 'Mt'), (312,276,152, 'Eu'),\
                  (312,238,243, 'Am'), (350,466, 58.69, 'Ni'), (350,428,106.4,'Pd'),\
                  (350,390,195.1,'Pt'),(350,352,271,'Ds'),(350,276,157.3,'Gd'),\
                  (350,238,247,'Cm'),(388,466,63.55,'Cu'),(388,428,107.9,'Ag'),\
                  (388,390,197.0,'Au'),(388,352,272,'Rg'),(388,276,158.9,'Tb'),\
                  (388,238,247,'Bk'),(426,466,65.39,'Zn'),(426,428,112.4,'Cd'),\
                  (426,390,200.5,'Hg'),(426,352,277,'Cn'),(426,276,162.5,'Dy'),\
                  (426,238,249,'Cf'),(464,542,10.81,'B'),(464,504,26.98,'Al'),\
                  (464,466,69.72,'Ga'),(464,428,114.8,'In'),(464,390,204.4,'Ti'),\
                  (464,352,284,'Uut'),(464,276,164.9,'Ho'),(464,238,254,'Es'),\
                  (502,542,12.01,'C'),(502,504,28.09,'Si'),(502,466,72.59,'Ge'),\
                  (502,428,118.7,'Sn'),(502,390,207.2,'Pb'),(502,352,296,'Uuq'),\
                  (502,276,167.3,'Er'),(502,238,253,'Fm'),(540,542,14.01,'N'),\
                  (540,504,30.97,'P'),(540,466,74.92,'As'),(540,428,121.8,'Sb'),\
                  (540,390,209,'Bi'),(540,352,288,'Uup'),(540,276,168.9,'Tm'),\
                  (540,238,256,'Md'),(578,542,16,'O'),(578,504,32.07,'S'),\
                  (578,466,78.96,'Se'),(578,428,127.6,'Te'),(578,390,210,'Po'),\
                  (578,352,298,'Uuh'),(578,276,173,'Yb'),(578,238,254,'No'),\
                  (616,542,19,'F'),(616,504,35.45,'Cl'),(616,466,79.90,'Br'),\
                  (616,428,126.9,'I'),(616,390,210,'At'),(616,352,0,'Uus'),\
                  (616,276,175,'Lu'),(616,238,257,'Lr'),(654,542,20.18,'Ne'),\
                  (654,504,39.95,'Ar'),(654,466, 83.80,'Kr'),(654,428,131.3,'Xe'),\
                  (654,390,222,'Rn'), (654,352,293,'Uuo')]

    clickElements=Text(Point(win.width/2.5,600), 'Click an element to get the moles.')
    clickElements.draw(win)

    clickQ=Text(Point(win.width/2,40), 'Click Quit to quit')
    clickQ.draw(win)

    qMain=Rectangle(Point(640,670), Point(695,695))
    qMain.draw(win)
    qText=Text(Point(665,680), 'Quit')
    qText.draw(win)

    
    for(x,y,weight,element) in elementSetup:

        atom=makeRect(Point(x,y), 38,38,weight,element,win)
        elementPairs.append((atom,weight,element))

        element=Text(Point(x+18,y-18),element)
        element.draw(win) 
 

    while (getChoice(elementPairs,win)):
        
        for (x,y,weight,element1) in [getChoice(elementPairs,win)]:
            win2=GraphWin('Periodic Table of Elements',400,400)
            win2.yUp()
            newRectTitle=Rectangle(Point(5,360), Point(395,330))
            newRectTitle.draw(win2)

            quitBox=Rectangle(Point(350,375), Point(395,395))
            quitBox.draw(win2)

            quitTitle=Text(Point(375,385), 'Quit.')
            quitTitle.draw(win2) 
                              

             
            se=Text(Point(win2.width/1.7,140),'Element: '+element1)
            se.draw(win2)
           

            
            strweight=str(weight) 
            eweight=Text(Point(win2.width/1.7,120),'Atomic Weight: '+strweight)
            eweight.draw(win2)
            molarityformula=Text(Point(win2.width/1.7,100),'Moles = Grams/Atomic Weight')
            molarityformula.draw(win2) 

            
            newTitle=Text(Point(200,345), 'Enter the number of grams.')
            newTitle.draw(win2) 

            ent=Entry(Point(200,200), 40)
            ent.draw(win2)

            grams=ent.getText()

            
            newRectEnter=Rectangle(Point(17,170), Point(70,150))
            newRectEnter.draw(win2)
            newRectEnterText=Text(Point(42,160), 'Enter')
            newRectEnterText.draw(win2)

            message=Text(Point(win2.width/2,20),'Click Enter to submit grams')
            message.draw(win2)

                            
            enterchoice=[getEnter(newRectEnter,win2)]
            for rectangle2 in enterchoice: 
                if grams.isdigit()==True:
                    grams1=float(ent.getText())
                    molescalc=grams1/weight
                    mls=format(molescalc, '.2f')
                    moles='{} moles.'.format(mls)
                    mc=Text(Point(win2.width/1.7,80),moles)
                    mc.draw(win2)


                else:
                    grams1=float(ent.getText())
                    molescalc=grams1/weight
                    mls=format(molescalc, '.2f')
                    moles='{} moles.'.format(mls)
            
                    mc=Text(Point(win2.width/1.7,80),moles)
                    mc.draw(win2)

            enterquitchoice=[getQuit(quitBox,win2)]
            for rectangle3 in enterquitchoice:
                win2.close()

    
        
    
    for rectangle4 in [mainQuit(qMain,win)]:
        win.close()

    
main() 
