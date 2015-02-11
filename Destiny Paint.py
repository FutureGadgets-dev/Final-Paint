#Paint Program
#Ahmad Kashash

from pygame import*
from math import*
from random import*

import tkinter.filedialog
import tkinter 

root = tkinter.Tk()
root.withdraw()

screen=display.set_mode((1024,640))

init()

#Font---------------------------------------------

font.init()
centuryfont= font.SysFont("Century Gothic",23)
centuryfont2= font.SysFont("Century Gothic",70)
centuryfont3=font.SysFont("Century Gothic",18)
centuryfont4=font.SysFont("Century Gothic",16)

#Images-------------------------------------------

startScreen = image.load("Images\Wallpapers\Destiny City Start Screen.jpg")
startScreen = transform.scale(startScreen,(1024,640))
background= image.load("Images\Wallpapers\Destiny Background.jpg")    
background= transform.scale(background,(1024,640))
screen.blit (startScreen,(0,0))

#Stickers-----------------------------------------

Titan1=image.load("Images/Png Photoes/Destiny Titan 2.png")
Titan2=image.load("Images/Png Photoes/Destiny Titan 3.png")
Warlock1=image.load("Images/Png Photoes/Warlock.png")
Warlock2=image.load("Images/Png Photoes/Destiny Warlocks.png")
Hunter1=image.load("Images/Png Photoes/Hunter.png")
Hunter2=image.load("Images/Png Photoes/Destiny Hunters.png")

Fallen1=image.load("Images/Png Photoes/Destiny The Fallen 3.png")
Fallen2=image.load("Images/Png Photoes/Destiny The Fallen 4.png")
Fallen3=image.load("Images/Png Photoes/Destiny The Fallen 3.png")
Fallen4=image.load("Images/Png Photoes/Destiny The Fallen 6.png")
Vex1=image.load("Images/Png Photoes/Destiny Vex 2.png")
Vex2=image.load("Images/Png Photoes/Destiny Vex 3.png")
Hive1=image.load("Images/Png Photoes/Destiny The Hive 3.png")
Hive2=image.load("Images/Png Photoes/Destiny The Hive 4.png")
Hive3=image.load("Images/Png Photoes/Destiny The Hive 5.png")
Hive4=image.load("Images/Png Photoes/Destiny The Hive 6.png")
Hive5=image.load("Images/Png Photoes/Destiny The Hive 7.png")
Cabal1=image.load("Images/Png Photoes/Destiny Cabal 2.png")
Cabal2=image.load("Images/Png Photoes/Destiny Cabal 3.png")

#Small Stickers-----------------------------------

Titan1small=image.load("Images/Png Photoes/Destiny Titan 2 small.png")
Titan2small=image.load("Images/Png Photoes/Destiny Titan 3 small.png")
Warlock1small=image.load("Images/Png Photoes/Warlock small.png")
Warlock2small=image.load("Images/Png Photoes/Destiny Warlocks small.png")
Hunter1small=image.load("Images/Png Photoes/Hunter small.png")
Hunter2small=image.load("Images/Png Photoes/Destiny Hunters small.png")

Fallen1small=image.load("Images/Png Photoes/Destiny The Fallen 3 small.png")
Fallen2small=image.load("Images/Png Photoes/Destiny The Fallen 4 small.png")
Fallen3small=image.load("Images/Png Photoes/Destiny The Fallen 5 small.png")
Fallen4small=image.load("Images/Png Photoes/Destiny The Fallen 6 small.png")
Vex1small=image.load("Images/Png Photoes/Destiny Vex 2 small.png")
Vex2small=image.load("Images/Png Photoes/Destiny Vex 3 small.png")
Hive1small=image.load("Images/Png Photoes/Destiny The Hive 3 small.png")
Hive2small=image.load("Images/Png Photoes/Destiny The Hive 4 small.png")
Hive3small=image.load("Images/Png Photoes/Destiny The Hive 5 small.png")
Hive4small=image.load("Images/Png Photoes/Destiny The Hive 6 small.png")
Hive5small=image.load("Images/Png Photoes/Destiny The Hive 7 small.png")
Cabal1small=image.load("Images/Png Photoes/Destiny Cabal 2 small.png")
Cabal2small=image.load("Images/Png Photoes/Destiny Cabal 3 small.png")

#Wallpapers---------------------------------------

Wallpaper1=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 1.jpg")
Wallpaper2=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 2.jpg")
Wallpaper3=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 3.jpg")
Wallpaper4=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 4.jpg")
Wallpaper5=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 5.jpg")
Wallpaper6=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 6.jpg")
Wallpaper7=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 7.jpg")
Wallpaper8=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 8.jpg")
Wallpaper9=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 9.jpg")
Wallpaper10=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 10.jpg")
Wallpaper11=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 11.jpg")
Wallpaper12=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 12.jpg")
Wallpaper13=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 13.jpg")
Wallpaper14=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 14.jpg")
Wallpaper15=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 15.jpg")
Wallpaper16=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 16.jpg")
Wallpaper17=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 17.jpg")
Wallpaper18=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 18.jpg")

#Small Wallpapers---------------------------------

Wallpaper1small=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 1 small.jpg")
Wallpaper2small=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 2 small.jpg")
Wallpaper3small=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 3 small.jpg")
Wallpaper4small=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 4 small.jpg")
Wallpaper5small=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 5 small.jpg")
Wallpaper6small=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 6 small.jpg")
Wallpaper7small=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 7 small.jpg")
Wallpaper8small=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 8 small.jpg")
Wallpaper9small=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 9 small.jpg")
Wallpaper10small=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 10 small.jpg")
Wallpaper11small=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 11 small.jpg")
Wallpaper12small=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 12 small.jpg")
Wallpaper13small=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 13 small.jpg")
Wallpaper14small=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 14 small.jpg")
Wallpaper15small=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 15 small.jpg")
Wallpaper16small=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 16 small.jpg")
Wallpaper17small=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 17 small.jpg")
Wallpaper18small=image.load("Images/Wallpapers/Choosable Wallpaper/Destiny Wallpaper 18 small.jpg")

#Wallpaper Rects----------------------------------

wallRect1=Rect(496,507,153,96)
wallRect2=Rect(649,507,153,96)
wallRect3=Rect(802,507,153,96)
wallRect4=Rect(496,620,153,96)
wallRect5=Rect(649,620,153,96)
wallRect6=Rect(802,620,153,96)
wallRect7=Rect(496,733,153,96)
wallRect8=Rect(649,733,153,96)
wallRect9=Rect(802,733,153,96)
wallRect10=Rect(496,846,153,96)
wallRect11=Rect(649,846,153,96)
wallRect12=Rect(802,846,153,96)
wallRect13=Rect(496,959,153,96)
wallRect14=Rect(649,959,153,96)
wallRect15=Rect(802,959,153,96)
wallRect16=Rect(496,1072,153,96)
wallRect17=Rect(649,1072,153,96)
wallRect18=Rect(802,1072,153,96)

wallRectlist=[wallRect1,wallRect2,wallRect3,wallRect4,wallRect5,
              wallRect6,wallRect7,wallRect8,wallRect9,wallRect10,
              wallRect11,wallRect12,wallRect13,wallRect14,wallRect15,
              wallRect16,wallRect17,wallRect18]

#Sticker Lists------------------------------------

titanlist=[Titan1,Titan2]
warlocklist=[Warlock1,Warlock2]
hunterlist=[Hunter1,Hunter2]

fallenlist=[Fallen1,Fallen2,Fallen3,Fallen4]
vexlist=[Vex1,Vex2]
hivelist=[Hive1,Hive2,Hive3,Hive4,Hive5]
caballist=[Cabal1,Cabal2]


tpreviewlist=[Titan1small,Titan2small]
wpreviewlist=[Warlock1small,Warlock2small]
hupreviewlist=[Hunter1small,Hunter2small]

fpreviewlist=[Fallen1small,Fallen2small,Fallen3small,Fallen4small]
vpreviewlist=[Vex1small,Vex2small]
hipreviewlist=[Hive1small,Hive2small,Hive3small,Hive4small,Hive5small]
cpreviewlist=[Cabal1small,Cabal2small]

wallpaperlist=[Wallpaper1,Wallpaper2,Wallpaper3,Wallpaper4,Wallpaper5,
               Wallpaper6,Wallpaper7,Wallpaper8,Wallpaper9,Wallpaper10,
               Wallpaper11,Wallpaper12,Wallpaper13,Wallpaper14,
               Wallpaper15,Wallpaper16,Wallpaper17,Wallpaper18]

wallpaperlistsmall=[Wallpaper1small,Wallpaper2small,Wallpaper3small,
                    Wallpaper4small,Wallpaper5small,Wallpaper6small,
                    Wallpaper7small,Wallpaper8small,Wallpaper9small,
                    Wallpaper10small,Wallpaper11small,Wallpaper12small,
                    Wallpaper13small,Wallpaper14small,Wallpaper15small,
                    Wallpaper16small,Wallpaper17small,Wallpaper18small]

tcounter=0
wcounter=0
hucounter=0
fcounter=0
vcounter=0
hicounter=0
ccounter=0

#Sticker Rects------------------------------------

titansmall=image.load("Images/Heroes/Destiny Titan Wallpaper small.jpg")
warlocksmall=image.load("Images/Heroes/Destiny Warlock Wallpaper small.jpg")
huntersmall=image.load("Images/Heroes/Destiny Hunter Wallpaper small.jpg")

fallensmall=image.load("Images/Enemies/Destiny The Fallen 6.png")
cabalsmall=image.load("Images/Enemies/Destiny Cabal 4.png")
vexsmall=image.load("Images/Enemies/Destiny Vex 3.png")
hivesmall=image.load("Images/Enemies/Destiny Hive 2.png")

white=((255,255,255))
grey=((111,111,111))

slocRect=Rect(300,465,660,170)
stickerboxRect=Rect(485,490,470,130)

heroesRect=Rect(305,470,160,50)
enemiesRect=Rect(305,520,160,50)
wallpaperRect=Rect(305,570,160,50)

sTab1=Rect(485,470,100,20)
sTab2=Rect(587,470,100,20)
sTab3=Rect(689,470,100,20)
sTab4=Rect(791,470,100,20)

##scloseRect=Rect(420,465,20,8)
##smaxRect=Rect(400,465,20,8)
##sminRect=Rect(380,465,20,8)

stickerposRect=Rect(675,495,90,130)

heroeswordg=centuryfont3.render(("Heroes"),True,grey)
enemieswordg=centuryfont3.render(("Enemies"),True,grey)
wallpaperwordg=centuryfont3.render(("Wallpapers"),True,grey)

heroeswordw=centuryfont3.render(("Heroes"),True,white)
enemieswordw=centuryfont3.render(("Enemies"),True,white)
wallpaperwordw=centuryfont3.render(("Wallpapers"),True,white)

twordg=centuryfont4.render(("Titans"),True,grey)
wwordg=centuryfont4.render(("Warlock"),True,grey)
huwordg=centuryfont4.render(("Hunter"),True,grey)

twordw=centuryfont4.render(("Titans"),True,white)
wwordw=centuryfont4.render(("Warlock"),True,white)
huwordw=centuryfont4.render(("Hunter"),True,white)

fwordg=centuryfont4.render(("Fallen"),True,grey)
vwordg=centuryfont4.render(("Vex"),True,grey)
hiwordg=centuryfont4.render(("Hive"),True,grey)
cwordg=centuryfont4.render(("Cabal"),True,grey)

fwordw=centuryfont4.render(("Fallen"),True,white)
vwordw=centuryfont4.render(("Vex"),True,white)
hiwordw=centuryfont4.render(("Hive"),True,white)
cwordw=centuryfont4.render(("Cabal"),True,white)

wallword=centuryfont4.render(("Wallpaper"),True,grey)

#Random-------------------------------------------

blackscreen=image.load("Images\Win3x_Black_Screen_of_Death.gif")
blackscreen=transform.scale(blackscreen,(1024,640))
blackscreen.set_alpha(55)
whitescreen=image.load("Images\whitescreen-300x300.jpg")
whitescreen=transform.scale(whitescreen,(347,190))
blueback=image.load("Images/blue screen.jpg")
blueback=transform.scale(blueback,(660,420))

mx,my=mouse.get_pos()

c1=174
c=3

size=10
sizeE=size

sizepos=0

slider=image.load("Images\whitescreen-300x300.jpg")
slider=transform.scale(slider,(200,50))
sizeRect=Rect(28,403,44,44)
ssliderbutton=image.load("Images\Icons\Sizeslider.jpg")

rcolpos=0
gcolpos=0
bcolpos=0

colsetRect=Rect(347.5,235,347,190)
rsliderRect=Rect(350.5,238,44,44)
gsliderRect=Rect(350.5,298,44,44)
bsliderRect=Rect(350.5,358,44,44)

colsetRectcopy=Rect(347.5,235,307,190)

bsliderbutton=image.load("Images\Icons\Sizeslider.jpg")
rsliderbutton=image.load("Images\Icons\\red slider button.jpg")
gsliderbutton=image.load("images\Icons\green slider button.jpg")

#Words--------------------------------------------

Destiny=centuryfont2.render(("Destiny"),True,(255,255,255))
Paint=centuryfont2.render(("Paint"),True,(255,255,255))

#Buttons------------------------------------------
#-------------------------------------------------

filebutton=image.load("Images\Icons\File.jpg")
editbutton=image.load("Images\Icons\Edit.jpg")
toolsbutton=image.load("Images\Icons\Tools.jpg")
stickersbutton=image.load("Images\Icons\Stickers.jpg")
helpbutton=image.load("Images\Icons\Help.jpg")

fileRect=Rect(25,40,200,50)
editRect=Rect(25,100,200,50)
toolsRect=Rect(25,160,200,50)
stickersRect=Rect(25,220,200,50)
helpRect=Rect(25,280,200,50)

newbutton=image.load("Images/Icons/New.jpg")
openbutton=image.load("Images\Icons\Open.jpg")
savebutton=image.load("Images\Icons\Save As.jpg")

newRect=Rect(25,40,200,50)

newybutton=image.load("Images\Icons\Check.png")
newnbutton=image.load("Images\Icons\XcloseX.png")
back=newnbutton

newRecty=Rect(227,42,21,21)
newRectn=Rect(227,67,21,21)

openRect=Rect(25,100,200,50)
saveRect=Rect(25,160,200,50)

undobutton=image.load("Images/Icons/Undo.jpg")
redobutton=image.load("Images\Icons\Redo.jpg")
cutbutton=image.load("Images\Icons\Cut.jpg")
copybutton=image.load("Images\Icons\Copy.jpg")
pastebutton=image.load("Images\Icons\Paste.jpg")

undoRect=Rect(25,40,200,50)
redoRect=Rect(25,100,200,50)

arrowbuttonleft=image.load("Images/Icons/arrow icon left.png")
arrowRectleft=Rect(492.5,535,30,30)
arrowbuttonright=image.load("Images/Icons/arrow icon right.png")
arrowRectright=Rect(917.5,535,30,30)

#Tool Images--------------------------------------

penciltool=image.load("Images/Icons/Pen.jpg")

erasertool=image.load("Images/Icons/Eraser.jpg")

brushtool=image.load("Images/Icons/Brush.jpg")

spraytool=image.load("Images/Icons/Spray.jpg")
                           
shapestool=image.load("Images/Icons/Shapes.jpg")

shapestool2=image.load("Images/Icons/Shapes Detailed.jpg")

filltool=image.load("Images/Icons/Bucket.jpg")

#Tools--------------------------------------------

canvasRect=Rect(310,45,640,390)
topcanvasRect=Rect(300,25,660,20)
resizeRect=Rect(950,435,10,10)

pencilRect=Rect(25,40,200,50)
eraserRect=Rect(25,100,200,50)
brushRect=Rect(25,160,200,50)
sprayRect=Rect(25,220,200,50)

shapesRect=Rect(25,280,200,50)
ellipseRect=Rect(36,292,27,27)
lineRect=Rect(68,292,26,27)
rectRect=Rect(102,294,36,24)
inverseRect=Rect(146,289,33,35)
polygonRect=Rect(188,289,28,32)

fillRect=Rect(25,340,200,50)

tool="pencil"

#Fill Function------------------------------------

def floodfill(x,y,oldColor,newColor):
    listfill = [(mx,my)]
    if oldColor==newColor:return
    while len(listfill)>0:
        x,y = listfill.pop()
        if screen.get_at((x,y))==oldColor:
            screen.set_at((x,y),newColor)
            listfill+=[(x+1,y), (x-1,y),(x,y+1),(x,y-1)]

def invertcol(rect):
    for x in range(rect.get_width()):
        for y in range(rect.get_height()):
            RGBA = rect.get_at((x,y))
            for i in range(3):
                # Invert RGB, but not Alpha
                RGBA[i] = 255 - RGBA[i]
            rect.set_at((x,y),RGBA)
    
#-------------------------------------------------
#-------------------------------------------------

#SidePanel----------------------------------------

sidepanel=image.load("Images\whitescreen-300x300.jpg")
canvas=image.load("Images\whitescreen-300x300.jpg")

sidepanel.set_alpha(55)
sidepanel=transform.scale(sidepanel,(250,640))

closepanel=image.load("Images\Icons\Close Panel.png")
openpanel=image.load("Images\Icons\Open Panel.png")
closepanelRect=Rect(0,0,20,20)

canvas=transform.scale(canvas,(640,390))

backRect=Rect(230,0,20,20)

#Color Wheel--------------------------------------

colorwheel = image.load("Images\ColorWheel2.jpg")
colorwheel = transform.scale(colorwheel,(130,120))
wheel=Rect(20,460,135,120)
rcol=0
gcol=0
bcol=0
col=((rcol,gcol,bcol))

#Start Screen-------------------------------------

mixer.music.load("Music/Destiny OST - 1  &quot;Glimmer of Hope&quot; HD.mp3")
mixer.music.play(-1)
run=True
while run:
    for evt in event.get():
        if evt.type ==QUIT:
            run=False
    keys=key.get_pressed()
    
    start=centuryfont.render(("Press Enter"),True,(c1,c1,c1))
    screen.blit (startScreen,(0,0))
    screen.blit(Destiny,(512-Destiny.get_width()/2,160-Destiny.get_height()/2))
    screen.blit(Paint,(512-Paint.get_width()/2,240-Paint.get_height()/2))
    screen.blit(start,(512-start.get_width()/2,450-start.get_height()/2))
    firstcopy=screen.copy()
    c1+=c
    if c1>=255:
        c*=-1
    if c1<=174:
        c*=-1
    if keys[K_RETURN]==1:                
        run=False
    display.flip()
mixer.music.fadeout(100)

colbuttonRect=Rect(157,566,14,14)

#Flag--------------------------------------------

menubuttons=True
filebuttons=False
editbuttons=False
toolbuttons=False
stickerbuttons=False
helpbuttons=False

shapesbutton=False

newbuttons=False

panelbutton=True

colorslider=False

heroesbutton=False
enemiesbutton=False
wallpapersbutton=False

titanbutton=False
warlockbutton=False
hunterbutton=False

fallenbutton=False
vexbutton=False
hivebutton=False
cabalbutton=False

inverse=False

cutcopy=False

motion=False

#Paint Program-----------------------------------

for i in range (255,1,-2):
    screen.fill(0)
    firstcopy.set_alpha(i)
    screen.blit(firstcopy,(0,0))
    display.flip()

mixer.music.load("Music/Destiny OST - -Reveal-.mp3")
mixer.music.play(-1)

for i in range(-250,1,10):
    screen.blit(background,(0,0))

    x=i+25

    screen.blit(sidepanel,(i,0))
    screen.blit(blueback,(canvasRect.x-10,canvasRect.y-20))
    screen.blit(canvas,canvasRect)
    screen.blit(filebutton,(x,40))
    screen.blit(editbutton,(x,100))
    screen.blit(toolsbutton,(x,160))
    screen.blit(stickersbutton,(x,220))
    screen.blit(helpbutton,(x,280))
    screen.blit(closepanel,(0,0))
    display.flip()

maker=centuryfont3.render(("Done By: Ahmad Kashash"),True,(255,255,255))
maker2=centuryfont3.render(("Helpful, Right? :)"),True,(255,255,255))

undo=[screen.subsurface(canvasRect).copy()]
redo=[]
end=False

polygonlist=[]

myClock=time.Clock()

inverse=False
click=0

running=True   
while running:
    for evt in event.get():
        if evt.type ==QUIT:
            running=False
        if evt.type==MOUSEMOTION:
            if evt.buttons[0] and topcanvasRect.collidepoint(mx,my):
                rel = evt.rel
                topcanvasRect.x += rel[0]
                topcanvasRect.y += rel[1]
                resizeRect.x += rel[0]
                resizeRect.y += rel[1]
                canvasRect.x+=rel[0]
                canvasRect.y+=rel[1]
                screen.blit(background,(0,0))
                if stickerbuttons==True:
                    screen.blit(sscopy,(300,465))
                if panelbutton==True:
                    screen.blit(sidepanel,(0,0))
                    screen.blit(filebutton,(25,40))
                    screen.blit(editbutton,(25,100))
                    screen.blit(toolsbutton,(25,160))
                    screen.blit(stickersbutton,(25,220))
                    screen.blit(helpbutton,(25,280))
                screen.blit(openpanel,(0,0))
                screen.blit(blueback,(canvasRect.x-10,canvasRect.y-20))
                screen.blit(undo[-1],canvasRect)
                menubuttons=False
                filebuttons=False
                editbuttons=False
                toolbuttons=False
                helpbuttons=False
                motion=True
                if canvasRect.x<0:
                    topcanvasRect.x=-10
                    canvasRect.x=0
                    resizeRect.x=canvas.get_width()
                if int(canvas.get_width()+canvasRect.x)>1024: 
                    topcanvasRect.x=1024-(canvas.get_width()+10)
                    canvasRect.x=1024-canvas.get_width()
                    resizeRect.x=1024
                if int(canvas.get_height()+canvasRect.y)>640:
                    topcanvasRect.y=640-(canvas.get_height()+20)
                    canvasRect.y=640-canvas.get_height()
                    resizeRect.y=640

        if evt.type==MOUSEBUTTONDOWN:
            click=1
            copy=screen.copy()
            canvascopy=screen.subsurface(canvasRect).copy()
            
            if evt.button==1:
                oldmx,oldmy=evt.pos

            if closepanelRect.collidepoint(mx,my) and click==1 and panelbutton==True:
                for i in range(0,-251,-50):
                    screen.blit(background,(0,0))
                    screen.blit(blueback,(canvasRect.x-10,canvasRect.y-20))
                    screen.blit(undo[-1],canvasRect)
                    screen.blit(sidepanel,(i,0))
                    screen.blit(openpanel,(0,0))
                    panelbutton=False
                    menubuttons=False
                    filebuttons=False
                    editbuttons=False
                    toolbuttons=False
                    if stickerbuttons==True:
                        screen.blit(sscopy,(300,465))
                    display.flip()
            elif closepanelRect.collidepoint(mx,my) and click==1 and panelbutton==False:
                for i in range(-250,1,50):
                    screen.blit(background,(0,0))
                    screen.blit(blueback,(canvasRect.x-10,canvasRect.y-20))
                    screen.blit(undo[-1],canvasRect)
                    screen.blit(sidepanel,(i,0))
                    screen.blit(openpanel,(0,0))
                    panelbutton=True
                    menubuttons=True
                    if stickerbuttons==True:
                        screen.blit(sscopy,(300,465))
                    display.flip()
                screen.blit(blueback,(canvasRect.x-10,canvasRect.y-20))
                screen.blit(undo[-1],canvasRect)
                screen.blit(filebutton,(25,40))
                screen.blit(editbutton,(25,100))
                screen.blit(toolsbutton,(25,160))
                screen.blit(stickersbutton,(25,220))
                screen.blit(helpbutton,(25,280))
                screen.blit(closepanel,(0,0))
                
            if evt.button == 1:
                if undoRect.collidepoint(mx,my) and len(undo) > 1 and editbuttons==True: 
                    redo.append(undo[-1]) 
                    undo = undo[:-1]
                    screen.blit(undo[-1],canvasRect)
                    if len(polygonlist)>1:
                        del polygonlist[-1]
                if redoRect.collidepoint(mx,my) and len(redo) > 0 and editbuttons==True: 
                    undo.append(redo[-1]) 
                    redo = redo[:-1]
                    screen.blit(blueback,(canvasRect.x-10,canvasRect.y-20))
                    screen.blit(undo[-1],canvasRect)

            if wallpapersbutton==True and stickerboxRect.collidepoint(mx,my):
                screen.set_clip(stickerboxRect)
                if evt.button==5 and wallRect18.y>=515:
                    wallRect1.y-=15
                    wallRect2.y-=15
                    wallRect3.y-=15
                    wallRect4.y-=15
                    wallRect5.y-=15
                    wallRect6.y-=15
                    wallRect7.y-=15
                    wallRect8.y-=15
                    wallRect9.y-=15
                    wallRect10.y-=15
                    wallRect11.y-=15
                    wallRect12.y-=15
                    wallRect13.y-=15
                    wallRect14.y-=15
                    wallRect15.y-=15
                    wallRect16.y-=15
                    wallRect17.y-=15
                    wallRect18.y-=15   
                if evt.button==4 and wallRect1.y<=500:
                    wallRect1.y+=15
                    wallRect2.y+=15
                    wallRect3.y+=15
                    wallRect4.y+=15
                    wallRect5.y+=15
                    wallRect6.y+=15
                    wallRect7.y+=15
                    wallRect8.y+=15
                    wallRect9.y+=15
                    wallRect10.y+=15
                    wallRect11.y+=15
                    wallRect12.y+=15
                    wallRect13.y+=15
                    wallRect14.y+=15
                    wallRect15.y+=15
                    wallRect16.y+=15
                    wallRect17.y+=15
                    wallRect18.y+=15
                draw.rect(screen,(white),(485,490,470,130))
                screen.blit(wallpaperlistsmall[0],(wallRect1.x,wallRect1.y))
                screen.blit(wallpaperlistsmall[1],(wallRect2.x,wallRect2.y))
                screen.blit(wallpaperlistsmall[2],(wallRect3.x,wallRect3.y))
                screen.blit(wallpaperlistsmall[3],(wallRect4.x,wallRect4.y))
                screen.blit(wallpaperlistsmall[4],(wallRect5.x,wallRect5.y))
                screen.blit(wallpaperlistsmall[5],(wallRect6.x,wallRect6.y))
                screen.blit(wallpaperlistsmall[6],(wallRect7.x,wallRect7.y))
                screen.blit(wallpaperlistsmall[7],(wallRect8.x,wallRect8.y))
                screen.blit(wallpaperlistsmall[8],(wallRect9.x,wallRect9.y))
                screen.blit(wallpaperlistsmall[9],(wallRect10.x,wallRect10.y))
                screen.blit(wallpaperlistsmall[10],(wallRect11.x,wallRect11.y))
                screen.blit(wallpaperlistsmall[11],(wallRect12.x,wallRect12.y))
                screen.blit(wallpaperlistsmall[12],(wallRect13.x,wallRect13.y))
                screen.blit(wallpaperlistsmall[13],(wallRect14.x,wallRect14.y))
                screen.blit(wallpaperlistsmall[14],(wallRect15.x,wallRect15.y))
                screen.blit(wallpaperlistsmall[15],(wallRect16.x,wallRect16.y))
                screen.blit(wallpaperlistsmall[16],(wallRect17.x,wallRect17.y))
                screen.blit(wallpaperlistsmall[17],(wallRect18.x,wallRect18.y))

        if evt.type == MOUSEBUTTONUP:
            click=0
            end = True
            if motion==True:
                if panelbutton==True:
                    menubuttons=True
                motion=False
            if evt.button == 1 and canvasRect.collidepoint(mx,my) and colorslider==False : 
                undo.append(screen.subsurface(canvasRect).copy())
            
    size=max(0,size)
    keys=key.get_pressed()

#Mouse Stuff-------------------------------------

    omx,omy=mx,my
    mx,my=mouse.get_pos()
    dist=max(1,hypot(mx-omx,my-omy))
    sx=(mx-omx)/dist
    sy=(my-omy)/dist
    mb=mouse.get_pressed()
    
#Buttons-----------------------------------------
    if click==1 and resizeRect.collidepoint(mx,my):
        canx=canvasRect.x
        cany=canvasRect.y
        topcanvasRect=Rect(canx-10,cany-20,(mx-canx)+20,20)
        canvasRect=Rect(canx,cany,(mx-canx)-5,(my-cany)-5)
        resizeRect=Rect(mx-5,my-5,10,10)
        blueback=transform.scale(blueback,((mx-canx)+15,(my-cany)+25))
        canvas=transform.scale(undo[-1],((mx-canx)-5,(my-cany)-5))
        screen.blit(background,(0,0))
        if stickerbuttons==True:
            screen.blit(sscopy,(300,465))
        screen.blit(sidepanel,(0,0))
        screen.blit(filebutton,(25,40))
        screen.blit(editbutton,(25,100))
        screen.blit(toolsbutton,(25,160))
        screen.blit(stickersbutton,(25,220))
        screen.blit(helpbutton,(25,280))
        if panelbutton==True:
            screen.blit(closepanel,(0,0))
        elif panelbutton==False:
            screen.blit(openpanel,(0,0))
        screen.blit(blueback,(canvasRect.x-10,canvasRect.y-20))
        screen.blit(canvas,canvasRect)
        undo.append(screen.subsurface(canvasRect).copy())
        
    if fileRect.collidepoint(mx,my) and click==1:
        if menubuttons==True:
            menubuttons=False
            filebuttons=True
            editbuttons=False
            toolbuttons=False
            helpbuttons=False
            screen.blit(background,(0,0))
            screen.blit(sidepanel,(0,0))
            screen.blit(blueback,(canvasRect.x-10,canvasRect.y-20))
            screen.blit(undo[-1],canvasRect)
            screen.blit(newbutton,(25,40))
            screen.blit(openbutton,(25,100))
            screen.blit(savebutton,(25,160))
            screen.blit(back,(230,0))
            screen.blit(closepanel,(0,0))
            if stickerbuttons==True:
                screen.blit(sscopy,(300,465))
        
    elif editRect.collidepoint(mx,my) and click==1:
        if menubuttons==True:
            menubuttons=False
            filebuttons=False
            editbuttons=True
            toolbuttons=False
            helpbuttons=False
            screen.blit(background,(0,0))
            screen.blit(sidepanel,(0,0))
            screen.blit(blueback,(canvasRect.x-10,canvasRect.y-20))
            screen.blit(undo[-1],canvasRect)
            screen.blit(undobutton,(25,40))
            screen.blit(redobutton,(25,100))
            screen.blit(cutbutton,(25,160))
            screen.blit(copybutton,(25,220))
            screen.blit(pastebutton,(25,280))
            screen.blit(back,(230,0))
            screen.blit(closepanel,(0,0))
            if stickerbuttons==True:
                screen.blit(sscopy,(300,465))
        
    elif toolsRect.collidepoint(mx,my) and click==1:
        if menubuttons==True:
            menubuttons=False
            filebuttons=False
            editbuttons=False
            toolbuttons=True
            helpbuttons=False
            screen.blit(background,(0,0))
            screen.blit(sidepanel,(0,0))
            screen.blit(blueback,(canvasRect.x-10,canvasRect.y-20))
            screen.blit(undo[-1],canvasRect)
            screen.blit(penciltool,(25,40))
            screen.blit(erasertool,(25,100))
            screen.blit(brushtool,(25,160))
            screen.blit(spraytool,(25,220))
            screen.blit(shapestool,(25,280))
            screen.blit(filltool,(25,340))
            screen.blit(colorwheel,(25,460))
            screen.blit(slider,(25,400))
            screen.blit(ssliderbutton,sizeRect) 
            draw.rect(screen,(255,255,255),(157,566,14,14))
            draw.rect(screen,col,(159,568,10,10))
            screen.blit(back,(230,0))
            screen.blit(closepanel,(0,0))                
            if stickerbuttons==True:
                screen.blit(sscopy,(300,465))

    elif stickersRect.collidepoint(mx,my) and click==1:
        if menubuttons==True:
            menubuttons=True
            filebuttons=False
            editbuttons=False
            toolbuttons=False
            stickerbuttons=True
            helpbuttons=False
            heroesbutton=True
            titanbutton=True
            draw.rect(screen,(177,189,201),(300,465,170,160))
            draw.rect(screen,(white),(305,470,160,150))
            draw.rect(screen,(grey),(305,470,160,50))
            screen.blit(heroeswordw,(390-heroeswordw.get_width()/2,495-heroeswordw.get_height()/2))
            screen.blit(enemieswordg,(390-enemieswordg.get_width()/2,545-enemieswordg.get_height()/2))
            screen.blit(wallpaperwordg,(390-wallpaperwordg.get_width()/2,595-wallpaperwordg.get_height()/2))
            draw.rect(screen,(177,189,201),(480,465,480,160))
            draw.rect(screen,(white),(485,490,470,130))
            screen.blit(titansmall,(530,495))
            screen.blit(arrowbuttonleft,(492.5,535))
            screen.blit(arrowbuttonright,(917.5,535))
            screen.blit(tpreviewlist[0],stickerposRect)
            draw.rect(screen,(white),(485,470,100,20))
            draw.rect(screen,(grey),(587,470,100,18))
            draw.rect(screen,(grey),(689,470,100,18))         
            screen.blit(closepanel,(0,0))
            screen.blit(twordg,(535-twordg.get_width()/2,480-twordg.get_height()/2))
            screen.blit(wwordw,(637-wwordw.get_width()/2,480-wwordw.get_height()/2))
            screen.blit(huwordw,(739-huwordw.get_width()/2,480-huwordw.get_height()/2))
            sscopy=screen.subsurface(slocRect).copy()

    elif helpRect.collidepoint(mx,my) and click==1:
        if menubuttons==True:
            menubuttons=True
            filebuttons=False
            editbuttons=False
            toolbuttons=False
            helpbuttons=True
            draw.rect(screen,(255,20,20),(0,0,20,20))
            screen.blit(background,(0,0))
            screen.blit(sidepanel,(0,0))
            screen.blit(blueback,(canvasRect.x-10,canvasRect.y-20))
            screen.blit(undo[-1],canvasRect)
            screen.blit(filebutton,(25,40))
            screen.blit(editbutton,(25,100))
            screen.blit(toolsbutton,(25,160))
            screen.blit(stickersbutton,(25,220))
            screen.blit(helpbutton,(25,280))
            screen.blit(maker,(10,640-maker.get_height()/.12))
            screen.blit(maker2,(125-maker2.get_width()/2,640-maker2.get_height()/.14))
            screen.blit(closepanel,(0,0))
            if stickerbuttons==True:
                screen.blit(sscopy,(300,465))

#Tools-------------------------------------------
                
    if newRect.collidepoint(mx,my) and filebuttons==True and click==1:
        copy2=screen.copy()
        draw.rect(screen,(255,255,255),(27,42,197,47),3)
        screen.blit(newybutton,(227,42))
        screen.blit(newnbutton,(227,67))
        newbuttons=True
    if newbuttons==True and newRecty.collidepoint(mx,my) and click==1:
        screen.blit(copy2,(0,0))
        screen.blit(newbutton,(25,40))
        screen.blit(canvas,canvasRect)
        undo.append(screen.subsurface(canvasRect).copy())
        newbuttons=False
    elif newbuttons==True and newRectn.collidepoint(mx,my) and click==1:
        screen.blit(copy2,(0,0))
        screen.blit(newbutton,(25,40))
        screen.blit(undo[-1],canvasRect)
        newbuttons=False
    elif openRect.collidepoint(mx,my) and filebuttons==True and click==1:
        newbuttons=False
        screen.blit(copy2,(0,0))
        filename=tkinter.filedialog.askopenfilename()
        openimage=image.load(str(filename))
        openimage=transform.scale(openimage,(660,420))
        screen.set_clip(canvasRect)
        screen.blit(openimage,(canvasRect))
        undo.append(screen.subsurface(canvasRect).copy())
    elif saveRect.collidepoint(mx,my) and filebuttons==True and click==1:
        newbuttons=False
        screen.blit(copy2,(0,0))
        filename=tkinter.filedialog.asksaveasfilename()
        image.save(screen.subsurface(canvasRect),str(filename))

    if brushRect.collidepoint(mx,my) and editbuttons==True and click==1:
        tool="cut"
    elif sprayRect.collidepoint(mx,my) and editbuttons==True and click==1:
        tool="copy"
    elif shapesRect.collidepoint(mx,my) and editbuttons==True and click==1:
        tool="paste"
        
    if stickerbuttons==True and click==1 and heroesRect.collidepoint(mx,my):
        heroesbutton=True
        enemiesbutton=False
        wallpapersbutton=False
        fallenbutton=False
        vexbutton=False
        hivebutton=False
        cabalbutton=False
        titanbutton=True
        draw.rect(screen,(white),(305,470,160,150))
        draw.rect(screen,(grey),(305,470,160,50))
        screen.blit(heroeswordw,(390-heroeswordw.get_width()/2,495-heroeswordw.get_height()/2))
        screen.blit(enemieswordg,(390-enemieswordg.get_width()/2,545-enemieswordg.get_height()/2))
        screen.blit(wallpaperwordg,(390-wallpaperwordg.get_width()/2,595-enemieswordg.get_height()/2))
        draw.rect(screen,(177,189,201),(480,465,480,160))
        draw.rect(screen,(white),(485,490,470,130))
        screen.blit(titansmall,(530,495))
        screen.blit(arrowbuttonleft,(492.5,535))
        screen.blit(arrowbuttonright,(917.5,535))
        screen.blit(tpreviewlist[0],stickerposRect)
        draw.rect(screen,(white),(485,470,100,20))
        draw.rect(screen,(grey),(587,470,100,18))
        draw.rect(screen,(grey),(689,470,100,18))
        screen.blit(twordg,(535-twordg.get_width()/2,480-twordg.get_height()/2))
        screen.blit(wwordw,(637-wwordw.get_width()/2,480-wwordw.get_height()/2))
        screen.blit(huwordw,(739-huwordw.get_width()/2,480-huwordw.get_height()/2))
        sscopy=screen.subsurface(slocRect).copy()
    elif stickerbuttons==True and click==1 and enemiesRect.collidepoint(mx,my):
        heroesbutton=False
        enemiesbutton=True
        wallpapersbutton=False
        titanbutton=False
        warlockbutton=False
        hunterbutton=False
        fallenbutton=True
        draw.rect(screen,(white),(305,470,160,150))
        draw.rect(screen,(grey),(305,520,160,50))
        screen.blit(heroeswordg,(390-heroeswordg.get_width()/2,495-heroeswordg.get_height()/2))
        screen.blit(enemieswordw,(390-enemieswordw.get_width()/2,545-enemieswordw.get_height()/2))
        screen.blit(wallpaperwordg,(390-wallpaperwordg.get_width()/2,595-enemieswordg.get_height()/2))
        draw.rect(screen,(177,189,201),(480,465,480,160))
        draw.rect(screen,(white),(485,490,470,130))
        screen.blit(fallensmall,(530,495))
        screen.blit(arrowbuttonleft,(492.5,535))
        screen.blit(arrowbuttonright,(917.5,535))
        screen.blit(fpreviewlist[0],stickerposRect)
        draw.rect(screen,(white),(485,470,100,20))
        draw.rect(screen,(grey),(587,470,100,18))
        draw.rect(screen,(grey),(689,470,100,18))
        draw.rect(screen,(grey),(791,470,100,18))
        screen.blit(fwordg,(535-fwordg.get_width()/2,480-fwordg.get_height()/2))
        screen.blit(vwordw,(637-vwordw.get_width()/2,480-vwordw.get_height()/2))
        screen.blit(hiwordw,(739-hiwordw.get_width()/2,480-hiwordw.get_height()/2))
        screen.blit(cwordw,(841-cwordw.get_width()/2,480-cwordw.get_height()/2))
        sscopy=screen.subsurface(slocRect).copy()
    elif stickerbuttons==True and click==1 and wallpaperRect.collidepoint(mx,my):
        heroesbutton=False
        enemiesbutton=False
        wallpapersbutton=True
        titanbutton=False
        warlockbutton=False
        hunterbutton=False
        fallenbutton=False
        vexbutton=False
        hivebutton=False
        cabalbutton=False
        draw.rect(screen,(white),(305,470,160,150))
        draw.rect(screen,(grey),(305,570,160,50))
        screen.blit(heroeswordg,(390-heroeswordg.get_width()/2,495-heroeswordg.get_height()/2))
        screen.blit(enemieswordg,(390-enemieswordg.get_width()/2,545-enemieswordg.get_height()/2))
        screen.blit(wallpaperwordw,(390-wallpaperwordw.get_width()/2,595-enemieswordw.get_height()/2))
        sscopy=screen.subsurface(slocRect).copy()
        draw.rect(screen,(177,189,201),(480,465,480,160))
        draw.rect(screen,(white),(485,490,470,130))
        draw.rect(screen,(white),(485,470,100,20))
        screen.blit(wallword,(535-wallword.get_width()/2,480-wallword.get_height()/2))
        screen.set_clip(stickerboxRect)
        screen.blit(wallpaperlistsmall[0],(wallRect1.x,wallRect1.y))
        screen.blit(wallpaperlistsmall[1],(wallRect2.x,wallRect2.y))
        screen.blit(wallpaperlistsmall[2],(wallRect3.x,wallRect3.y))
        screen.blit(wallpaperlistsmall[3],(wallRect4.x,wallRect4.y))
        screen.blit(wallpaperlistsmall[4],(wallRect5.x,wallRect5.y))
        screen.blit(wallpaperlistsmall[5],(wallRect6.x,wallRect6.y))
        screen.blit(wallpaperlistsmall[6],(wallRect7.x,wallRect7.y))
        screen.blit(wallpaperlistsmall[7],(wallRect8.x,wallRect8.y))
        screen.blit(wallpaperlistsmall[8],(wallRect9.x,wallRect9.y))
        screen.blit(wallpaperlistsmall[9],(wallRect10.x,wallRect10.y))
        screen.blit(wallpaperlistsmall[10],(wallRect11.x,wallRect11.y))
        screen.blit(wallpaperlistsmall[11],(wallRect12.x,wallRect12.y))
        screen.blit(wallpaperlistsmall[12],(wallRect13.x,wallRect13.y))
        screen.blit(wallpaperlistsmall[13],(wallRect14.x,wallRect14.y))
        screen.blit(wallpaperlistsmall[14],(wallRect15.x,wallRect15.y))
        screen.blit(wallpaperlistsmall[15],(wallRect16.x,wallRect16.y))
        screen.blit(wallpaperlistsmall[16],(wallRect17.x,wallRect17.y))
        screen.blit(wallpaperlistsmall[17],(wallRect18.x,wallRect18.y))
        
    if stickerbuttons==True and click==1:
        if heroesbutton==True:
            if sTab1.collidepoint(mx,my):
                titanbutton=True
                warlockbutton=False
                hunterbutton=False
                draw.rect(screen,(177,189,201),(480,465,480,160))
                draw.rect(screen,(white),(485,490,470,130))
                screen.blit(titansmall,(530,495))
                screen.blit(arrowbuttonleft,(492.5,535))
                screen.blit(arrowbuttonright,(917.5,535))
                screen.blit(tpreviewlist[0],stickerposRect)
                draw.rect(screen,(white),(485,470,100,20))
                draw.rect(screen,(grey),(587,470,100,18))
                draw.rect(screen,(grey),(689,470,100,18))
                screen.blit(twordg,(535-twordg.get_width()/2,480-twordg.get_height()/2))
                screen.blit(wwordw,(637-wwordw.get_width()/2,480-wwordw.get_height()/2))
                screen.blit(huwordw,(739-huwordw.get_width()/2,480-huwordw.get_height()/2))
                sscopy=screen.subsurface(slocRect).copy()
            elif sTab2.collidepoint(mx,my):
                titanbutton=False
                warlockbutton=True
                hunterbutton=False
                draw.rect(screen,(177,189,201),(480,465,480,160))
                draw.rect(screen,(white),(485,490,470,130))
                screen.blit(warlocksmall,(530,495))
                screen.blit(arrowbuttonleft,(492.5,535))
                screen.blit(arrowbuttonright,(917.5,535))
                screen.blit(wpreviewlist[0],stickerposRect)
                draw.rect(screen,(grey),(485,470,100,18))
                draw.rect(screen,(white),(587,470,100,20))
                draw.rect(screen,(grey),(689,470,100,18))
                screen.blit(twordw,(535-twordw.get_width()/2,480-twordw.get_height()/2))
                screen.blit(wwordg,(637-wwordg.get_width()/2,480-wwordg.get_height()/2))
                screen.blit(huwordw,(739-huwordw.get_width()/2,480-huwordw.get_height()/2))
                sscopy=screen.subsurface(slocRect).copy()
            elif sTab3.collidepoint(mx,my):
                titanbutton=False
                warlockbutton=False
                hunterbutton=True
                draw.rect(screen,(177,189,201),(480,465,480,160))
                draw.rect(screen,(white),(485,490,470,130))
                screen.blit(huntersmall,(530,495))
                screen.blit(arrowbuttonleft,(492.5,535))
                screen.blit(arrowbuttonright,(917.5,535))
                screen.blit(hupreviewlist[0],stickerposRect)
                draw.rect(screen,(grey),(485,470,100,18))
                draw.rect(screen,(grey),(587,470,100,18))
                draw.rect(screen,(white),(689,470,100,20))
                screen.blit(twordw,(535-twordw.get_width()/2,480-twordw.get_height()/2))
                screen.blit(wwordw,(637-wwordw.get_width()/2,480-wwordw.get_height()/2))
                screen.blit(huwordg,(739-huwordg.get_width()/2,480-huwordg.get_height()/2))
                sscopy=screen.subsurface(slocRect).copy()
        elif enemiesbutton==True:
            if sTab1.collidepoint(mx,my):
                fallenbutton=True
                vexbutton=False
                hivebutton=False
                cabalbutton=False
                draw.rect(screen,(177,189,201),(480,465,480,160))
                draw.rect(screen,(white),(485,490,470,130))
                screen.blit(fallensmall,(530,495))
                screen.blit(arrowbuttonleft,(492.5,535))
                screen.blit(arrowbuttonright,(917.5,535))
                screen.blit(fpreviewlist[0],stickerposRect)
                draw.rect(screen,(white),(485,470,100,20))
                draw.rect(screen,(grey),(587,470,100,18))
                draw.rect(screen,(grey),(689,470,100,18))
                draw.rect(screen,(grey),(791,470,100,18))
                screen.blit(fwordg,(535-fwordg.get_width()/2,480-fwordg.get_height()/2))
                screen.blit(vwordw,(637-vwordw.get_width()/2,480-vwordw.get_height()/2))
                screen.blit(hiwordw,(739-hiwordw.get_width()/2,480-hiwordw.get_height()/2))
                screen.blit(cwordw,(841-cwordw.get_width()/2,480-cwordw.get_height()/2))
                sscopy=screen.subsurface(slocRect).copy()
            elif sTab2.collidepoint(mx,my):
                fallenbutton=False
                vexbutton=True
                hivebutton=False
                cabalbutton=False
                draw.rect(screen,(177,189,201),(480,465,480,160))
                draw.rect(screen,(white),(485,490,470,130))
                screen.blit(vexsmall,(530,495))
                screen.blit(arrowbuttonleft,(492.5,535))
                screen.blit(arrowbuttonright,(917.5,535))
                screen.blit(vpreviewlist[0],stickerposRect)
                draw.rect(screen,(grey),(485,470,100,18))
                draw.rect(screen,(white),(587,470,100,20))
                draw.rect(screen,(grey),(689,470,100,18))
                draw.rect(screen,(grey),(791,470,100,18))
                screen.blit(fwordw,(535-fwordw.get_width()/2,480-fwordw.get_height()/2))
                screen.blit(vwordg,(637-vwordg.get_width()/2,480-vwordg.get_height()/2))
                screen.blit(hiwordw,(739-hiwordw.get_width()/2,480-hiwordw.get_height()/2))
                screen.blit(cwordw,(841-cwordw.get_width()/2,480-cwordw.get_height()/2))
                sscopy=screen.subsurface(slocRect).copy()
            elif sTab3.collidepoint(mx,my):
                fallenbutton=False
                vexbutton=False
                hivebutton=True
                cabalbutton=False
                draw.rect(screen,(177,189,201),(480,465,480,160))
                draw.rect(screen,(white),(485,490,470,130))
                screen.blit(hivesmall,(530,495))
                screen.blit(arrowbuttonleft,(492.5,535))
                screen.blit(arrowbuttonright,(917.5,535))
                screen.blit(hipreviewlist[0],stickerposRect)
                draw.rect(screen,(grey),(485,470,100,18))
                draw.rect(screen,(grey),(587,470,100,18))
                draw.rect(screen,(white),(689,470,100,20))
                draw.rect(screen,(grey),(791,470,100,18))
                screen.blit(fwordw,(535-fwordw.get_width()/2,480-fwordw.get_height()/2))
                screen.blit(vwordw,(637-vwordw.get_width()/2,480-vwordw.get_height()/2))
                screen.blit(hiwordg,(739-hiwordg.get_width()/2,480-hiwordg.get_height()/2))
                screen.blit(cwordw,(841-cwordw.get_width()/2,480-cwordw.get_height()/2))
                sscopy=screen.subsurface(slocRect).copy()
            elif sTab4.collidepoint(mx,my):
                fallenbutton=False
                vexbutton=False
                hivebutton=False
                cabalbutton=True
                draw.rect(screen,(177,189,201),(480,465,480,160))
                draw.rect(screen,(white),(485,490,470,130))
                screen.blit(cabalsmall,(530,495))
                screen.blit(arrowbuttonleft,(492.5,535))
                screen.blit(arrowbuttonright,(917.5,535))
                screen.blit(cpreviewlist[0],stickerposRect)
                draw.rect(screen,(grey),(485,470,100,18))
                draw.rect(screen,(grey),(587,470,100,18))
                draw.rect(screen,(grey),(689,470,100,18))
                draw.rect(screen,(white),(791,470,100,20))
                screen.blit(fwordw,(535-fwordw.get_width()/2,480-fwordw.get_height()/2))
                screen.blit(vwordw,(637-vwordw.get_width()/2,480-vwordw.get_height()/2))
                screen.blit(hiwordw,(739-hiwordw.get_width()/2,480-hiwordw.get_height()/2))
                screen.blit(cwordg,(841-cwordg.get_width()/2,480-cwordg.get_height()/2))
                sscopy=screen.subsurface(slocRect).copy()
                
        elif wallpapersbutton==True and stickerboxRect.collidepoint(mx,my):
            if click==1:
                if wallRect1.collidepoint(mx,my):
                    screen.blit(wallpaperlist[0],(0,0))
                    background=wallpaperlist[0]
                elif wallRect2.collidepoint(mx,my):
                    screen.blit(wallpaperlist[1],(0,0))
                    background=wallpaperlist[1]
                elif wallRect3.collidepoint(mx,my):
                    screen.blit(wallpaperlist[2],(0,0))
                    background=wallpaperlist[2]
                elif wallRect4.collidepoint(mx,my):
                    screen.blit(wallpaperlist[3],(0,0))
                    background=wallpaperlist[3]
                elif wallRect5.collidepoint(mx,my):
                    screen.blit(wallpaperlist[4],(0,0))
                    background=wallpaperlist[4]
                elif wallRect6.collidepoint(mx,my):
                    screen.blit(wallpaperlist[5],(0,0))
                    background=wallpaperlist[5]
                elif wallRect7.collidepoint(mx,my):
                    screen.blit(wallpaperlist[6],(0,0))
                    background=wallpaperlist[6]
                elif wallRect8.collidepoint(mx,my):
                    screen.blit(wallpaperlist[7],(0,0))
                    background=wallpaperlist[7]
                elif wallRect9.collidepoint(mx,my):
                    screen.blit(wallpaperlist[8],(0,0))
                    background=wallpaperlist[8]
                elif wallRect10.collidepoint(mx,my):
                    screen.blit(wallpaperlist[9],(0,0))
                    background=wallpaperlist[9]
                elif wallRect11.collidepoint(mx,my):
                    screen.blit(wallpaperlist[10],(0,0))
                    background=wallpaperlist[10]
                elif wallRect12.collidepoint(mx,my):
                    screen.blit(wallpaperlist[11],(0,0))
                    background=wallpaperlist[11]
                elif wallRect13.collidepoint(mx,my):
                    screen.blit(wallpaperlist[12],(0,0))
                    background=wallpaperlist[12]
                elif wallRect14.collidepoint(mx,my):
                    screen.blit(wallpaperlist[13],(0,0))
                    background=wallpaperlist[13]
                elif wallRect15.collidepoint(mx,my):
                    screen.blit(wallpaperlist[14],(0,0))
                    background=wallpaperlist[14]
                elif wallRect16.collidepoint(mx,my):
                    screen.blit(wallpaperlist[15],(0,0))
                    background=wallpaperlist[15]
                elif wallRect17.collidepoint(mx,my):
                    screen.blit(wallpaperlist[16],(0,0))
                    background=wallpaperlist[16]
                elif wallRect18.collidepoint(mx,my):
                    screen.blit(wallpaperlist[17],(0,0))
                    background=wallpaperlist[17]
                screen.blit(blueback,(canvasRect.x-10,canvasRect.y-20))
                screen.blit(undo[-1],canvasRect)
                if filebuttons==True:
                    screen.blit(sidepanel,(0,0))
                    screen.blit(newbutton,(25,40))
                    screen.blit(openbutton,(25,100))
                    screen.blit(savebutton,(25,160))
                    screen.blit(back,(230,0))
                    screen.blit(closepanel,(0,0))
                elif editbuttons==True:
                    screen.blit(sidepanel,(0,0))
                    screen.blit(undobutton,(25,40))
                    screen.blit(redobutton,(25,100))
                    screen.blit(cutbutton,(25,160))
                    screen.blit(copybutton,(25,220))
                    screen.blit(pastebutton,(25,280))
                    screen.blit(back,(230,0))
                    screen.blit(closepanel,(0,0))
                elif toolbuttons==True:
                    screen.blit(sidepanel,(0,0))
                    screen.blit(penciltool,(25,40))
                    screen.blit(erasertool,(25,100))
                    screen.blit(brushtool,(25,160))
                    screen.blit(spraytool,(25,220))
                    screen.blit(shapestool,(25,280))
                    screen.blit(filltool,(25,340))
                    screen.blit(colorwheel,(25,460))
                    screen.blit(slider,(25,400))
                    screen.blit(ssliderbutton,sizeRect) 
                    draw.rect(screen,(255,255,255),(157,566,14,14))
                    draw.rect(screen,col,(159,568,10,10))
                    screen.blit(back,(230,0))
                    screen.blit(closepanel,(0,0))
                elif menubuttons==True:
                    screen.blit(sidepanel,(0,0))
                    screen.blit(filebutton,(25,40))
                    screen.blit(editbutton,(25,100))
                    screen.blit(toolsbutton,(25,160))
                    screen.blit(stickersbutton,(25,220))
                    screen.blit(helpbutton,(25,280))
                    screen.blit(closepanel,(0,0))
                draw.rect(screen,(177,189,201),(300,465,170,160))
                draw.rect(screen,(white),(305,470,160,150))
                draw.rect(screen,(grey),(305,570,160,50))
                screen.blit(heroeswordg,(390-heroeswordg.get_width()/2,495-heroeswordg.get_height()/2))
                screen.blit(enemieswordg,(390-enemieswordg.get_width()/2,545-enemieswordg.get_height()/2))
                screen.blit(wallpaperwordw,(390-wallpaperwordw.get_width()/2,595-enemieswordw.get_height()/2))
                sscopy=screen.subsurface(slocRect).copy()
                draw.rect(screen,(177,189,201),(480,465,480,160))
                draw.rect(screen,(white),(485,490,470,130))
                draw.rect(screen,(white),(485,470,100,20))
                if panelbutton==False:
                    screen.blit(openpanel,(0,0))
                screen.blit(wallword,(535-wallword.get_width()/2,480-wallword.get_height()/2))
                screen.set_clip(stickerboxRect)
                screen.blit(wallpaperlistsmall[0],(wallRect1.x,wallRect1.y))
                screen.blit(wallpaperlistsmall[1],(wallRect2.x,wallRect2.y))
                screen.blit(wallpaperlistsmall[2],(wallRect3.x,wallRect3.y))
                screen.blit(wallpaperlistsmall[3],(wallRect4.x,wallRect4.y))
                screen.blit(wallpaperlistsmall[4],(wallRect5.x,wallRect5.y))
                screen.blit(wallpaperlistsmall[5],(wallRect6.x,wallRect6.y))
                screen.blit(wallpaperlistsmall[6],(wallRect7.x,wallRect7.y))
                screen.blit(wallpaperlistsmall[7],(wallRect8.x,wallRect8.y))
                screen.blit(wallpaperlistsmall[8],(wallRect9.x,wallRect9.y))
                screen.blit(wallpaperlistsmall[9],(wallRect10.x,wallRect10.y))
                screen.blit(wallpaperlistsmall[10],(wallRect11.x,wallRect11.y))
                screen.blit(wallpaperlistsmall[11],(wallRect12.x,wallRect12.y))
                screen.blit(wallpaperlistsmall[12],(wallRect13.x,wallRect13.y))
                screen.blit(wallpaperlistsmall[13],(wallRect14.x,wallRect14.y))
                screen.blit(wallpaperlistsmall[14],(wallRect15.x,wallRect15.y))
                screen.blit(wallpaperlistsmall[15],(wallRect16.x,wallRect16.y))
                screen.blit(wallpaperlistsmall[16],(wallRect17.x,wallRect17.y))
                screen.blit(wallpaperlistsmall[17],(wallRect18.x,wallRect18.y))
                sscopy=screen.subsurface(slocRect).copy()
                
                
    if arrowRectright.collidepoint(mx,my) and click==1:
        if heroesbutton==True:
            if titanbutton==True:
                for i in range (len(tpreviewlist)):
                    draw.rect(screen,(white),(485,490,470,130))
                    screen.blit(titansmall,(530,495))
                    screen.blit(tpreviewlist[1],stickerposRect)
                    screen.blit(arrowbuttonleft,(492.5,535))
                    screen.blit(arrowbuttonright,(917.5,535))
                tpreviewlist=tpreviewlist[1:]+[tpreviewlist[0]]
                tcounter+=1
                if tcounter>=(len(tpreviewlist)):
                    tcounter=0
                time.wait(100)
                display.flip()
            elif warlockbutton==True:
                for i in range (len(wpreviewlist)):
                    draw.rect(screen,(white),(485,490,470,130))
                    screen.blit(warlocksmall,(530,495))
                    screen.blit(wpreviewlist[1],stickerposRect)
                    screen.blit(arrowbuttonleft,(492.5,535))
                    screen.blit(arrowbuttonright,(917.5,535))
                wpreviewlist=wpreviewlist[1:]+[wpreviewlist[0]]
                wcounter+=1
                if wcounter>=(len(wpreviewlist)):
                    wcounter=0
                time.wait(100)
                display.flip()
            elif hunterbutton==True:
                for i in range (len(hupreviewlist)):
                    draw.rect(screen,(white),(485,490,470,130))
                    screen.blit(huntersmall,(530,495))
                    screen.blit(hupreviewlist[1],stickerposRect)
                    screen.blit(arrowbuttonleft,(492.5,535))
                    screen.blit(arrowbuttonright,(917.5,535))
                hupreviewlist=hupreviewlist[1:]+[hupreviewlist[0]]
                hucounter+=1
                if hucounter>=(len(hupreviewlist)):
                    hucounter=0
                time.wait(100)
                display.flip()
        if enemiesbutton==True:
            if fallenbutton==True:
                for i in range (len(fpreviewlist)):
                    draw.rect(screen,(white),(485,490,470,130))
                    screen.blit(fallensmall,(530,495))
                    screen.blit(fpreviewlist[1],stickerposRect)
                    screen.blit(arrowbuttonleft,(492.5,535))
                    screen.blit(arrowbuttonright,(917.5,535))
                fpreviewlist=fpreviewlist[1:]+[fpreviewlist[0]]
                fcounter+=1
                if fcounter>=(len(fpreviewlist)):
                    fcounter=0
                time.wait(100)
                display.flip()
            elif vexbutton==True:
                for i in range (len(vpreviewlist)):
                    draw.rect(screen,(white),(485,490,470,130))
                    screen.blit(vexsmall,(530,495))
                    screen.blit(vpreviewlist[1],stickerposRect)
                    screen.blit(arrowbuttonleft,(492.5,535))
                    screen.blit(arrowbuttonright,(917.5,535))
                vpreviewlist=vpreviewlist[1:]+[vpreviewlist[0]]
                vcounter+=1
                if vcounter>=(len(vpreviewlist)):
                    vcounter=0
                time.wait(100)
                display.flip()
            elif hivebutton==True:
                for i in range (len(hipreviewlist)):
                    draw.rect(screen,(white),(485,490,470,130))
                    screen.blit(hivesmall,(530,495))
                    screen.blit(hipreviewlist[1],stickerposRect)
                    screen.blit(arrowbuttonleft,(492.5,535))
                    screen.blit(arrowbuttonright,(917.5,535))
                hipreviewlist=hipreviewlist[1:]+[hipreviewlist[0]]
                hicounter+=1
                if hicounter>=(len(hipreviewlist)):
                    hicounter=0
                time.wait(100)
                display.flip()
            elif cabalbutton==True:
                for i in range (len(cpreviewlist)):
                    draw.rect(screen,(white),(485,490,470,130))
                    screen.blit(cabalsmall,(530,495))
                    screen.blit(cpreviewlist[1],stickerposRect)
                    screen.blit(arrowbuttonleft,(492.5,535))
                    screen.blit(arrowbuttonright,(917.5,535))
                cpreviewlist=cpreviewlist[1:]+[cpreviewlist[0]]
                ccounter+=1
                if ccounter>=(len(cpreviewlist)):
                    ccounter=0
                time.wait(100)
                display.flip()
    if arrowRectleft.collidepoint(mx,my) and click==1:
        if heroesbutton==True:
            if titanbutton==True:
                for i in range (len(tpreviewlist)):
                    draw.rect(screen,(white),(485,490,470,130))
                    screen.blit(titansmall,(530,495))
                    screen.blit(tpreviewlist[-1],stickerposRect)
                    screen.blit(arrowbuttonleft,(492.5,535))
                    screen.blit(arrowbuttonright,(917.5,535))
                tpreviewlist=[tpreviewlist[-1]]+tpreviewlist[:-1]
                tcounter-=1
                if tcounter<0:
                    tcounter=(len(tpreviewlist)-1)
                time.wait(100)
                display.flip()
            elif warlockbutton==True:
                for i in range (len(wpreviewlist)):
                    draw.rect(screen,(white),(485,490,470,130))
                    screen.blit(warlocksmall,(530,495))
                    screen.blit(wpreviewlist[-1],stickerposRect)
                    screen.blit(arrowbuttonleft,(492.5,535))
                    screen.blit(arrowbuttonright,(917.5,535))
                wpreviewlist=wpreviewlist[1:]+[wpreviewlist[0]]
                wcounter-=1
                if wcounter<0:
                    wcounter=(len(wpreviewlist)-1)
                time.wait(100)
                display.flip()
            elif hunterbutton==True:
                for i in range (len(hupreviewlist)):
                    draw.rect(screen,(white),(485,490,470,130))
                    screen.blit(huntersmall,(530,495))
                    screen.blit(hupreviewlist[-1],stickerposRect)
                    screen.blit(arrowbuttonleft,(492.5,535))
                    screen.blit(arrowbuttonright,(917.5,535))
                hupreviewlist=hupreviewlist[1:]+[hupreviewlist[0]]
                hucounter-=1
                if hucounter<0:
                    hucounter=(len(hupreviewlist)-1)
                time.wait(100)
                display.flip()
        if enemiesbutton==1:
            if fallenbutton==True:
                for i in range (len(fpreviewlist)):
                    draw.rect(screen,(white),(485,490,470,130))
                    screen.blit(fallensmall,(530,495))
                    screen.blit(fpreviewlist[-1],stickerposRect)
                    screen.blit(arrowbuttonleft,(492.5,535))
                    screen.blit(arrowbuttonright,(917.5,535))
                fpreviewlist=[fpreviewlist[-1]]+fpreviewlist[:-1]
                fcounter-=1
                if fcounter<0:
                    fcounter=(len(fpreviewlist)-1)
                time.wait(100)
                display.flip()
            elif vexbutton==True:
                for i in range (len(vpreviewlist)):
                    draw.rect(screen,(white),(485,490,470,130))
                    screen.blit(vexsmall,(530,495))
                    screen.blit(vpreviewlist[-1],stickerposRect)
                    screen.blit(arrowbuttonleft,(492.5,535))
                    screen.blit(arrowbuttonright,(917.5,535))
                vpreviewlist=[vpreviewlist[-1]]+vpreviewlist[:-1]
                vcounter-=1
                if vcounter<0:
                    vcounter=(len(vpreviewlist)-1)
                time.wait(100)
                display.flip()
            elif hivebutton==True:
                for i in range (len(hipreviewlist)):
                    draw.rect(screen,(white),(485,490,470,130))
                    screen.blit(hivesmall,(530,495))
                    screen.blit(hipreviewlist[-1],stickerposRect)
                    screen.blit(arrowbuttonleft,(492.5,535))
                    screen.blit(arrowbuttonright,(917.5,535))
                hipreviewlist=[hipreviewlist[-1]]+hipreviewlist[:-1]
                hicounter-=1
                if hicounter<0:
                    hicounter=(len(hipreviewlist)-1)
                time.wait(100)
                display.flip()
            elif cabalbutton==True:
                for i in range (len(cpreviewlist)):
                    draw.rect(screen,(white),(485,490,470,130))
                    screen.blit(cabalsmall,(530,495))
                    screen.blit(cpreviewlist[-1],stickerposRect)
                    screen.blit(arrowbuttonleft,(492.5,535))
                    screen.blit(arrowbuttonright,(917.5,535))
                cpreviewlist=[cpreviewlist[-1]]+cpreviewlist[:-1]
                ccounter-=1
                if ccounter<0:
                    ccounter=(len(cpreviewlist)-1)
                time.wait(100)
                display.flip()

    if stickerposRect.collidepoint(mx,my) and click==1:
        if heroesbutton==True:
            if titanbutton==True:
                tool="titan"
            elif warlockbutton==True:
                tool="warlock"
            elif hunterbutton==True:
                tool="hunter"
        elif enemiesbutton==True:
            if fallenbutton==True:
                tool="fallen"
            elif vexbutton==True:
                tool="vex"
            elif hivebutton==True:
                tool="hive"
            elif cabalbutton==True:
                tool="cabal"
            
    if pencilRect.collidepoint(mx,my) and toolbuttons==True:
        if click==1:
            screen.blit(penciltool,(25,40))
            draw.rect(screen,(255,255,255),(27,42,197,47),3)
            screen.blit(erasertool,(25,100))
            screen.blit(brushtool,(25,160))
            screen.blit(spraytool,(25,220))
            screen.blit(shapestool,(25,280))
            screen.blit(filltool,(25,340))
            tool="pencil"
            shapesbutton=False
    elif eraserRect.collidepoint(mx,my) and toolbuttons==True:
        if click==1:
            screen.blit(penciltool,(25,40))
            screen.blit(erasertool,(25,100))
            draw.rect(screen,(255,255,255),(27,102,197,47),3)
            screen.blit(brushtool,(25,160))
            screen.blit(spraytool,(25,220))
            screen.blit(shapestool,(25,280))
            screen.blit(filltool,(25,340))
            tool="eraser"
            shapesbutton=False
    elif brushRect.collidepoint(mx,my) and toolbuttons==True:
        if click==1:
            screen.blit(penciltool,(25,40))
            screen.blit(erasertool,(25,100))
            screen.blit(brushtool,(25,160))
            draw.rect(screen,(255,255,255),(27,162,197,47),3) 
            screen.blit(spraytool,(25,220))
            screen.blit(shapestool,(25,280))
            screen.blit(filltool,(25,340))
            tool="brush"
            shapesbutton=False
    elif sprayRect.collidepoint(mx,my) and toolbuttons==True:
        if click==1:
            screen.blit(penciltool,(25,40))
            screen.blit(erasertool,(25,100))
            screen.blit(brushtool,(25,160))
            screen.blit(spraytool,(25,220))
            draw.rect(screen,(255,255,255),(27,222,197,47),3)
            screen.blit(shapestool,(25,280))
            screen.blit(filltool,(25,340))
            tool="spray"
            shapesbutton=False
    elif shapesRect.collidepoint(mx,my) and toolbuttons==True:
        if click==1:
            screen.blit(penciltool,(25,40))
            screen.blit(erasertool,(25,100))
            screen.blit(brushtool,(25,160))
            screen.blit(spraytool,(25,220))
            screen.blit(shapestool2,(25,280))
            screen.blit(filltool,(25,340))
            tool="shapes"
            shapesbutton=True
    elif fillRect.collidepoint(mx,my) and toolbuttons==True:
        if click==1:
            screen.blit(penciltool,(25,40))
            screen.blit(erasertool,(25,100))
            screen.blit(brushtool,(25,160))
            screen.blit(spraytool,(25,220))
            screen.blit(shapestool,(25,280))
            screen.blit(filltool,(25,340))
            draw.rect(screen,(255,255,255),(27,342,197,47),3)
            tool="fill"
            shapesbutton=False

    if shapesbutton==True and click==1 and toolbuttons==True:
        if ellipseRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,255),(36,292,27,27),1)
            tool="ellipse"
        elif lineRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,255),(68,292,26,27),1)
            tool="line"
        elif rectRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,255),(102,294,36,24),1)
            tool="rectangle"
        elif inverseRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,255),(146,289,33,35),1)
            tool="inverse"
        elif polygonRect.collidepoint(mx,my):
            draw.rect(screen,(255,255,255),(186,289,30,32),1)
            tool="polygon"

    if mx>25 and my>403 and mx<225 and my<447 and toolbuttons==True:
        if mx<50:
            sizepos=28
        elif mx>200:
            sizepos=178
        else:
            sizepos=mx-22
        sizeRect=Rect(sizepos,403,44,44)
        if sizeRect.collidepoint(mx,my) and click==1 and toolbuttons==True:
            screen.blit(slider,(25,400))
            screen.blit(ssliderbutton,(sizeRect))
            size=sizepos-int(sizepos*.64)
            
    elif backRect.collidepoint(mx,my) and click==1:
        if toolbuttons==True or filebuttons==True or editbuttons==True:
            screen.blit(background,(0,0))
            screen.blit(blueback,(canvasRect.x-10,canvasRect.y-20))
            screen.blit(undo[-1],canvasRect)
            screen.blit(sidepanel,(0,0))
            screen.blit(filebutton,(25,40))
            screen.blit(editbutton,(25,100))
            screen.blit(toolsbutton,(25,160))
            screen.blit(stickersbutton,(25,220))
            screen.blit(helpbutton,(25,280))
            screen.blit(closepanel,(0,0))
            menubuttons=True
            filebuttons=False
            editbuttons=False
            toolbuttons=False
            helpbuttons=False
            if stickerbuttons==True:
                screen.blit(sscopy,(300,465))
            
    if wheel.collidepoint(mx,my) and click==1 and toolbuttons==True:
        col=screen.get_at((mx,my))
        draw.rect(screen,(255,255,255),(157,566,14,14))
        draw.rect(screen,col,(159,568,10,10))
        
    if colbuttonRect.collidepoint(mx,my) and click==1 and colorslider==False:
        copy3=screen.copy()
        screen.blit(blackscreen,(0,0))
        screen.blit(whitescreen,(512-whitescreen.get_width()/2,320-whitescreen.get_height()/2))
        draw.rect(screen,col,(347.5,235,305,50))
        draw.rect(screen,col,(347.5,295,305,50))
        draw.rect(screen,col,(347.5,355,305,50))
        screen.blit(rsliderbutton,rsliderRect)
        screen.blit(gsliderbutton,gsliderRect)
        screen.blit(bsliderbutton,bsliderRect)
        rcolnum=centuryfont4.render(str(rcol),True,(rcol,0,0))
        gcolnum=centuryfont4.render(str(gcol),True,(0,gcol,0))
        bcolnum=centuryfont4.render(str(bcol),True,(0,0,bcol))
        screen.blit(rcolnum,(654,242.5))
        screen.blit(gcolnum,(654,302.5))
        screen.blit(bcolnum,(654,362.5))
        menubuttons=False
        filebuttons=False
        editbuttons=False
        toolbuttons=False
        helpbuttons=False
        colorslider=True
        
    if colorslider==True:
        if mx>347.5 and mx<652.5 and my>235 and my<285:
            if mx<369.5:
                rcolpos=350.5
            elif mx>627.5:
                rcolpos=605.5
            else:
                rcolpos=mx-22
            rsliderRect=Rect(rcolpos,238,44,44)
            if rsliderRect.collidepoint(mx,my) and click==1:
                colcopy=screen.subsurface(colsetRectcopy).copy()
                screen.blit(whitescreen,(512-whitescreen.get_width()/2,320-whitescreen.get_height()/2))
                screen.blit(colcopy,(347.5,235))
                draw.rect(screen,(rcol,0,0),(347.5,235,305,50))
                screen.blit(rsliderbutton,rsliderRect)
                rcol= abs(int(rcolpos-350))
                col=((rcol,gcol,bcol))
                rcolnum=centuryfont4.render(str(rcol),True,(col))
                gcolnum=centuryfont4.render(str(gcol),True,(col))
                bcolnum=centuryfont4.render(str(bcol),True,(col))
                screen.blit(rcolnum,(654,242.5))
                screen.blit(gcolnum,(654,302.5))
                screen.blit(bcolnum,(654,362.5))
        elif mx>347.5 and mx<652.5 and my>295 and my<345:
            if mx<369.5:
                gcolpos=350.5
            elif mx>627.5:
                gcolpos=605.5
            else:
                gcolpos=mx-22
            gsliderRect=Rect(gcolpos,298,44,44)
            if gsliderRect.collidepoint(mx,my) and click==1:
                colcopy=screen.subsurface(colsetRectcopy).copy()
                screen.blit(whitescreen,(512-whitescreen.get_width()/2,320-whitescreen.get_height()/2))
                screen.blit(colcopy,(347.5,235))
                draw.rect(screen,(0,gcol,0),(347.5,295,305,50))
                screen.blit(gsliderbutton,gsliderRect)
                gcol=abs(int(gcolpos-350))
                col=((rcol,gcol,bcol))
                rcolnum=centuryfont4.render(str(rcol),True,(col))
                gcolnum=centuryfont4.render(str(gcol),True,(col))
                bcolnum=centuryfont4.render(str(bcol),True,(col))
                screen.blit(rcolnum,(654,242.5))
                screen.blit(gcolnum,(654,302.5))
                screen.blit(bcolnum,(654,362.5))
        elif mx>347.5 and mx<652.5 and my>355 and my<405:
            if mx<369.5:
                bcolpos=350.5
            elif mx>627.5:
                bcolpos=605.5
            else:
                bcolpos=mx-22
            bsliderRect=Rect(bcolpos,358,44,44)
            if bsliderRect.collidepoint(mx,my) and click==1:
                colcopy=screen.subsurface(colsetRectcopy).copy()
                screen.blit(whitescreen,(512-whitescreen.get_width()/2,320-whitescreen.get_height()/2))
                screen.blit(colcopy,(347.5,235))
                draw.rect(screen,(0,0,bcol),(347.5,355,305,50))
                screen.blit(bsliderbutton,bsliderRect)
                bcol=abs(int(bcolpos-350))
                col=((rcol,gcol,bcol))
                rcolnum=centuryfont4.render(str(rcol),True,(col))
                gcolnum=centuryfont4.render(str(gcol),True,(col))
                bcolnum=centuryfont4.render(str(bcol),True,(col))
                screen.blit(rcolnum,(654,242.5))
                screen.blit(gcolnum,(654,302.5))
                screen.blit(bcolnum,(654,362.5))

        elif click==1 and not colsetRect.collidepoint(mx,my) and not colbuttonRect.collidepoint(mx,my):
            screen.blit(copy3,(0,0))
            screen.blit(blueback,(canvasRect.x-10,canvasRect.y-20))
            screen.blit(undo[-1],canvasRect)
            draw.rect(screen,col,(159,568,10,10))
            menubuttons=False
            filebuttons=False
            editbuttons=False
            toolbuttons=True
            helpbuttons=False
            colorslider=False
            
#Tools Main Program----------------------------------------
            
    if click==1 and canvasRect.collidepoint(mx,my) and colorslider==False:
        screen.set_clip(canvasRect)
        if tool=="pencil":
            draw.aaline(screen,col,(omx,omy),(mx,my),1)
        elif tool=="eraser":
            for i in range (int(dist)):
                ndx=int(omx+sx*i)
                ndy=int(omy+sy*i)
                draw.circle(screen,(255,255,255),(ndx,ndy),size)
        elif tool=="brush":
            for i in range (int(dist)):
                ndx=int(omx+sx*i)
                ndy=int(omy+sy*i)
                draw.circle(screen,col,(ndx,ndy),size)
        elif tool=="spray":
            for i in range(20):
                pointx=randint(mx-size,mx+size)
                pointy=randint(my-size,my+size)
                if ((pointx-mx)**2+(pointy-my)**2)**0.5<=size:
                    draw.circle(screen, col,(pointx,pointy),0)
        elif tool=="ellipse":
            screen.blit(canvascopy,canvasRect)
            rectang=Rect(oldmx,oldmy,mx-oldmx,my-oldmy)
            rectang.normalize()
            if abs(size-9) >= abs((mx-oldmx)/2) or abs(size-9) >= abs((my-oldmy)/2):
                sizeE=0
            elif abs(size-9) <= abs((mx-oldmx)/2) or abs(size-9) <= abs((my-oldmy)/2):
                sizeE=size-9
            draw.ellipse(screen,col,rectang,sizeE)
        elif tool=="line":
            screen.blit(canvascopy,canvasRect)
            rectang=Rect(oldmx,oldmy,mx-oldmx,my-oldmy)
            rectang.normalize()
            draw.line(screen, col,(oldmx,oldmy),(mx,my), size-9)
        elif tool=="rectangle":
            screen.blit(canvascopy,canvasRect)
            rectang=Rect(oldmx,oldmy,mx-oldmx,my-oldmy)
            rectang.normalize()
            draw.rect(screen, col, (oldmx,oldmy,mx-oldmx,my-oldmy),size-9)
        elif tool=="inverse":
            screen.blit(canvascopy,canvasRect)
            copysquare=(screen.subsurface(oldmx,oldmy,mx-oldmx,my-oldmy))
            draw.rect(screen,white,(oldmx,oldmy,mx-oldmx,my-oldmy),1)
            inverse=True
        elif tool=="polygon":
            if mb[0]==1:
                draw.circle(screen,col,(mx,my),2)
                polygonlist.append((mx,my))
                if len(polygonlist)>1:
                    draw.line(screen,col,(polygonlist[-2]),(polygonlist[-1]))
        elif tool=="fill":
            oldcol=screen.get_at((mx,my))
            floodfill(mx,my,oldcol,col)

        elif tool=="cut":
            screen.blit(canvascopy,canvasRect)
            draw.rect(screen,(0,0,0), (oldmx,oldmy,mx-oldmx,my-oldmy),1)
            cutcopy=True
        elif tool=="copy":
            screen.blit(canvascopy,canvasRect)
            draw.rect(screen,(0,0,0), (oldmx,oldmy,mx-oldmx,my-oldmy),1)
            cutcopy=True
        elif tool=="paste":
            screen.blit(canvascopy,canvasRect)
            screen.blit(cccopy,(mx-cccopy.get_width()/2,my-cccopy.get_height()/2))

        elif tool=="titan":
            screen.blit(canvascopy,canvasRect)
            screen.blit(titanlist[tcounter],(mx,my))
        elif tool=="warlock":
            screen.blit(canvascopy,canvasRect)
            screen.blit(warlocklist[wcounter],(mx,my))
        elif tool=="hunter":
            screen.blit(canvascopy,canvasRect)
            screen.blit(hunterlist[hucounter],(mx,my))
        elif tool=="fallen":
            screen.blit(canvascopy,canvasRect)
            screen.blit(fallenlist[fcounter],(mx,my))
        elif tool=="vex":
            screen.blit(canvascopy,canvasRect)
            screen.blit(vexlist[vcounter],(mx,my))
        elif tool=="hive":
            screen.blit(canvascopy,canvasRect)
            screen.blit(hivelist[hicounter],(mx,my))
        elif tool=="cabal":
            screen.blit(canvascopy,canvasRect)
            screen.blit(cabal[ccounter],(mx,my))
            
    if click==0 and canvasRect.collidepoint(mx,my) and colorslider==False:
        screen.set_clip(canvasRect)
        if inverse==True:
            invertcol(copysquare)
            undo.append(screen.subsurface(canvasRect).copy())
            inverse=False
        if cutcopy==True:
            rectang2=Rect(oldmx,oldmy,mx-oldmx,my-oldmy)
            rectang2.normalize()
            if tool=="cut":
                screen.blit(canvascopy,canvasRect)
                ccpos=(screen.subsurface(rectang2))
                cccopy=ccpos.copy()
                draw.rect(screen,(255,255,255), (oldmx,oldmy,mx-oldmx,my-oldmy))
                undo.append(screen.subsurface(canvasRect).copy())
                cutcopy=False
            elif tool=="copy":
                screen.blit(canvascopy,canvasRect)
                ccpos=(screen.subsurface(rectang2))
                cccopy=ccpos.copy()
                draw.rect(screen,(255,255,255), (oldmx,oldmy,mx-oldmx,my-oldmy))
                screen.blit(cccopy,(oldmx,oldmy))
                undo.append(screen.subsurface(canvasRect).copy())
                cutcopy=False

    if mb[2]==1 and canvasRect.collidepoint(mx,my) and colorslider==False:
        screen.set_clip(canvasRect)
        if len(polygonlist)>1:
            draw.polygon(screen,col,polygonlist,6)
            del polygonlist[0:]
        else:
           del polygonlist[0:]
        undo.append(screen.subsurface(canvasRect).copy())
                    
    screen.set_clip(None)
    display.flip()
quit()
