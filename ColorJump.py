import pygame
import random as r

pygame.font.init()
pygame.init()

my_font = pygame.font.SysFont('Adobe Garamond Pro', 80)


clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

jump_sound = pygame.mixer.Sound("sounds/bounce.mp3")
win_sound = pygame.mixer.Sound("sounds/winSound.mp3")
pygame.mixer.music.load('sounds/awesomeMusic.mp3')
pygame.mixer.music.play(-1 )


gravity = 7
gravMultiple = 1.05
JUMP = 100
rectYVal = -50
greenRectXVal = 250

time = 0
realTime = 0.0

playgame = False

circColor = "blue"

moveLeft = True#Boolean to see if the green rect is moving right or left
    
topCircleRect = pygame.Rect((200,10,300,rectYVal-200))
myCircleRect = pygame.Rect((50,50,375,375))
botCircleRect = pygame.Rect((200,10,300,rectYVal-200 + 175))
greenRect = pygame.Rect((greenRectXVal, rectYVal-400, 75, 25))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def gameScreen():
    global playgame
    global run
    screen.fill("black")
    welcomeScreen = my_font.render('Welcome to Color Jump!', False, (255, 255, 255))
    screen.blit(welcomeScreen, (70,200))
    start = my_font.render('Press Space to Start', False, (255, 255, 255))
    screen.blit(start, (125,350))
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                playgame = True
                reset()
        if event.type == pygame.QUIT:
            run = False
    

def fallingGravity():
    global rectYVal 
    global myCircleRect
    global topCircleRect
    global botCircleRect
    
    rectYVal -= gravity
    
    screen.fill("black")
    # pygame.draw.rect(screen, "white", myCircleRect)#HITBOX
    # pygame.draw.rect(screen, "white", topCircleRect)
    # pygame.draw.rect(screen, "white", botCircleRect)
    
    pygame.draw.rect(screen,"red", (325,rectYVal,150,75))#FIRST JUMP
    pygame.draw.circle(screen, "red", (400,400), 25)#PLAYER
    pygame.draw.circle(screen, circColor, (400,rectYVal-200), 100, width=10)#COLOR SWAPPING CIRCLE
    pygame.draw.rect(screen, "green", (greenRectXVal, rectYVal-400, 75, 25))#moving green plat
    
    myCircleRect = pygame.Rect((375,375,50,50))
    topCircleRect = pygame.Rect((300,rectYVal-305 ,185, 10))
    botCircleRect = pygame.Rect((300,rectYVal-305 + 190,200,10))

#returns boolean to make code more readable
# def looseConditions():
#     #does my cicle collide with either the bottom hit box  or the top of the color changing circle while its blue? and does it not hit the green moving box
#     return ((myCircleRect.colliderect(botCircleRect) or myCircleRect.colliderect(topCircleRect))and circColor == "blue") and myCircleRect.colliderect(greenRect)

#play bounce sound when jumping  
def bounceSound():
    pygame.mixer.Sound.play(jump_sound)
    # pygame.mixer.music.stop() 
    
def reset():
    global rectYVal
    rectYVal = -50
    
run = True
while run:
    
    
    if(playgame):
        # screen.blit(screen, myCircleRect)
        # screen.blit(screen, firstCircleRect)
        # pygame.draw.rect(screen, "white", myCircleRect)#HI TBOX
        # pygame.draw.rect(screen, "white", topCircleRect)
        # pygame.draw.rect(screen, "white", botCircleRect)
        # print("Work")
        pygame.draw.rect(screen, "green", (greenRectXVal, rectYVal-400, 75, 25))
        pygame.draw.rect(screen,"red", (325,rectYVal,150,75))
        pygame.draw.circle(screen, "red", (400,400), 25)
        pygame.draw.circle(screen, circColor, (400,rectYVal-200), 100, width=10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False   
            print("Work")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    bounceSound()
                    gravity = 7
                    rectYVal+=JUMP
                    print("Jumping!")  
            
            screen.fill("black")
        if(playgame):
            if (((myCircleRect.colliderect(botCircleRect) or myCircleRect.colliderect(topCircleRect))and circColor == "blue") or myCircleRect.colliderect(greenRect)):
                print("COLLISION")
                playgame = False
            elif(rectYVal <= -1000):#out of bounds
                print("Out Of Bounds")
                playgame = False
            elif(rectYVal>= 1300):#Win
                print("resetting...")
                rectYVal = -50
                pygame.mixer.Sound.play(win_sound)
                pygame.mixer.music.stop() 
        fallingGravity()   
        
        greenRect = pygame.Rect((greenRectXVal, rectYVal-400, 75, 25))
        if(moveLeft):
            greenRectXVal +=7#MOVE GREEN RECTANGLE
            if(greenRectXVal >=475):
                moveLeft = False
        else:
            greenRectXVal -= 7
            if(greenRectXVal <= 250):
                moveLeft = True
        
        
        time+=1
        realTime = time/20
        if(realTime % 2.0 == 0): 
            circColor = "blue"
            # pygame.draw.circle(screen, circColor, (400,400), 100, width=10)
        elif(realTime % 1.0 == 0):
            circColor = "red"
            # realTime = 0.0
            # pygame.draw.circle(screen, circColor, (400,400), 100, width=10)
        if(realTime % 0.25 == 0):
            gravity *= gravMultiple
        # print(gravity)
        # print(realTime)
        # print(rectYVal)
        
        clock.tick(20)
        # dt = pygame.time.Clock.get_time(clock) / 1000
        # print(dt)
        # print(f"fps: {pygame.time.Clock.get_fps(clock)}")
    else:
        gameScreen()
            
        
    pygame.display.update()
pygame.quit()
        