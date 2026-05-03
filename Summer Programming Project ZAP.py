import random
import time
import pygame
import math

pygame.init()

clock = pygame.time.Clock()

#instantiate constants
framerate = 360

#Login details
accounts = [["ZAP","123"],
            ["abc","321"],
            ["Thom","P4sw0rd"],
            ["Pl4y3r","No:1"],
            ["Username","Password"],
            ["31.12.23","Du3D4t3"],
            ["Python","3.12.1"],
            ["Pygame","2.5.2"],
            ["Winner","4tTH3T0p"],
            ["Michigan","M1cH1g4n"],
            ["Happy","NewYear"]]

#Initial colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
gold = (255,220,115)

#Pygame window instantiation
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("ZAP's Rolling Dice Game")
window.fill(white)

pygame.display.update()

#Lets pygame start here
for event in pygame.event.get():
    #When QUIT pressed
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()

#Text
letters = [
    ["a",5,[[-2],
          [1,0,0],
          [3,0],
          [1,0,0,0],
          [0,2,0],
          [0,2,0],
          [1,0,0,0]]],
    ["b",5,[[-1],
          [0],
          [0],
          [0],
          [0,0,0],
          [0,2,0],
          [0,2,0],
          [0,0,0]]],
    ["c",4,[[-4],
            [1,0,0],
            [0],
            [0],
            [1,0,0]]],
    ["d",5,[[-1],
            [3,0],
            [3,0],
            [3,0],
            [1,0,0,0],
            [0,2,0],
            [0,2,0],
            [1,0,0,0]]],
    ["e",5,[[-3],
            [1,0,0],
            [0,2,0],
            [0,0,0],
            [0],
            [1,0,0,0]]],
    ["f",5,[[-1],
            [2,0],
            [1,0,1,0],
            [1,0],
            [0,0,0],
            [1,0],
            [1,0],
            [1,0]]],
    ["g",5,[[-4],
            [1,0,0],
            [0,2,0],
            [0,2,0],
            [1,0,0,0],
            [3,0],
            [0,2,0],
            [1,0,0]]],
    ["h",5,[[-1],
            [0],
            [0],
            [0],
            [0,0,0],
            [0,2,0],
            [0,2,0],
            [0,2,0]]],
    ["i",2,[[-2],
            [0],
            [-1],
            [0],
            [0],
            [0],
            [0]]],
    ["j",4,[[-2],
            [2,0],
            [-1],
            [2,0],
            [2,0],
            [2,0],
            [2,0],
            [2,0],
            [2,0],
            [1,0]]],
    ["k",4,[[-1],
            [0],
            [0],
            [0],
            [0,1,0],
            [0,0],
            [0,1,0],
            [0,1,0]]],
    ["l",2,[[-1],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0]]],
    ["m",6,[[-4],
            [1,0,1,0],
            [0,1,0,1,0],
            [0,1,0,1,0],
            [0,3,0]]],
    ["n",5,[[-4],
            [1,0,0],
            [0,2,0],
            [0,2,0],
            [0,2,0]]],
    ["o",5,[[-4],
            [1,0,0],
            [0,2,0],
            [0,2,0],
            [1,0,0]]],
    ["p",5,[[-4],
            [1,0,0],
            [0,2,0],
            [0,2,0],
            [0,0,0],
            [0],
            [0],
            [0]]],
    ["q",5,[[-4],
            [1,0,0],
            [0,2,0],
            [0,2,0],
            [1,0,0,0],
            [3,0],
            [3,0],
            [3,0]]],
    ["r",4,[[-4],
            [1,0],
            [0,1,0],
            [0],
            [0]]],
    ["s",4,[[-3],
            [1,0,0],
            [0],
            [1,0],
            [2,0],
            [0,0]]],
    ["t",4,[[-2],
            [0],
            [0],
            [0,0,0],
            [0],
            [0],
            [1,0,0]]],
    ["u",5,[[-4],
            [0,2,0],
            [0,2,0],
            [0,2,0],
            [1,0,0]]],
    ["v",4,[[-4],
            [0,1,0],
            [0,1,0],
            [0,1,0],
            [1,0]]],
    ["w",6,[[-4],
            [0,3,0],
            [0,3,0],
            [0,1,0,1,0],
            [1,0,1,0]]],
    ["x",4,[[-5],
            [0,1,0],
            [1,0],
            [0,1,0]]],
    ["y",5,[[-4],
            [0,2,0],
            [0,2,0],
            [0,2,0],
            [1,0,0,0],
            [3,0],
            [0,2,0],
            [1,0,0]]],
    ["z",5,[[-4],
            [0,0,0,0],
            [2,0],
            [1,0],
            [0,0,0,0]]],
    ["A",6,[[1,0,0,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,0,0,0,0],
            [0,3,0],
            [0,3,0],
            [0,3,0]]],
    ["B",6,[[0,0,0,0],
            [0,3,0],
            [0,3,0],
            [0,0,0,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,0,0,0]]],
    ["C",6,[[1,0,0,0,0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [1,0,0,0,0]]],
    ["D",6,[[0,0,0],
            [0,2,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,2,0],
            [0,0,0]]],
    ["E",6,[[0,0,0,0,0],
            [0],
            [0],
            [0,0,0,0],
            [0],
            [0],
            [0],
            [0,0,0,0,0]]],
    ["F",6,[[0,0,0,0,0],
            [0],
            [0],
            [0,0,0,0],
            [0],
            [0],
            [0],
            [0]]],
    ["G",6,[[1,0,0,0,0],
            [0],
            [0],
            [0],
            [0,1,0,0,0],
            [0,3,0],
            [0,3,0],
            [1,0,0,0]]],
    ["H",6,[[0,3,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,0,0,0,0],
            [0,3,0],
            [0,3,0],
            [0,3,0]]],
    ["I",6,[[0,0,0,0,0],
            [2,0],
            [2,0],
            [2,0],
            [2,0],
            [2,0],
            [2,0],
            [0,0,0,0,0]]],
    ["J",6,[[0,0,0,0,0],
            [2,0],
            [2,0],
            [2,0],
            [2,0],
            [2,0],
            [0,1,0],
            [0,0,0]]],
    ["K",6,[[0,3,0],
            [0,3,0],
            [0,2,0],
            [0,2,0],
            [0,0,0],
            [0,2,0],
            [0,3,0],
            [0,3,0]]],
    ["L",6,[[0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0,0,0,0,0]]],
    ["M",6,[[0,3,0],
            [0,0,1,0,0],
            [0,1,0,1,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,3,0]]],
    ["N",7,[[0,4,0],
            [0,0,3,0],
            [0,1,0,2,0],
            [0,1,0,2,0],
            [0,2,0,1,0],
            [0,2,0,1,0],
            [0,3,0,0],
            [0,4,0]]],
    ["O",6,[[1,0,0,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [1,0,0,0]]],
    ["P",6,[[0,0,0,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,0,0,0],
            [0],
            [0],
            [0]]],
    ["Q",6,[[1,0,0,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,1,0,1,0],
            [0,2,0],
            [1,0,0,1,0]]],
    ["R",6,[[0,0,0,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,0,0,0],
            [0,3,0],
            [0,3,0],
            [0,3,0]]],
    ["S",6,[[1,0,0,0],
            [0,3,0],
            [0,4],
            [1,0,0,0],
            [4,0],
            [0,3,0],
            [0,3,0],
            [1,0,0,0]]],
    ["T",6,[[0,0,0,0,0],
            [2,0],
            [2,0],
            [2,0],
            [2,0],
            [2,0],
            [2,0],
            [2,0]]],
    ["U",6,[[0,3,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [1,0,0,0]]],
    ["V",6,[[0,3,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [1,0,1,0],
            [2,0]]],
    ["W",6,[[0,3,0],
            [0,3,0],
            [0,3,0],
            [0,3,0],
            [0,1,0,1,0],
            [0,1,0,1,0],
            [0,0,1,0,0],
            [0,3,0]]],
    ["X",6,[[0,3,0],
            [1,0,1,0],
            [1,0,1,0],
            [2,0],
            [2,0],
            [1,0,1,0],
            [1,0,1,0],
            [0,3,0]]],
    ["Y",6,[[0,3,0],
            [0,3,0],
            [1,0,1,0],
            [2,0],
            [2,0],
            [2,0],
            [2,0],
            [2,0]]],
    ["Z",6,[[0,0,0,0,0],
            [4,0],
            [3,0],
            [2,0],
            [2,0],
            [1,0],
            [0],
            [0,0,0,0,0]]],
    
    #NUMBERS
    ["1",4,[[1,0,],
            [0,0],
            [1,0],
            [1,0],
            [1,0],
            [1,0],
            [1,0],
            [0,0,0]]],
    ["2",5,[[1,0,0],
            [0,2,0],
            [0,2,0],
            [3,0],
            [2,0],
            [1,0],
            [0],
            [0,0,0,0]]],
    ["3",5,[[1,0,0],
            [0,2,0],
            [3,0],
            [1,0,0],
            [3,0],
            [3,0],
            [0,2,0],
            [1,0,0]]],
    ["4",5,[[0,2,0],
            [0,2,0],
            [0,2,0],
            [0,0,0,0],
            [3,0],
            [3,0],
            [3,0],
            [3,0]]],
    ["5",5,[[0,0,0,0],
            [0],
            [0],
            [0,0,0],
            [3,0],
            [0,2,0],
            [0,2,0],
            [1,0,0]]],
    ["6",5,[[1,0,0],
            [0,2,0],
            [0],
            [0,0,0],
            [0,2,0],
            [0,2,0],
            [0,2,0],
            [1,0,0]]],
    ["7",5,[[0,0,0,0],
            [3,0],
            [3,0],
            [2,0],
            [2,0],
            [1,0],
            [1,0],
            [1,0]]],
    ["8",5,[[1,0,0],
            [0,2,0],
            [0,2,0],
            [1,0,0],
            [0,2,0],
            [0,2,0],
            [0,2,0],
            [1,0,0]]],
    ["9",5,[[1,0,0],
            [0,2,0],
            [0,2,0],
            [1,0,0,0],
            [3,0],
            [3,0],
            [3,0],
            [3,0]]],
    ["0",5,[[1,0,0],
            [0,2,0],
            [0,2,0],
            [0,2,0],
            [0,2,0],
            [0,2,0],
            [0,2,0],
            [1,0,0]]],        
    
    #PUNCTUATION
    [" ",5,[]],
    [".",2,[[-7],
            [0]]],
    ["!",2,[[-1],
            [0],
            [0],
            [0],
            [0],
            [0],
            [-1],
            [0]]],
    ["?",4,[[-1],
            [1,0],
            [0,1,0],
            [2,0],
            [1,0],
            [1,0],
            [1],
            [1,0]]],
    [",",3,[[-6],
            [1,0],
            [1,0],
            [0]]],
    [";",3,[[-2],
            [1,0],
            [-3],
            [1,0],
            [0]]],
    [":",2,[[-2],
            [0],
            [-3],
            [0]]],
    ["'",3,[[-1],
            [1,0],
            [1,0],
            [0]]],
    ['"',4,[[-1],
            [0,1,0],
            [0,1,0],
            [0,1,0]]],
    ["-",4,[[-4],
            [0,0,0]]],
    ["+",4,[[-3],
            [1,0],
            [0,0,0],
            [1,0]]],
    ["(",4,[[2,0],
            [1,0],
            [0],
            [0],
            [0],
            [0],
            [1,0],
            [2,0]]],
    [")",4,[[0],
            [1,0],
            [2,0],
            [2,0],
            [2,0],
            [2,0],
            [1,0],
            [0]]],   
    
    #TOP CUT OFF:
    ["b_cut",5,[[-2],
          [0],
          [0],
          [0,0,0],
          [0,2,0],
          [0,2,0],
          [0,0,0]]],
    ["h_cut",5,[[-2],
            [0],
            [0],
            [0,0,0],
            [0,2,0],
            [0,2,0],
            [0,2,0]]],
    ["k_cut",4,[[-2],
            [0],
            [0],
            [0,1,0],
            [0,0],
            [0,1,0],
            [0,1,0]]],
    ["l_cut",2,[[-2],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0]]],
    ]

#Icons
icons = [["lock",7,[[2,0,0,0],
           [2,0,1,0],
           [0,0,0,0,0,0,0],
           [0,0,3,0,0],
           [0,0,3,0,0],
           [0,0,3,0,0],
           [0,0,0,1,0,0,0],
           [0,0,0,1,0,0,0],
           [0,0,0,0,0,0,0]]],
         
         ["unlock",7,[[2,0,0,0],
           [2,0,1,0],
           [4,0],
           [0,0,0,0,0,0,0],
           [0,0,3,0,0],
           [0,0,3,0,0],
           [0,0,3,0,0],
           [0,0,0,1,0,0,0],
           [0,0,0,1,0,0,0],
           [0,0,0,0,0,0,0]]],           
                    
         #The largest width is 7 pixels, the largest height is 11 pixels
         ["blank",7,[[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]]],
         
         ["textCursor",2,[[0,0],
                        [0,0],
                        [0,0],
                        [0,0],
                        [0,0],
                        [0,0],
                        [0,0],
                        [0,0]]]
           ]

#Compatible Letters - prevents large gaps in text

#Can be nestled with the f (1 space left)
canNestle_f = ["a","c","d","e","g","m","n","o","p","q","r","s","u","v","w","x","y","z"]
#Cuts off the j while nestling (j moves 2 spaces left, most leftward pixel removed)
cuts_j = ["g","j","q"]
#Where uppercases can nestle with lowercases
canNestle_upper = ["J","T"]
#Where the topmost pixel is removed to do so - f cannot be nestled
cuts_lower = ["b","h","k","l"]

#Draws a rectangle - convenience
def DrawRect(color,position,dimensions):
    pygame.draw.rect(window,color,(position,dimensions))
    
#Draws text, icons or an outline box
def Draw(string,color,position,scale,setting,delayType = 1, centralizeX = False, leftMost = 0, rightMost = 500):

    #Variables
    originalPos = position
    pos = position
    count = 0
    drawDelay = 0.005
    cutJ = False
    nestleUpper = False
    cutsLower = False

    #To see if an animation style is wanted
    #Draws with drawing animation
    if delayType == 1:
        
        #Draws Text
        if setting == "text":

            #Horizontally centralises text
            if centralizeX:
                #Length of text
                
                length = 0
                for character in string:
                    #Finds character's length for size 1
                    for value in letters:
                        if value[0] == character:
                            pixelLength = value[1]
                            break
                        
                    #Adds actual length to total length
                    length += pixelLength * scale

                #Accounts for unnecessary space at the end
                length -= scale

                #Calculate position
                middle = leftMost + (rightMost - leftMost)/2
                xPos = middle - length/2

                #Update position
                position = (xPos,position[1])
                originalPos = position
                pos = position
            
            #Runs for each character
            for character in string:
                
                #Finds character's location in list
                
                for value in letters:

                    #If letter needs to be cut off the top, adds "_cut" suffix
                    if cutsLower == True:
                        character += "_cut"
                        if value[0] == character:
                            index = letters.index(value)
                            character = character[0]
                            break
                        cutsLower = False
                        
                    #Find letter normally
                    if value[0] == character:
                        index = letters.index(value)
                        break
                
                #Nestling j - moves two left
                if (character == "j") & (count != 0):
                    pos = (pos[0] - 2 * scale, pos[1])
                    originalPos = (originalPos[0] - 2 * scale, originalPos[1])
                    
                #Draws pixels
                for value in letters[index][2]:

                    for val in value:
                        clock.tick(framerate)
                        #When rows are empty
                        if val < 0:
                            pos = (pos[0],pos[1] - (1 + val) * scale)
                            
                        #When there needs to be a pixel
                        elif val == 0:
                            DrawRect(color,(pos[0],pos[1]),(scale,scale))
                            pos = (pos[0] + scale, pos[1])
                            pygame.display.update()
                            time.sleep(drawDelay)
                            
                        #When there is a line of empty spaces
                        else:
                            pos = (pos[0] + val * scale,pos[1])
                            
                    pos = (originalPos[0],pos[1] + scale)

                #Alters next letter based on current letter   
                try:
                    #Nestling with f
                    if (character == "f") & (string[count + 1] in canNestle_f):
                        #Moves next letter 1 left
                        originalPos = (originalPos[0] + (letters[index][1] - 1) * scale, originalPos[1])

                    #Nestling with J or T
                    elif (character in canNestle_upper) & (string[count+1] != "f") & (string[count+1].islower()):
                        #Marks that the next letter needs to be cut
                        if string[count+1] in cuts_lower:
                            cutsLower = True
                            
                        #Moves next letter 2 left
                        originalPos = (originalPos[0] + (letters[index][1] - 2) * scale, originalPos[1])
                        
                    else:
                        #Leaves a 1 pixel gap
                        originalPos = (originalPos[0] + letters[index][1] * scale, originalPos[1])
                except:
                    #End of string
                    pass

                pos = originalPos
                count += 1

        #To draw an image AKA icon
        elif setting == "icon":          
                
            for val in icons:
                if val[0] == string:
                    index = icons.index(val)

            #Centralizes icon horizontally
            if centralizeX:

                #Calculates position
                middle = leftMost + (rightMost - leftMost)/2
                length = icons[index][1]
                xPos = middle - length/2

                #Updates positions
                position = (xPos,position[1])
                originalPos = position
                pos = position

            #Draws icon
            values = icons[index][2]
            for value in values:
                for val in value:
                    clock.tick(framerate)
                #When rows are empty
                    if val < 0:
                        pos = (pos[0],pos[1] - (1 + val) * scale)
                    #When there needs to be a pixel
                        
                    elif val == 0:
                        DrawRect(color,(pos[0],pos[1]),(scale,scale))
                        pos = (pos[0] + scale, pos[1])
                        pygame.display.update()
                        time.sleep(drawDelay)
                            
                    #When there is a line of empty spaces
                    else:
                        pos = (pos[0] + val * scale,pos[1])
                        
                pos = (originalPos[0],pos[1] + scale)
                
        #To draw a hollow rectangle
        elif setting == "box":
            #Gets values where "x' indicates the separation
            posX = string.index("x")
            lengthX = int(string[:posX])
            heightY = int(string[posX+1:])
            
            #top
            for value in range(0,lengthX):
                clock.tick(framerate)
                DrawRect(color,(pos[0] + value * scale,pos[1]),(scale,scale))
                pygame.display.update()
                
            #right
            for value in range(0,heightY):
                clock.tick(framerate)
                DrawRect(color,(pos[0] + (lengthX - 1) * scale, pos[1] + value * scale), (scale,scale))
                pygame.display.update()
            
            #bottom
            for value in range(0,lengthX):
                clock.tick(framerate)
                DrawRect(color,(pos[0] + (lengthX - 1) * scale - value * scale, pos[1] + (heightY - 1) * scale),(scale,scale))
                pygame.display.update()

            #left
            for value in range(0, heightY):
                clock.tick(framerate)
                DrawRect(color,(pos[0], pos[1] + (heightY - 1) * scale - value * scale), (scale,scale))
                pygame.display.update()
                
    #Draws with typing delay
    elif delayType == 2:
        #Draws text
        if setting == "text":
            
            #Horizontally centralises text
            if centralizeX:
                #Length of text
                length = 0
                
                for character in string:
                    #Finds character's length for size 1
                    for value in letters:
                        if value[0] == character:
                            pixelLength = value[1]
                            break

                    #Adds actual length to total length
                    length += pixelLength * scale

                #Accounts for unnecessary space at the end
                length -= scale

                #Calculates position
                middle = leftMost + (rightMost - leftMost)/2
                xPos = middle - length/2

                #Updates position
                position = (xPos,position[1])
                originalPos = position
                pos = position

            #Runs for each character
            for character in string:
                
                #Finds character's location in list
                for value in letters:

                    #If letter needs to be cut off the top
                    if cutsLower == True:
                        character += "_cut"
                        if value[0] == character:
                            index = letters.index(value)
                            character = character[0]
                            break
                        cutsLower = False
                        
                    #Find letter normally
                    if value[0] == character:
                        index = letters.index(value)
                        break

                #Nestling j
                if (character == "j") & (count != 0):
                    pos = (pos[0] - 2 * scale, pos[1])
                    originalPos = (originalPos[0] - 2 * scale, originalPos[1])

                #Draws pixels
                for value in letters[index][2]:

                    for val in value:
                    #When rows are empty
                        clock.tick(framerate)
                        if val < 0:
                            pos = (pos[0],pos[1] - (1 + val) * scale)
                            
                        #When there needs to be a pixel
                        elif val == 0:
                            DrawRect(color,(pos[0],pos[1]),(scale,scale))
                            pos = (pos[0] + scale, pos[1])
                            
                        #When there is a line of empty spaces
                        else:
                            pos = (pos[0] + val * scale,pos[1])
                            
                    pos = (originalPos[0],pos[1] + scale)

                #Updates display letter by letter
                pygame.display.update()
                
                #Alters next letter based on current letter   
                try:
                    #Nestling with f
                    if (character == "f") & (string[count + 1] in canNestle_f):
                        #Moves next letter 1 left
                        originalPos = (originalPos[0] + (letters[index][1] - 1) * scale, originalPos[1])

                    #Nestling with J T
                    elif (character in canNestle_upper) & (string[count+1] != "f") & (string[count+1].islower()):
                        #Marks that the next letter needs to be cut
                        if string[count+1] in cuts_lower:
                            cutsLower = True
                            
                        #Moves next letter 2 left
                        originalPos = (originalPos[0] + (letters[index][1] - 2) * scale, originalPos[1])
                        
                    else:
                        #Leaves a 1 pixel gap
                        originalPos = (originalPos[0] + letters[index][1] * scale, originalPos[1])
                except:
                    #End of string
                    pass

                pos = originalPos
                count += 1

        #Draws an icon
        elif setting == "icon":
            for val in icons:
                if val[0] == string:
                    index = icons.index(val)

            #Centralizes icon horizontally
            if centralizeX:

                #Calculates position
                middle = leftMost + (rightMost - leftMost)/2
                length = icons[index][1]
                xPos = middle - length/2

                #Updayes positions
                position = (xPos,position[1])
                originalPos = position
                pos = position

            values = icons[index][2]

            #Draws icon
            for value in values:
                for val in value:
                    clock.tick(framerate)
                    #When rows are empty
                    if val < 0:
                        pos = (pos[0],pos[1] - (1 + val) * scale)
                        
                    #When there needs to be a pixel
                    elif val == 0:
                        DrawRect(color,(pos[0],pos[1]),(scale,scale))
                        pos = (pos[0] + scale, pos[1])
                        
                    #When there is a line of empty spaces
                    else:
                        pos = (pos[0] + val * scale,pos[1])
                        
                pos = (originalPos[0],pos[1] + scale)

            pygame.display.update()
            
        #To draw a hollow rectangle
        elif setting == "box":
            #Gets values where "x" shows the separation
            posX = string.index("x")
            lengthX = int(string[:posX])
            heightY = int(string[posX+1:])
            
            #top
            for value in range(0,lengthX):
                clock.tick(framerate)
                DrawRect(color,(pos[0] + value * scale,pos[1]),(scale,scale))
                
            #right
            for value in range(0,heightY):
                clock.tick(framerate)
                DrawRect(color,(pos[0] + (lengthX - 1) * scale, pos[1] + value * scale), (scale,scale))
            
            #bottom
            for value in range(0,lengthX):
                clock.tick(framerate)
                DrawRect(color,(pos[0] + (lengthX - 1) * scale - value * scale, pos[1] + (heightY - 1) * scale),(scale,scale))

            #left
            for value in range(0, heightY):
                clock.tick(framerate)
                DrawRect(color,(pos[0], pos[1] + (heightY - 1) * scale - value * scale), (scale,scale))

            pygame.display.update()

    #Draws without delay
    else:
        #Draws text
        if setting == "text":
            
            #Horizontally centralises text
            if centralizeX:
                #Length of text
                length = 0
                
                for character in string:
                    #Finds character's length for size 1
                    for value in letters:
                        if value[0] == character:
                            pixelLength = value[1]
                            break

                    #Adds actual length to total length
                    length += pixelLength * scale

                #Accounts for unnecessary space at the end
                length -= scale

                #Calculates position
                middle = leftMost + (rightMost - leftMost)/2
                xPos = middle - length/2

                #Updates position
                position = (xPos,position[1])
                originalPos = position
                pos = position

            #Runs for each character
            for character in string:
                
                #Finds character's location in list
                for value in letters:

                    #If letter needs to be cut off the top
                    if cutsLower == True:
                        character += "_cut"
                        if value[0] == character:
                            index = letters.index(value)
                            character = character[0]
                            break
                        cutsLower = False
                        
                    #Find letter normally
                    if value[0] == character:
                        index = letters.index(value)
                        break

                #Nestling j
                if (character == "j") & (count != 0):
                    pos = (pos[0] - 2 * scale, pos[1])
                    originalPos = (originalPos[0] - 2 * scale, originalPos[1])

                #Draws pixels
                for value in letters[index][2]:

                    for val in value:
                    #When rows are empty
                        if val < 0:
                            pos = (pos[0],pos[1] - (1 + val) * scale)
                            
                        #When there needs to be a pixel
                        elif val == 0:
                            DrawRect(color,(pos[0],pos[1]),(scale,scale))
                            pos = (pos[0] + scale, pos[1])
                            
                        #When there is a line of empty spaces
                        else:
                            pos = (pos[0] + val * scale,pos[1])
                            
                    pos = (originalPos[0],pos[1] + scale)

                #Updates display letter by letter
                pygame.display.update()
                
                #Alters next letter based on current letter   
                try:
                    #Nestling with f
                    if (character == "f") & (string[count + 1] in canNestle_f):
                        #Moves next letter 1 left
                        originalPos = (originalPos[0] + (letters[index][1] - 1) * scale, originalPos[1])

                    #Nestling with J T
                    elif (character in canNestle_upper) & (string[count+1] != "f") & (string[count+1].islower()):
                        #Marks that the next letter needs to be cut
                        if string[count+1] in cuts_lower:
                            cutsLower = True
                            
                        #Moves next letter 2 left
                        originalPos = (originalPos[0] + (letters[index][1] - 2) * scale, originalPos[1])
                        
                    else:
                        #Leaves a 1 pixel gap
                        originalPos = (originalPos[0] + letters[index][1] * scale, originalPos[1])
                except:
                    #End of string
                    pass

                pos = originalPos
                count += 1

        #Draws an icon
        elif setting == "icon":
            for val in icons:
                if val[0] == string:
                    index = icons.index(val)

            #Centralizes icon horizontally
            if centralizeX:

                #Calculates position
                middle = leftMost + (rightMost - leftMost)/2
                length = icons[index][1]
                xPos = middle - length/2

                #Updayes positions
                position = (xPos,position[1])
                originalPos = position
                pos = position

            values = icons[index][2]

            #Draws icon
            for value in values:
                for val in value:
                    #When rows are empty
                    if val < 0:
                        pos = (pos[0],pos[1] - (1 + val) * scale)
                        
                    #When there needs to be a pixel
                    elif val == 0:
                        DrawRect(color,(pos[0],pos[1]),(scale,scale))
                        pos = (pos[0] + scale, pos[1])
                        
                    #When there is a line of empty spaces
                    else:
                        pos = (pos[0] + val * scale,pos[1])
                        
                pos = (originalPos[0],pos[1] + scale)

            pygame.display.update()
            
        #To draw a hollow rectangle
        elif setting == "box":
            #Gets values where "x" shows the separation
            posX = string.index("x")
            lengthX = int(string[:posX])
            heightY = int(string[posX+1:])
            
            #top
            for value in range(0,lengthX):
                DrawRect(color,(pos[0] + value * scale,pos[1]),(scale,scale))
                
            #right
            for value in range(0,heightY):
                DrawRect(color,(pos[0] + (lengthX - 1) * scale, pos[1] + value * scale), (scale,scale))
            
            #bottom
            for value in range(0,lengthX):
                DrawRect(color,(pos[0] + (lengthX - 1) * scale - value * scale, pos[1] + (heightY - 1) * scale),(scale,scale))

            #left
            for value in range(0, heightY):
                DrawRect(color,(pos[0], pos[1] + (heightY - 1) * scale - value * scale), (scale,scale))

            pygame.display.update()
            
    pygame.display.update()
    
#Collects text input from player,returns to variable and outputs to display
def InputToDisplay(topLeft,size,maxLength):
    #Instantiate Variables
    string = ""
    enter = False
    currentPos = topLeft
    tCpos = (currentPos[0] - 2,currentPos[1] + 6)
    
    #Collecting inputs
    while not enter:
        clock.tick(framerate)
        Draw("textCursor",white,tCpos,4,"icon",0)
        
        for event in pygame.event.get():
            #When QUIT pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            #For any key
            elif event.type == pygame.KEYDOWN:
                #To ENTER text
                if event.key == pygame.K_RETURN:
                    enter = True
                    
                #To add characters to string
                elif event.key == pygame.K_BACKSPACE:
                    try:
                        #Get last character
                        character = string[-1]
                        
                        #Remove it
                        for values in letters:
                            if values[0] == character:
                                currentPos = (currentPos[0] - values[1] * size,currentPos[1])
                                tCpos = (currentPos[0] - 2, currentPos[1] + 6)
                                DrawRect(white,currentPos,(values[1]*size,11*size))
                                maxLength += values[1] * size

                                pygame.display.update()
                                break
                            
                                
                        #Remove character from string
                        if len(string) == 1:
                            string = ""
                            
                        string = string[:-1]
                        
                    except:
                        #There are no characters
                        pass
                    
                #Else can be used as commands do not return a string unicode
                else:
                    #Find added character's length
                    for values in letters:
                        if values[0] == event.unicode:
                            if values[1] * size <= maxLength:
                                currentPos = (currentPos[0]+values[1]*size,currentPos[1])
                                tCpos = (currentPos[0] - 2, currentPos[1] + 6)
                                maxLength -= values[1] * size
                                #Add character to string
                                string += event.unicode
                                break
                            else:
                                #Not enough space symbolised by red cursor
                                Draw("textCursor",red,tCpos,4,"icon",0)
                        
            #Redraw text
            if(string == ""):
                Draw("blank",white,(topLeft),size,"icon",0)
            else:
                Draw(string,green,(topLeft),size,"text",0)

        #Visual indication of where text is being typed
        time.sleep(0.2)
        Draw("textCursor",black,tCpos,4,"icon",0)
        time.sleep(0.2)

    #When entered - symbolized by blue color
    Draw("textCursor",blue,tCpos,4,"icon",0)
    time.sleep(0.5)
    Draw("textCursor",white,tCpos,4,"icon",0)

    Draw("46x15",blue,(topLeft[0]-15,topLeft[1]-10),5,"box")
    Draw(string,blue,(topLeft),size,"text",0)

    return string

#Creates a single input button
def Button(centre, radius, color, returnValue, text, size):
    #Visual button on display
    pygame.draw.circle(window, color, centre, radius)
    diameter = (centre[0] - radius, centre[0] + radius)
    Draw(text,white,(0,centre[1] - 4 * size),size,"text",0,True,diameter[0],diameter[1])
    
    while True:
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()

                #Calculates distance using Pythagoras
                deltaX = centre[0] - mousePos[0]
                deltaY = centre[1] - mousePos[1]

                distance = round(math.sqrt(deltaX ** 2 + deltaY ** 2),2)

                if distance <= radius:

                    #Darkens button color as visual indicator
                    darkerColor =  (color[0] - 100, color[1] - 100, color[2] - 100)

                    if darkerColor[0] < 0:
                        darkerColor = (0,darkerColor[1],darkerColor[2])
                    if darkerColor[1] < 0:
                        darkerColor = (darkerColor[0],0,darkerColor[2])
                    if darkerColor[2] < 0:
                        darkerColor = (darkerColor[0],darkerColor[1],0)
                        
                    pygame.draw.circle(window, darkerColor, centre, radius)
                    Draw(text,white,(0,centre[1] - 4 * size),size,"text",2,True,diameter[0],diameter[1])

                    return returnValue

#Uses two input buttons for a choice answer - usually yes or no
def TwoButtons(centreA, centreB, radiusA, colorA, colorB, textA, textB, sizeA, textColorA = white, textColorB = None,
                radiusB = None, sizeB = None, returnValueA = 0, returnValueB = 1):

    #Default values
    if radiusB == None:
        radiusB = radiusA
    if sizeB == None:
        sizeB = sizeA
    if textColorB == None:
        textColorB = textColorA

    #Display output
    pygame.draw.circle(window, colorA, centreA, radiusA)
    pygame.draw.circle(window,colorB, centreB, radiusB)

    diameterA = (centreA[0] - radiusA, centreA[0] + radiusA)
    diameterB = (centreB[0] - radiusB, centreB[0] + radiusB)
    
    Draw(textA,textColorA,(centreA,centreA[1] - 4 * sizeA),sizeA,"text",0,True,diameterA[0],diameterA[1])
    Draw(textB,textColorB,(centreB,centreB[1] - 4 * sizeB),sizeB,"text",0,True,diameterB[0],diameterB[1])

    #Waiting for input
    while(True):
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()  

                #Calculates distance from first button
                deltaX = centreA[0] - mousePos[0]
                deltaY = centreA[1] - mousePos[1]

                distance = round(math.sqrt(deltaX ** 2 + deltaY ** 2))

                if distance <= radiusA:
                    #Darkens button color as visual indicator
                    darkerColor =  (colorA[0] - 100, colorA[1] - 100, colorA[2] - 100)

                    if darkerColor[0] < 0:
                        darkerColor = (0,darkerColor[1],darkerColor[2])
                    if darkerColor[1] < 0:
                        darkerColor = (darkerColor[0],0,darkerColor[2])
                    if darkerColor[2] < 0:
                        darkerColor = (darkerColor[0],darkerColor[1],0)
                        
                    pygame.draw.circle(window, darkerColor, centreA, radiusA)
                    Draw(textA,textColorA,(centreA,centreA[1] - 4 * sizeA),sizeA,"text",2,True,diameterA[0],diameterA[1])
                    
                    return returnValueA
                
                else:
                    #Calculates difference from second button
                    deltaX = centreB[0] - mousePos[0]
                    deltaY = centreB[1] - mousePos[1]

                    distance = round(math.sqrt(deltaX ** 2 + deltaY ** 2))
                    
                    if distance <= radiusB:
                        #Darkens button color as visual indicator
                        darkerColor =  (colorB[0] - 100, colorB[1] - 100, colorB[2] - 100)

                        if darkerColor[0] < 0:
                            darkerColor = (0,darkerColor[1],darkerColor[2])
                        if darkerColor[1] < 0:
                            darkerColor = (darkerColor[0],0,darkerColor[2])
                        if darkerColor[2] < 0:
                            darkerColor = (darkerColor[0],darkerColor[1],0)
                            
                        pygame.draw.circle(window, darkerColor, centreB, radiusB)
                        Draw(textB,textColorB,(centreB,centreB[1] - 4 * sizeB),sizeB,"text",2,True,diameterB[0],diameterB[1])
                        
                        return returnValueB

#Checks login details
def Login(usernameTopLeft, passwordTopLeft, size, maxLength, exceptIndex = None):
    
    username = InputToDisplay(usernameTopLeft, size, maxLength)
    #Turns blue once entered
    Draw("Username:",blue,(usernameTopLeft[0] - 5, usernameTopLeft[1] - 55),5,"text",2)
    
    password = InputToDisplay(passwordTopLeft, size, maxLength)
    #Turns blue ones entered
    Draw("Password:",blue,(passwordTopLeft[0] - 5, passwordTopLeft[1] - 55),5,"text",2)

    try:
        #Returns an error when not in list
        index = accounts.index([username,password])

        #Prevents the same user playing themself
        if(index == exceptIndex):
            return 1/0

        #Green symbolizes correct
        Draw("Username:",green,(usernameTopLeft[0] - 5, usernameTopLeft[1] - 55),5,"text",2)     
        Draw("46x15",green,(usernameTopLeft[0]-15,usernameTopLeft[1]-10),5,"box")
        Draw(username,green,(usernameTopLeft),size,"text",2)

        #Green symbolizes correct
        Draw("Password:",green,(passwordTopLeft[0] - 5, passwordTopLeft[1] - 55),5,"text",2)  
        Draw("46x15",green,(passwordTopLeft[0]-15,passwordTopLeft[1]-10),5,"box")
        Draw(password,green,(passwordTopLeft),size,"text",2)
        
        return index            
    
    except:
        #Incorrect username or password
        Draw(username,red,(usernameTopLeft),size,"text",2)
        Draw(password,red,(passwordTopLeft),size,"text",2)

        DrawRect(white,usernameTopLeft,(210,55))
        DrawRect(white,passwordTopLeft,(210,55))

        Draw("Username:",red,(usernameTopLeft[0] - 5, usernameTopLeft[1] - 55),5,"text",2)
        Draw("46x15",red,(usernameTopLeft[0]-15,usernameTopLeft[1]-10),5,"box")
        
        Draw("Password:",red,(passwordTopLeft[0] - 5, passwordTopLeft[1] - 55),5,"text",2)
        Draw("46x15",red,(passwordTopLeft[0]-15,passwordTopLeft[1]-10),5,"box")

#Waits for specified key input - usually SPACE
def WaitForInputKey(awaitedInputKey):

    a = True
    while a:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == awaitedInputKey:
                    a = False

#Nice little animation when changing the scores
def ChangeScoreAnimation(text,color,scoreColor,size,score,minX,maxX):

    #y = 310 ---> 180
    yVal = 310
    while yVal > 210:
        Draw(text,white,(25,yVal),size,"text",0,True,minX,maxX)
        Draw(str(score),scoreColor,(25,170),10,"text",0,True,minX,maxX)
        
        yVal -= 10
        
        Draw(text,color,(25,yVal),size,"text",0,True,minX,maxX)
        
        time.sleep(0.1)
        
        pygame.display.update()

#Object storing player values
class Player:
    def __init__(self,name):
        self.name = name
        self.die1 = None
        self.die2 = None
        self.score = 0

#Object for rendering die
class Die():
    def __init__(self,centre,length,initialRotation,lineColor,baseColor = white):
        
        #When values are updated
        try:
            self.erase()
        except:
            #When first instantiated
            pass
        
        self.centre = centre
        self.length = length
        self.initialRotation = initialRotation
        self.lineColor = lineColor
        self.baseColor = baseColor
        self.rotation = (0,0,0)
        
        self.calcPoints(self.centre, self.length)

        self.rotate(initialRotation)
        
        self.update()

    def calcPoints(self, centre, length):
        
        self.ftl = (centre[0]-length/2,centre[1]-length/2,centre[2]+length/2) #FrontTopLeft
        self.ftr = (centre[0]+length/2,centre[1]-length/2,centre[2]+length/2) #FrontTopRight
        self.fbl = (centre[0]-length/2,centre[1]+length/2,centre[2]+length/2) #FrontBottomLeft
        self.fbr = (centre[0]+length/2,centre[1]+length/2,centre[2]+length/2) #FrontBottomRight
        self.btl = (centre[0]-length/2,centre[1]-length/2,centre[2]-length/2) #BackTopLeft
        self.btr = (centre[0]+length/2,centre[1]-length/2,centre[2]-length/2) #BackTopRight
        self.bbl = (centre[0]-length/2,centre[1]+length/2,centre[2]-length/2) #BackBottomLeft
        self.bbr = (centre[0]+length/2,centre[1]+length/2,centre[2]-length/2) #BackBottomRight

        pitLength = length/9
        
        self.one = [
                # Front face Middle
                [
                    (self.ftl[0] + 4 * pitLength, self.ftl[1] + 4 * pitLength, self.ftl[2]),
                    (self.ftl[0] + 5 * pitLength, self.ftl[1] + 4 * pitLength, self.ftl[2]),
                    (self.ftl[0] + 5 * pitLength, self.ftl[1] + 5 * pitLength, self.ftl[2]),
                    (self.ftl[0] + 4 * pitLength, self.ftl[1] + 5 * pitLength, self.ftl[2]),
                ]
            ]
        
        self.two = [
                # Right face TopRight
                [
                    (self.ftr[0], self.ftr[1] + pitLength, self.ftr[2] - 7 * pitLength),
                    (self.ftr[0], self.ftr[1] + pitLength, self.ftr[2] - 8 * pitLength),
                    (self.ftr[0], self.ftr[1] + 2 * pitLength, self.ftr[2] - 8 * pitLength),
                    (self.ftr[0], self.ftr[1] + 2 * pitLength, self.ftr[2] - 7 * pitLength)
                ],
                # Right face BottomLeft
                [
                    (self.ftr[0], self.ftr[1] + 7 * pitLength, self.ftr[2] - pitLength),
                    (self.ftr[0], self.ftr[1] + 7 * pitLength, self.ftr[2] - 2 * pitLength),
                    (self.ftr[0], self.ftr[1] + 8 * pitLength, self.ftr[2] - 2 * pitLength),
                    (self.ftr[0], self.ftr[1] + 8 * pitLength, self.ftr[2] - pitLength)
                ]
            ]
            
        self.three = [
                # Top face BottomLeft
                [
                    (self.ftl[0] + pitLength, self.ftl[1], self.ftl[2] - pitLength),
                    (self.ftl[0] + pitLength, self.ftl[1], self.ftl[2] - 2 * pitLength),
                    (self.ftl[0] + 2 * pitLength, self.ftl[1], self.ftl[2] - 2 * pitLength),
                    (self.ftl[0] + 2 * pitLength, self.ftl[1], self.ftl[2] - pitLength) 
                ],
                # Top face Middle
                [
                    (self.ftl[0] + 4 * pitLength, self.ftl[1], self.ftl[2] - 4 * pitLength),
                    (self.ftl[0] + 4 * pitLength, self.ftl[1], self.ftl[2] - 5 * pitLength),
                    (self.ftl[0] + 5 * pitLength, self.ftl[1], self.ftl[2] - 5 * pitLength),
                    (self.ftl[0] + 5 * pitLength, self.ftl[1], self.ftl[2] - 4 * pitLength),  
                ],
                # Top face TopRight
                [
                    (self.ftl[0] + 7 * pitLength, self.ftl[1], self.ftl[2] - 7 * pitLength),
                    (self.ftl[0] + 7 * pitLength, self.ftl[1], self.ftl[2] - 8 * pitLength),
                    (self.ftl[0] + 8 * pitLength, self.ftl[1], self.ftl[2] - 8 * pitLength),
                    (self.ftl[0] + 8 * pitLength, self.ftl[1], self.ftl[2] - 7 * pitLength),
                ]
            ]
        
        self.four = [
                #Bottom face TopLeft
                [
                    (self.bbl[0] + pitLength, self.bbl[1], self.bbl[2] + 7 * pitLength),
                    (self.bbl[0] + pitLength, self.bbl[1], self.bbl[2] + 8 * pitLength),
                    (self.bbl[0] + 2 * pitLength, self.bbl[1], self.bbl[2] + 8 * pitLength),
                    (self.bbl[0] + 2 * pitLength, self.bbl[1], self.bbl[2] + 7 * pitLength),
                ],
                #Bottom face TopRight
                [
                    (self.bbl[0] + 7 * pitLength, self.bbl[1], self.bbl[2] + 7 * pitLength),
                    (self.bbl[0] + 7 * pitLength, self.bbl[1], self.bbl[2] + 8 * pitLength),
                    (self.bbl[0] + 8 * pitLength, self.bbl[1], self.bbl[2] + 8 * pitLength),
                    (self.bbl[0] + 8 * pitLength, self.bbl[1], self.bbl[2] + 7 * pitLength),
                ],
                #Bottom face BottomLeft
                [
                    (self.bbl[0] + pitLength, self.bbl[1], self.bbl[2] + pitLength),
                    (self.bbl[0] + pitLength, self.bbl[1], self.bbl[2] + 2 * pitLength),
                    (self.bbl[0] + 2 * pitLength, self.bbl[1], self.bbl[2] + 2 * pitLength),
                    (self.bbl[0] + 2 * pitLength, self.bbl[1], self.bbl[2] + pitLength),
                ],
                #Bottom face BottomRigt
                [
                    (self.bbl[0] + 7 * pitLength, self.bbl[1], self.bbl[2] + pitLength),
                    (self.bbl[0] + 7 * pitLength, self.bbl[1], self.bbl[2] + 2 * pitLength),
                    (self.bbl[0] + 8 * pitLength, self.bbl[1], self.bbl[2] + 2 * pitLength),
                    (self.bbl[0] + 8 * pitLength, self.bbl[1], self.bbl[2] + pitLength),
                ],
            ]
                
        self.five = [
                #Left face BottomLeft
                [
                    (self.bbl[0], self.bbl[1] - pitLength, self.bbl[2] + pitLength),
                    (self.bbl[0], self.bbl[1] - pitLength, self.bbl[2] + 2 * pitLength),
                    (self.bbl[0], self.bbl[1] - 2 * pitLength, self.bbl[2] + 2 * pitLength),
                    (self.bbl[0], self.bbl[1] - 2 * pitLength, self.bbl[2] + pitLength),
                ],
                #Left face BottomRight
                [
                    (self.bbl[0], self.bbl[1] - pitLength, self.bbl[2] + 7 * pitLength),
                    (self.bbl[0], self.bbl[1] - pitLength, self.bbl[2] + 8 * pitLength),
                    (self.bbl[0], self.bbl[1] - 2 * pitLength, self.bbl[2] + 8 * pitLength),
                    (self.bbl[0], self.bbl[1] - 2 * pitLength, self.bbl[2] + 7 * pitLength),
                ],
                #Left face TopLeft
                [
                    (self.bbl[0], self.bbl[1] - 7 * pitLength, self.bbl[2] + pitLength),
                    (self.bbl[0], self.bbl[1] - 7 * pitLength, self.bbl[2] + 2 * pitLength),
                    (self.bbl[0], self.bbl[1] - 8 * pitLength, self.bbl[2] + 2 * pitLength),
                    (self.bbl[0], self.bbl[1] - 8 * pitLength, self.bbl[2] + pitLength),
                ],
                #Left face TopRight
                [
                    (self.bbl[0], self.bbl[1] - 7 * pitLength, self.bbl[2] + 7 * pitLength),
                    (self.bbl[0], self.bbl[1] - 7 * pitLength, self.bbl[2] + 8 * pitLength),
                    (self.bbl[0], self.bbl[1] - 8 * pitLength, self.bbl[2] + 8 * pitLength),
                    (self.bbl[0], self.bbl[1] - 8 * pitLength, self.bbl[2] + 7 * pitLength),
                ],
                #Left face Middle
                [
                    (self.bbl[0], self.bbl[1] - 4 * pitLength, self.bbl[2] + 4 * pitLength),
                    (self.bbl[0], self.bbl[1] - 4 * pitLength, self.bbl[2] + 5 * pitLength),
                    (self.bbl[0], self.bbl[1] - 5 * pitLength, self.bbl[2] + 5 * pitLength),
                    (self.bbl[0], self.bbl[1] - 5 * pitLength, self.bbl[2] + 4 * pitLength),
                ]
            ]
        
        self.six = [
                #Back face BottomLeft
                [
                    (self.bbr[0] - pitLength, self.bbr[1] - pitLength, self.bbr[2]),
                    (self.bbr[0] - pitLength, self.bbr[1] - 2 * pitLength, self.bbr[2]),
                    (self.bbr[0] - 2 * pitLength, self.bbr[1] - 2 * pitLength, self.bbr[2]),
                    (self.bbr[0] - 2 * pitLength, self.bbr[1] - pitLength, self.bbr[2])
                ],
                #Back face BottomRight
                [
                    (self.bbr[0] - 7 * pitLength, self.bbr[1] - pitLength, self.bbr[2]),
                    (self.bbr[0] - 7 * pitLength, self.bbr[1] - 2 * pitLength, self.bbr[2]),
                    (self.bbr[0] - 8 * pitLength, self.bbr[1] - 2 * pitLength, self.bbr[2]),
                    (self.bbr[0] - 8 * pitLength, self.bbr[1] - pitLength, self.bbr[2])
                ],
                #Back face MiddleLeft
                [
                    (self.bbr[0] - pitLength, self.bbr[1] - 4 * pitLength, self.bbr[2]),
                    (self.bbr[0] - pitLength, self.bbr[1] - 5 * pitLength, self.bbr[2]),
                    (self.bbr[0] - 2 * pitLength, self.bbr[1] - 5 * pitLength, self.bbr[2]),
                    (self.bbr[0] - 2 * pitLength, self.bbr[1] - 4 * pitLength, self.bbr[2])
                ],
                #Back face MiddleRight
                [
                    (self.bbr[0] - 7 * pitLength, self.bbr[1] - 4 * pitLength, self.bbr[2]),
                    (self.bbr[0] - 7 * pitLength, self.bbr[1] - 5 * pitLength, self.bbr[2]),
                    (self.bbr[0] - 8 * pitLength, self.bbr[1] - 5 * pitLength, self.bbr[2]),
                    (self.bbr[0] - 8 * pitLength, self.bbr[1] - 4 * pitLength, self.bbr[2])
                ],
                #Back face TopLeft
                [
                    (self.bbr[0] - pitLength, self.bbr[1] - 7 * pitLength, self.bbr[2]),
                    (self.bbr[0] - pitLength, self.bbr[1] - 8 * pitLength, self.bbr[2]),
                    (self.bbr[0] - 2 * pitLength, self.bbr[1] - 8 * pitLength, self.bbr[2]),
                    (self.bbr[0] - 2 * pitLength, self.bbr[1] - 7 * pitLength, self.bbr[2])
                ],
                #Back face TopRight
                [
                    (self.bbr[0] - 7 * pitLength, self.bbr[1] - 7 * pitLength, self.bbr[2]),
                    (self.bbr[0] - 7 * pitLength, self.bbr[1] - 8 * pitLength, self.bbr[2]),
                    (self.bbr[0] - 8 * pitLength, self.bbr[1] - 8 * pitLength, self.bbr[2]),
                    (self.bbr[0] - 8 * pitLength, self.bbr[1] - 7 * pitLength, self.bbr[2])
                ]
            ]
        
        self.points = [self.ftl,self.ftr,self.fbl,self.fbr,self.btl,self.btr,self.bbl,self.bbr]
        
        self.faces = [self.one,self.two,self.three,self.four,self.five,self.six]
        
    def update(self):
        
        backMost = self.points[0]
        
        for point in self.points:
            if point[2] < backMost[2]:
                backMost = point

        self.backMost = backMost

        if backMost == self.ftl:

            pygame.draw.polygon(window,self.baseColor,[self.ftr[:2],self.btr[:2],self.bbr[:2],self.fbr[:2]]) # Right Face
            pygame.draw.polygon(window,self.baseColor,[self.btl[:2],self.btr[:2],self.bbr[:2],self.bbl[:2]]) # Back Face
            pygame.draw.polygon(window,self.baseColor,[self.fbl[:2],self.fbr[:2],self.bbr[:2],self.bbl[:2]]) # Bottom Face

            pygame.draw.line(window,self.lineColor,(self.fbr[:2]),(self.ftr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.fbr[:2]),(self.fbl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.fbr[:2]),(self.bbr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.bbl[:2]),(self.btl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.bbl[:2]),(self.bbr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.bbl[:2]),(self.fbl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.btr[:2]),(self.btl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.btr[:2]),(self.bbr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.btr[:2]),(self.ftr[:2]),2)
            
            for pit in self.faces[1] + self.faces[3] + self.faces[5]:
                step = []
                for point in pit:
                    step.append(point[:2])
                pygame.draw.polygon(window,self.lineColor,step)
                
        elif backMost == self.fbr:

            pygame.draw.polygon(window,self.baseColor,[self.ftr[:2],self.btr[:2],self.btl[:2],self.ftl[:2]]) # Top Face
            pygame.draw.polygon(window,self.baseColor,[self.btl[:2],self.btr[:2],self.bbr[:2],self.bbl[:2]]) # Back Face
            pygame.draw.polygon(window,self.baseColor,[self.fbl[:2],self.ftl[:2],self.btl[:2],self.bbl[:2]]) # Left Face

            pygame.draw.line(window,self.lineColor,(self.ftl[:2]),(self.ftr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.ftl[:2]),(self.fbl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.ftl[:2]),(self.btl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.bbl[:2]),(self.btl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.bbl[:2]),(self.bbr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.bbl[:2]),(self.fbl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.btr[:2]),(self.btl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.btr[:2]),(self.bbr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.btr[:2]),(self.ftr[:2]),2)
            
            for pit in self.faces[2] + self.faces[4] + self.faces[5]:
                step = []
                for point in pit:
                    step.append(point[:2])
                pygame.draw.polygon(window,self.lineColor,step)
                
        elif backMost == self.bbl:

            pygame.draw.polygon(window,self.baseColor,[self.ftr[:2],self.btr[:2],self.btl[:2],self.ftl[:2]]) # Top Face
            pygame.draw.polygon(window,self.baseColor,[self.ftl[:2],self.ftr[:2],self.fbr[:2],self.fbl[:2]]) # Front Face
            pygame.draw.polygon(window,self.baseColor,[self.ftr[:2],self.btr[:2],self.bbr[:2],self.fbr[:2]]) # Right Face

            pygame.draw.line(window,self.lineColor,(self.ftl[:2]),(self.ftr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.ftl[:2]),(self.fbl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.ftl[:2]),(self.btl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.fbr[:2]),(self.ftr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.fbr[:2]),(self.fbl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.fbr[:2]),(self.bbr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.btr[:2]),(self.btl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.btr[:2]),(self.bbr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.btr[:2]),(self.ftr[:2]),2)
            
            for pit in self.faces[0] + self.faces[1] + self.faces[2]:
                step = []
                for point in pit:
                    step.append(point[:2])
                pygame.draw.polygon(window,self.lineColor,step)
                
        elif backMost == self.btr:

            pygame.draw.polygon(window,self.baseColor,[self.fbl[:2],self.fbr[:2],self.bbr[:2],self.bbl[:2]]) # Bottom Face
            pygame.draw.polygon(window,self.baseColor,[self.ftl[:2],self.ftr[:2],self.fbr[:2],self.fbl[:2]]) # Front Face
            pygame.draw.polygon(window,self.baseColor,[self.fbl[:2],self.ftl[:2],self.btl[:2],self.bbl[:2]]) # Left Face

            pygame.draw.line(window,self.lineColor,(self.ftl[:2]),(self.ftr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.ftl[:2]),(self.fbl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.ftl[:2]),(self.btl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.fbr[:2]),(self.ftr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.fbr[:2]),(self.fbl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.fbr[:2]),(self.bbr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.bbl[:2]),(self.btl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.bbl[:2]),(self.bbr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.bbl[:2]),(self.fbl[:2]),2)
            
            for pit in self.faces[0] + self.faces[3] + self.faces[4]:
                step = []
                for point in pit:
                    step.append(point[:2])
                pygame.draw.polygon(window,self.lineColor,step)
                
        elif backMost == self.ftr:

            pygame.draw.polygon(window,self.baseColor,[self.fbl[:2],self.ftl[:2],self.btl[:2],self.bbl[:2]]) # Left Face
            pygame.draw.polygon(window,self.baseColor,[self.fbl[:2],self.fbr[:2],self.bbr[:2],self.bbl[:2]]) # Bottom Face
            pygame.draw.polygon(window,self.baseColor,[self.btl[:2],self.btr[:2],self.bbr[:2],self.bbl[:2]]) # Back Face

            pygame.draw.line(window,self.lineColor,(self.ftl[:2]),(self.fbl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.ftl[:2]),(self.btl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.fbr[:2]),(self.fbl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.fbr[:2]),(self.bbr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.bbl[:2]),(self.btl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.bbl[:2]),(self.bbr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.bbl[:2]),(self.fbl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.btr[:2]),(self.btl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.btr[:2]),(self.bbr[:2]),2)
            
            for pit in self.faces[3] + self.faces[4] + self.faces[5]:
                step = []
                for point in pit:
                    step.append(point[:2])
                pygame.draw.polygon(window,self.lineColor,step)
                
        elif backMost == self.fbl:

            pygame.draw.polygon(window,self.baseColor,[self.btl[:2],self.btr[:2],self.bbr[:2],self.bbl[:2]]) # Back Face
            pygame.draw.polygon(window,self.baseColor,[self.ftr[:2],self.btr[:2],self.bbr[:2],self.fbr[:2]]) # Right Face
            pygame.draw.polygon(window,self.baseColor,[self.ftr[:2],self.btr[:2],self.btl[:2],self.ftl[:2]]) # Top Face

            pygame.draw.line(window,self.lineColor,(self.ftl[:2]),(self.ftr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.ftl[:2]),(self.btl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.fbr[:2]),(self.ftr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.fbr[:2]),(self.bbr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.bbl[:2]),(self.btl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.bbl[:2]),(self.bbr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.btr[:2]),(self.btl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.btr[:2]),(self.bbr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.btr[:2]),(self.ftr[:2]),2)
            
            for pit in self.faces[1] + self.faces[2] + self.faces[5]:
                step = []
                for point in pit:
                    step.append(point[:2])
                pygame.draw.polygon(window,self.lineColor,step)
                
        elif backMost == self.bbr:

            pygame.draw.polygon(window,self.baseColor,[self.ftr[:2],self.btr[:2],self.btl[:2],self.ftl[:2]]) # Top Face
            pygame.draw.polygon(window,self.baseColor,[self.fbl[:2],self.ftl[:2],self.btl[:2],self.bbl[:2]]) # Left Face
            pygame.draw.polygon(window,self.baseColor,[self.ftl[:2],self.ftr[:2],self.fbr[:2],self.fbl[:2]]) # Front Face

            pygame.draw.line(window,self.lineColor,(self.ftl[:2]),(self.ftr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.ftl[:2]),(self.fbl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.ftl[:2]),(self.btl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.fbr[:2]),(self.ftr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.fbr[:2]),(self.fbl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.bbl[:2]),(self.btl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.bbl[:2]),(self.fbl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.btr[:2]),(self.btl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.btr[:2]),(self.ftr[:2]),2)
            
            for pit in self.faces[0] + self.faces[2] + self.faces[4]:
                step = []
                for point in pit:
                    step.append(point[:2])
                pygame.draw.polygon(window,self.lineColor,step)
                
        #elif backMost == self.btl:    
        else:

            pygame.draw.polygon(window,self.baseColor,[self.ftl[:2],self.ftr[:2],self.fbr[:2],self.fbl[:2]]) # Front Face
            pygame.draw.polygon(window,self.baseColor,[self.ftr[:2],self.btr[:2],self.bbr[:2],self.fbr[:2]]) # Right Face
            pygame.draw.polygon(window,self.baseColor,[self.fbl[:2],self.fbr[:2],self.bbr[:2],self.bbl[:2]]) # Bottom Face

            pygame.draw.line(window,self.lineColor,(self.ftl[:2]),(self.ftr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.ftl[:2]),(self.fbl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.fbr[:2]),(self.ftr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.fbr[:2]),(self.fbl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.fbr[:2]),(self.bbr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.bbl[:2]),(self.bbr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.bbl[:2]),(self.fbl[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.btr[:2]),(self.bbr[:2]),2)
            pygame.draw.line(window,self.lineColor,(self.btr[:2]),(self.ftr[:2]),2)
            
            for pit in self.faces[0] + self.faces[1] + self.faces[3]:
                step = []
                for point in pit:
                    step.append(point[:2])
                pygame.draw.polygon(window,self.lineColor,step)

    def rotate(self,rotation):

        self.rotation = (self.rotation[0] + rotation[0], self.rotation[1] + rotation[1], self.rotation[2] + rotation[2])

        #360° = 0°
        step = []
        for value in self.rotation:
            if value >= 360:
                value -= 360
            step.append(value)
        self.rotation = step

        #Converting degrees into radians
        rotateValX = rotation[0]/360 * 2 * math.pi
        rotateValY = rotation[1]/360 * 2 * math.pi
        rotateValZ = rotation[2]/360 * 2 * math.pi

        step = []
        
        for point in self.points:
            #Rotations use equation (x,y) = (xcosθ - ysinθ, xsinθ + ycosθ)
            
            # Point relative to origin
            point = (point[0] - self.centre[0],point[1] - self.centre[1],point[2] - self.centre[2])
            
            # Rotate about z axis
            point = (point[0] * math.cos(rotateValZ) - point[1] * math.sin(rotateValZ),
                     point[0] * math.sin(rotateValZ) + point[1] * math.cos(rotateValZ),point[2])

            # Rotate about y axis
            point = (point[0] * math.cos(rotateValY) - point[2] * math.sin(rotateValY),
                     point[1], point[0] * math.sin(rotateValY) + point[2] * math.cos(rotateValY))

            # Rotate about x axis
            point = (point[0],point[1] * math.cos(rotateValX) - point[2] * math.sin(rotateValX),
                     point[1] * math.sin(rotateValX) + point[2] * math.cos(rotateValX))
            
            # Point relative to centre
            point = (point[0] + self.centre[0] ,point[1] + self.centre[1], point[2] + self.centre[2])

            step.append(point)

        self.ftl,self.ftr,self.fbl,self.fbr,self.btl,self.btr,self.bbl,self.bbr  = step[0], step[1], step[2], step[3], step[4], step[5], step[6], step[7]
        
        self.points = step

        faceStep = []
        for face in self.faces:
            pitStep = []
            for pit in face:
                pointStep = []
                
                for point in pit:

                    # Point relative to origin
                    point = (point[0] - self.centre[0],point[1] - self.centre[1],point[2] - self.centre[2])
                    
                    # Rotate about z axis
                    point = (point[0] * math.cos(rotateValZ) - point[1] * math.sin(rotateValZ),
                             point[0] * math.sin(rotateValZ) + point[1] * math.cos(rotateValZ),point[2])

                    # Rotate about y axis
                    point = (point[0] * math.cos(rotateValY) - point[2] * math.sin(rotateValY),
                             point[1], point[0] * math.sin(rotateValY) + point[2] * math.cos(rotateValY))

                    # Rotate about x axis
                    point = (point[0],point[1] * math.cos(rotateValX) - point[2] * math.sin(rotateValX),
                             point[1] * math.sin(rotateValX) + point[2] * math.cos(rotateValX))
                    
                    # Point relative to centre
                    point = (point[0] + self.centre[0] ,point[1] + self.centre[1], point[2] + self.centre[2])

                    pointStep.append(point)
                    
                pitStep.append(pointStep)

            faceStep.append(pitStep)
        
        self.faces = faceStep

    def translate(self,vector):
        
        self.centre = (self.centre[0] + vector[0],self.centre[1] + vector[1],self.centre[2] + vector[2])

        self.ftl = (self.ftl[0] + vector[0],self.ftl[1] + vector[1],self.ftl[2] + vector[2])
        self.ftr = (self.ftr[0] + vector[0],self.ftr[1] + vector[1],self.ftr[2] + vector[2])
        self.fbl = (self.fbl[0] + vector[0],self.fbl[1] + vector[1],self.fbl[2] + vector[2])
        self.fbr = (self.fbr[0] + vector[0],self.fbr[1] + vector[1],self.fbr[2] + vector[2])
        self.btl = (self.btl[0] + vector[0],self.btl[1] + vector[1],self.btl[2] + vector[2])
        self.btr = (self.btr[0] + vector[0],self.btr[1] + vector[1],self.btr[2] + vector[2])
        self.bbl = (self.bbl[0] + vector[0],self.bbl[1] + vector[1],self.bbl[2] + vector[2])
        self.bbr = (self.bbr[0] + vector[0],self.bbr[1] + vector[1],self.bbr[2] + vector[2])

        self.points = (self.ftl,self.ftr,self.fbl,self.fbr,self.btl,self.btr,self.bbl,self.bbr)
        
        faceStep = []
        for face in self.faces:
            pitStep = []
            for pit in face:
                pointStep = []
                
                for point in pit:

                    point = (point[0] + vector[0],point[1] + vector[1],point[2] + vector[2])

                    pointStep.append(point)
                    
                pitStep.append(pointStep)

            faceStep.append(pitStep)
        
        self.faces = faceStep
        
    def erase(self):
        originalLineColor = self.lineColor
        originalBaseColor = self.baseColor
        
        self.lineColor = white
        self.baseColor = white
        
        self.update()
        
        self.lineColor = originalLineColor
        self.baseColor = originalBaseColor

    #Returns topmost face - visible or not
    def topValue(self):
        anchorPoints = [self.ftl,self.fbr,self.btr,self.bbl]

        topPoints = []
        
        topMost = (500,500,500)
        for anchor in anchorPoints:
            if anchor[1] < topMost[1]:
                topMost = anchor

        topPoints.append(topMost)
        anchorPoints.remove(topMost)
        
        topMost = (500,500,500)
        for anchor in anchorPoints:
            if anchor[1] < topMost[1]:
                topMost = anchor

        topPoints.append(topMost)


        if (self.ftl in topPoints) & (self.fbr in topPoints):
            return 1
        elif (self.btr in topPoints) & (self.fbr in topPoints):
            return 2
        elif (self.ftl in topPoints) & (self.btr in topPoints):
            return 3
        elif (self.bbl in topPoints) & (self.fbr in topPoints):
            return 4
        elif (self.ftl in topPoints) & (self.bbl in topPoints):
            return 5
        #elif (self.btr in topPoints) & (self.bbl in topPoints):
        else:
            return 6

    #Returns most leftward face that can be seen
    def leftVisibleValue(self):
        anchorPoints = [self.ftl,self.fbr,self.btr,self.bbl]

        leftPoints = []
        
        leftMost = (500,500,0)
        for anchor in anchorPoints:
            if anchor[0] < leftMost[0]:
                leftMost = anchor

        leftPoints.append(leftMost)
        anchorPoints.remove(leftMost)
        
        leftMost = (500,500,0)
        for anchor in anchorPoints:
            if (anchor[0] < leftMost[0]) & (anchor[2] > leftMost[2]):
                leftMost = anchor

        leftPoints.append(leftMost)

        if (self.ftl in leftPoints) & (self.fbr in leftPoints):
            return 1
        elif (self.btr in leftPoints) & (self.fbr in leftPoints):
            return 2
        elif (self.ftl in leftPoints) & (self.btr in leftPoints):
            return 3
        elif (self.bbl in leftPoints) & (self.fbr in leftPoints):
            return 4
        elif (self.ftl in leftPoints) & (self.bbl in leftPoints):
            return 5
        #elif (self.btr in topPoints) & (self.bbl in topPoints):
        else:
            return 6

    #Algins cube in a meaningful way to see top, left and right face at angles that are multiples of 45°
    def reposition(self):
        top = self.topValue()
        left = self.leftVisibleValue()
        
        rotation = [0,0,0]
        
        if top == 1:
            rotation[0] = 45
            rotation[1] = 0
            
            if left == 2:
                rotation[2] = 135
            elif left == 3:
                rotation[2] = 225
            elif left == 4:
                rotation[2] = 45
            #elif left == 5:
            else:
                rotation[2] = 315
                
        elif top == 2:
            rotation[0] = 135
            rotation[2] = 90

            if left == 1:
                rotation[1] = 135
            elif left == 3:
                rotation[1] = 225
            elif left == 4:
                rotation[1] = 45
            #elif left == 6:
            else:
                rotation[1] = 315
            
        elif top == 3:
            rotation[0] = 315
            rotation[2] = 0

            if left == 1:
                rotation[1] = 45
            elif left == 2:
                rotation[1] = 135
            elif left == 5:
                rotation[1] = 315
            #elif left == 6:
            else:
                rotation[1] = 225
            
        elif top == 4:
            rotation[0] = 135

            if left == 1:
                rotation[1] = 135
            elif left == 2:
                rotation[1] = 225
            elif left == 5:
                rotation[1] = 45
            #elif left == 6:
            else:
                rotation[1] = 315
                
        elif top == 5:
            rotation[0] = 315
            rotation[2] = 90
            
            if left == 1:
                rotation[1] = 45
            elif left == 3:
                rotation[1] = 135
            elif left == 4:
                rotation[1] = 315
            #elif left == 6:
            else:
                rotation[1] = 225
                
        else:
            rotation[0] = 225
            rotation[1] = 0

            if left == 2:
                rotation[2] = 225
            elif left == 3:
                rotation[2] = 315
            elif left == 4:
                rotation[2] = 135
            #elif left == 5:
            else:
                rotation[2] = 45

        self.__init__(self.centre,self.length,rotation,self.lineColor,self.baseColor)

#Return 2 dice rolls and their sum
def RollDie(single = False):
    Transition()
    window.fill(white)
    Draw("100x100",blue,(0,0),5,"box",0)

    #Randomising and calculating dice start positions
    
    rotation1 = (random.randint(0,360),random.randint(0,360),random.randint(0,360))
    rotation2 = (random.randint(0,360),random.randint(0,360),random.randint(0,360))
    
    die1 = Die((100,0,0),100,rotation1,red,blue)

    if single:
        #Still runs, but cannot be seen
        die2 = Die((1000,0,0),100,rotation2,red,green)
    else:
        die2 = Die((400,0,0),100,rotation2,red,green)

    rotate1 = (random.randint(4,8)/8, random.randint(4,8)/8, random.randint(4,8)/8)
    rotate2 = (random.randint(4,8)/8, random.randint(4,8)/8, random.randint(4,8)/8)
    
    die1limitY = random.randint(200,400)
    die1limitX = random.randint(300,450)
    die2limitY = random.randint(200,400)
    die2limitX = random.randint(300,450)

    speed1Y = die1limitY/400
    speed1X = die1limitX/600
    speed2Y = die2limitY/400
    speed2X = -die2limitX/600

    die2limitX = 500 - die2limitX

    a = True

    #Moving the dice until a point based on their limits
    while a:
        clock.tick(framerate)
        if(die1.centre[1] < die1limitY) | (die1.centre[1] < die1limitY):
            if (die1.centre[1] < die1limitY):

                die1.erase()
                
                die1.rotate(rotate1)
                die1.translate((speed1X,speed1Y,0))

                #Slows down rotation continuously
                step = []
                for value in rotate1:
                    if value > 0:
                        value -= 0.001
                    else:
                        value += 0.001
                    step.append(value)
                rotate1 = step

                difference1 = die1limitY - die1.centre[1]

                #Slows down speed when close to end
                if difference1 < 100:
                    speed1Y -= speed1Y/200
                    speed1X -= speed1X/200

                    #Makes die appearance meaningful
                    if difference1 < 1:
                        die1.reposition()

                #In case the die gets stuck
                if speed1Y < 0.001:
                    speed1Y = 1
                    
                die1.update()
  
            if (die2.centre[1] < die2limitY):
                
                die2.erase()
                
                die2.rotate(rotate2)
                die2.translate((speed2X,speed2Y,0))

                #Slows down rotation continuously
                step = []
                for value in rotate2:
                    if value > 0:
                        value -= 0.001
                    else:
                        value += 0.001
                    step.append(value)
                rotate2 = step

                difference2 = die2limitY - die2.centre[1]

                #Slows down speed when close to end
                if difference2 < 100:
                    speed2Y -= speed2Y/200
                    speed2X -= speed2X/200

                    #Makes die appearance meaningful
                    if (difference2 < 1) & (not single):
                        die2.reposition()

                #In case the die gets stuck
                if speed2Y < 0.001:
                    speed2Y = 1

                die2.update()
            
        else:
            #Both dice reach their end points
            break
            
        for event in pygame.event.get():
            #When QUIT pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()

    #In case not done so previously
    die1.reposition()

    if not single:
        die2.reposition()

    pygame.display.update()
    
    Draw("Press SPACE to continue",black,(25,450),3,"text",2,True)
    
    WaitForInputKey(pygame.K_SPACE)

    if single:
        Transition()
        return die1.topValue()
    else:
        Transition()
        return die1.topValue(), die2.topValue(), die1.topValue() + die2.topValue()

#Nice transition using dice
def Transition():
    #Instantiating dice
    diceA = Die((-500,200,0),100,(random.randint(0,360),random.randint(0,360),random.randint(0,360)),red,blue)
    diceB = Die((-375,150,0),100,(random.randint(0,360),random.randint(0,360),random.randint(0,360)),red,green)
    diceC = Die((-250,100,0),100,(random.randint(0,360),random.randint(0,360),random.randint(0,360)),red,blue)
    diceD = Die((-125,50,0),100,(random.randint(0,360),random.randint(0,360),random.randint(0,360)),red,green)
    diceE = Die((0,0,0),100,(random.randint(0,360),random.randint(0,360),random.randint(0,360)),red,blue)
    diceF = Die((125,-50,0),100,(random.randint(0,360),random.randint(0,360),random.randint(0,360)),red,green)
    diceG = Die((250,-100,0),100,(random.randint(0,360),random.randint(0,360),random.randint(0,360)),red,blue)
    diceH = Die((375,-150,0),100,(random.randint(0,360),random.randint(0,360),random.randint(0,360)),red,blue)
    diceI = Die((500,-200,0),100,(random.randint(0,360),random.randint(0,360),random.randint(0,360)),red,blue)

    #Moves and rotates the dice
    while diceA.centre[0] < 550:
        clock.tick(framerate)
        
        diceA.erase()
        diceA.translate((1,1,0))
        diceA.rotate((-1,-1,0))
        diceA.update()

        diceB.erase()
        diceB.translate((1,1,0))
        diceB.rotate((-1,-1,0))
        diceB.update()

        diceC.erase()
        diceC.translate((1,1,0))
        diceC.rotate((-1,-1,0))
        diceC.update()

        diceD.erase()
        diceD.translate((1,1,0))
        diceD.rotate((-1,-1,0))
        diceD.update()

        diceE.erase()
        diceE.translate((1,1,0))
        diceE.rotate((-1,-1,0))
        diceE.update()

        diceF.erase()
        diceF.translate((1,1,0))
        diceF.rotate((-1,-1,0))
        diceF.update()

        diceG.erase()
        diceG.translate((1,1,0))
        diceG.rotate((-1,-1,0))
        diceG.update()

        diceH.erase()
        diceH.translate((1,1,0))
        diceH.rotate((-1,-1,0))
        diceH.update()

        diceI.erase()
        diceI.translate((1,1,0))
        diceI.rotate((-1,-1,0))
        diceI.update()
        
        pygame.display.update()
    
#Draws the UI
def DrawMainGameUI(gameRound):
    window.fill(white)
    Draw("100x100",gold,(0,0),5,"box",0)
    Draw("ZAP's Rolling Dice Game",gold,(10,9),2,"text",0,True)
    DrawRect(gold,(0,35),(500,2))
    Draw("Round " + str(gameRound),black,(25,42),5,"text",0,True)
    DrawRect(gold,(0,90),(500,5))
    DrawRect(gold,(245,90),(10,500))

    Draw(player1.name,blue,(25,101),5,"text",0,True,0,250)
    Draw(player2.name,green,(25,101),5,"text",0,True,250,500)

    DrawRect(gold,(0,160),(500,5))

#Main game as a procedure so that the game can be replayed endlessly
def MainGame():
    Transition()
    window.fill(white)
    Draw("100x100",gold,(0,0),5,"box",0)

    #First Time Animation
    Draw("ZAP's Rolling Dice Game",gold,(10,9),2,"text",2,True)
    DrawRect(gold,(0,35),(500,2))
    Draw("Round 1",black,(25,42),5,"text",2,True)
    DrawRect(gold,(0,90),(500,5))
    DrawRect(gold,(245,90),(10,500))

    Draw(player1.name,blue,(25,101),5,"text",2,True,0,250)
    Draw(player2.name,green,(25,101),5,"text",2,True,250,500)

    DrawRect(gold,(0,160),(500,5))

    Draw(str(player1.score),blue,(25,170),10,"text",2,True,0,250)
    Draw(str(player2.score),green,(25,170),10,"text",2,True,250,500)
        
    #Main game loop
    for gameRound in range(1,6):

        DrawMainGameUI(gameRound)
        Draw(str(player1.score),blue,(25,170),10,"text",0,True,0,250)
        Draw(str(player2.score),green,(25,170),10,"text",0,True,250,500)
        
        #Roll Player 1 die
        waitForInput = Button((125,400),50,red,0,"ROLL",3)

        player1vals = RollDie()
        
        DrawMainGameUI(gameRound)
        Draw(str(player1.score),blue,(25,170),10,"text",0,True,0,250)
        Draw(str(player2.score),green,(25,170),10,"text",0,True,250,500)

        ChangeScoreAnimation("+" + str(player1vals[2]),green,blue,5,player1.score,0,250)
        Draw(str(player1.score),white,(25,170),10,"text",0,True,0,250)
        
        #Assign dice rolls and sum to Player 1 object
        player1.die1,player1.die2 = player1vals[0],player1vals[1]
        player1.score += player1vals[2]

        #Update score
        Draw("+" + str(player1vals[2]),white,(25,210),5,"text",0,True,0,250)
        Draw(str(player1.score),blue,(25,170),10,"text",0,True,0,250)      

        pygame.display.update()
        
        #Bonuses and deductions for Player 1 object
        #Even sums give +10
        if player1vals[2] % 2 == 0:
            ChangeScoreAnimation("EVEN: +10",green,blue,3,player1.score,0,250)
            Draw(str(player1.score),white,(25,170),10,"text",0,True,0,250) 

            player1.score += 10
            Draw("EVEN: +10",white,(25,210),3,"text",0,True,0,250)
            Draw(str(player1.score),blue,(25,170),10,"text",0,True,0,250) 

            #Doubles give an extra roll
            if player1vals[0] == player1vals[1]:
                Draw("DOUBLE: BONUS ROLL!",green,(25,310),2,"text",0,True,0,250)

                waitForInput = Button((125,400),50,red,0,"ROLL",3)
                bonusRoll = RollDie(True)

                DrawMainGameUI(gameRound)
                Draw(str(player1.score),blue,(25,170),10,"text",0,True,0,250)
                Draw(str(player2.score),blue,(25,170),10,"text",0,True,250,500)
                
                ChangeScoreAnimation("BONUS: +" + str(bonusRoll),green,blue,3,player1.score,0,250)
                Draw(str(player1.score),white,(25,170),10,"text",0,True,0,250)
                
                player1.score += bonusRoll

                Draw("BONUS: +" + str(bonusRoll),white,(25,210),3,"text",0,True,0,250)
                Draw(str(player1.score),blue,(25,170),10,"text",0,True,0,250)
                
        #Odd sums give -5
        else:
            ChangeScoreAnimation("ODD: -5",red,blue,3,player1.score,0,250)
            Draw(str(player1.score),white,(25,170),10,"text",0,True,0,250)
            
            player1.score -= 5
            if player1.score < 0:
                player1.score = 0
                
            Draw("ODD: -5",white,(25,210),3,"text",0,True,0,250)
            Draw(str(player1.score),blue,(25,170),10,"text",0,True,0,250) 

            
        #Roll Player 2 dice
        waitForInput = Button((375,400),50,red,0,"ROLL",3)
        
        player2vals = RollDie()
        
        DrawMainGameUI(gameRound)
        Draw(str(player1.score),blue,(25,170),10,"text",0,True,0,250)
        Draw(str(player2.score),green,(25,170),10,"text",0,True,250,500)

        ChangeScoreAnimation("+" + str(player2vals[2]),green,green,5,player2.score,250,500)
        Draw(str(player2.score),white,(25,170),10,"text",0,True,250,500)

        #Assign dice rolls and sum to Player 2 object
        player2.die1,player2.die2 = player2vals[0],player2vals[1]
        player2.score += player2vals[2]

        #Update score
        Draw("+" + str(player2vals[2]),white,(25,210),5,"text",0,True,250,500)
        Draw(str(player2.score),green,(25,170),10,"text",0,True,250,500)      

        pygame.display.update()
        
        #Bonuses and deductions for Player 2 object
        #Even sums give +10
        if player2vals[2] % 2 == 0:
            ChangeScoreAnimation("EVEN: +10",green,green,3,player2.score,250,500)
            Draw(str(player2.score),white,(25,170),10,"text",0,True,250,500) 

            player2.score += 10
            Draw("EVEN: +10",white,(25,210),3,"text",0,True,250,500)
            Draw(str(player2.score),green,(25,170),10,"text",0,True,250,500) 

            #Doubles give an extra roll
            if player2vals[0] == player2vals[1]:
                Draw("DOUBLE: BONUS ROLL!",green,(25,310),2,"text",0,True,250,500)

                waitForInput = Button((375,400),50,red,0,"ROLL",3)
                bonusRoll = RollDie(True)

                DrawMainGameUI(gameRound)
                Draw(str(player1.score),blue,(25,170),10,"text",0,True,0,250)
                Draw(str(player2.score),green,(25,170),10,"text",0,True,250,500)
                
                ChangeScoreAnimation("BONUS: +" + str(bonusRoll),green,green,3,player2.score,250,500)
                Draw(str(player2.score),white,(25,170),10,"text",0,True,250,500)
                
                player2.score += bonusRoll

                Draw("BONUS: +" + str(bonusRoll),white,(25,210),3,"text",0,True,250,500)
                Draw(str(player2.score),green,(25,170),10,"text",0,True,250,500) 

        #Odd sums give -5 
        else:
            ChangeScoreAnimation("ODD: -5",red,green,3,player2.score,250,500)
            Draw(str(player2.score),white,(25,170),10,"text",0,True,250,500)
            
            player2.score -= 5
            if player2.score < 0:
                player2.score = 0
                
            Draw("ODD: -5",white,(25,210),3,"text",0,True,250,500)
            Draw(str(player2.score),green,(25,170),10,"text",0,True,250,500)

    #Check for winner
    tied = True
    
    while tied:
        if player1.score > player2.score:
            winner = player1
            tied = False
        elif player1.score < player2.score:
            winner = player2
            tied = False
        else:
            Draw("Round 5",white,(25,42),5,"text",0,True)
            Draw("TIE BREAKER",black,(25,42),5,"text",2,True)

            waitForInput = Button((125,340),50,red,0,"ROLL",3)
            tieDie1 = RollDie(True)

            DrawMainGameUI(gameRound)
            Draw(str(player1.score),blue,(25,170),10,"text",0,True,0,250)
            Draw(str(player2.score),green,(25,170),10,"text",0,True,250,500)
            
            Draw(str(tieDie1),blue,(25,300),7,"text",1,True,0,250)

            waitForInput = Button((375,340),50,red,0,"ROLL",3)
            tieDie2 = RollDie(True)

            DrawMainGameUI(gameRound)
            Draw(str(player1.score),blue,(25,170),10,"text",0,True,0,250)
            Draw(str(player2.score),green,(25,170),10,"text",0,True,250,500)

            Draw(str(tieDie1),blue,(25,300),7,"text",1,True,0,250)
            Draw(str(tieDie2),green,(25,300),7,"text",1,True,250,500)
            
            if tieDie1 > tieDie2:
                winner = player1
                tied = False
            elif tieDie2 > tieDie1:
                winner = player2
                tied = False
            #else tie breaker is ran again

    Draw("Press SPACE to continue",black,(25,450),3,"text",2,True)
    WaitForInputKey(pygame.K_SPACE)

    Transition()
    window.fill(white)
    Draw("100x100",gold,(0,0),5,"box",0)

    Draw("WINNER:",gold,(25,25),7,"text",2,True)
    Draw(winner.name,gold,(25,210),10,"text",2,True)

    Draw("Score: " + str(winner.score),black,(25,300),5,"text",2,True)

    Draw("Press SPACE to continue",black,(25,450),3,"text",2,True)
    WaitForInputKey(pygame.K_SPACE)

    #Reading data from text file
    file = open("ZAP.txt")
    data = file.readlines()

    #Adding winner data to text file
    newData = []

    for item in data:
        #Finding score of each item
        separation = item.find("|")
        itemScore = int(item[separation+1:])

        #Check to see if winner's data has already been added
        if winner.score != -1:
            if itemScore < winner.score:
                newData.append(winner.name + "|" + str(winner.score) + "\n")
                newData.append(item)
                #Marks score as having been added
                winner.score = -1
            else:
                newData.append(item)
        else:
            newData.append(item)

    if winner.score != -1:
        newData.append(winner.name + "|" + str(winner.score) + "\n")

    #Write new data to text file
    file.close()
    file = open("ZAP.txt","w")

    for item in newData:
        file.write(item)
    file.close()

    step = []
    for item in newData:
        separation = item.find("|")

        username = item[:separation]
        score = item[separation + 1:]

        item = username + " - " + score
        step.append(item)
    newData = step

    #Extract and OUTPUT top 5

    Transition()
    window.fill(white)
    Draw("100x100",blue,(0,0),5,"box",0)
  
    Draw("TOP 5:",blue,(25,15),7,"text",2,True)

    colors = [gold, green, blue, black, black]

    for index in range(0,5):
        color = colors[index]
        try:
            #Draws places on the leaderboard
            Draw(str(index + 1) + ". " + newData[index][:-1],color,(25,(index + 1) * 80),5,"text",2,True)
        except:
            #When there is no place on leaderboard
            Draw(str(index + 1) + ".   -",color,(25,5*75),5,"text",2,True)
        
        time.sleep(0.1)

    Draw("Press SPACE to continue",black,(25,450),3,"text",2,True)
    WaitForInputKey(pygame.K_SPACE)

    Transition()
    window.fill(white)
    Draw("100x100",gold,(0,0),5,"box",0)
    
    Draw("Thanks for playing!",gold,(25,25),5,"text",1,True)
    Draw("Do you want to play again?",black,(25,100),4,"text",1,True)

    replay = TwoButtons((250,300), (475,475), 150, green, red, "YES", "no", 15, white, white, 20, 3)

    if replay == 0:
        #Resets and restarts game
        player1.score = 0
        player2.score = 0
        MainGame()
    else:
        pygame.quit()
        quit()

# Color Sets
colorSets = [ #Black, White, Red, Green, Blue, Gold
    [(0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,220,115)],
    #Coffee, Cream, Redwood, Pistachio, Sky Blue, Lion
    [(100,69,54),(238,241,189),(178,103,94),(187,214,134),(126,196,207),(196,163,129)],
    #Night, Platinum, Burnt Sienna, Mint, Ceruleam, Gold
    [(8,15,15),(234,234,234),(221,110,66),(3,206,164),(41,120,160),(243,183,0)],
    #Russian Violet, Mint Cream, Red (CMYK), Apple Green, Light Sea Green, Hunyadi Yellow
    [(11,3,45),(247,255,247),(238,46,49),(157,177,67),(32,163,158),(246,174,45)],
    #Licorice, Lavender (Web), Orange (Pantone), SGBUS Green, Robin Egg Blue, Sunglow
    [(18,3,9),(231,230,247),(254,95,0),(4,231,98),(0,161,228),(255,200,87)],
    #Black, Lemon Chiffon, Cinnabar, Kelly Green, Turquoise, Sunglow
    [(8,7,5),(254,246,201),(229,89,52),(119,177,67),(0,224,213),(255,209,102)],
    #Black, White, Jasper, Emerald, French Blue, Tomato
    [(0,0,0),(255,255,255),(255,68,51),(51,202,127),(28,119,195),(242,143,59)],
    #Lavender (Web), White, Melon, Tea Green, Air Superiroity Blue, Jasmine
    [(219,216,233),(0,0,0),(240,181,170),(197,235,195),(114,155,172),(255,230,153)],
    #Glaucous, Raisin Black, Tomato, Lime, Robin Egg Blue, Orange (Web)
    [(113,128,172),(32,33,36),(254,94,65),(206,255,87),(49,221,224),(255,173,5)]
]

#Start Menu
Draw("100x100",blue,(0,0),5,"box",1)

DrawRect(black,(120,120),(260,85))
DrawRect(black,(120,220),(260,85))
DrawRect(black,(120,320),(260,85))

DrawRect(gold,(125,125),(250,75))
DrawRect(gold,(125,225),(250,75))
DrawRect(gold,(125,325),(250,75))

Draw("ZAP's Rolling",green,(25,25),4,"text",0,True)
Draw("Dice Game",blue,(25,75),5,"text",0,True)
Draw("START",white,(125,135),5,"text",0,True)
Draw("THEME 1",white,(125,235),5,"text",0,True)
Draw("CREDITS",white,(125,335),5,"text",0,True)
Draw("- Zayan Pannun.",red,(275,450),3,"text",0)
     
pygame.display.update()
    
menu = True

diceA = Die((75,75,0),50,(0,0,0),red,blue)
diceB = Die((425,75,0),50,(0,0,0),red,green)

#Theme counter
count = 1

while menu:
    clock.tick(framerate)
    
    mousePos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        #When QUIT pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                framerate = int(input("FPS: "))
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if 125 <= mousePos[0] <= 375:
                
                if 125 <= mousePos[1] <= 200:
                    #Start the game
                    DrawRect(blue,(125,125),(250,75))
                    Draw("START",white,(125,135),5,"text",2,True)
                    menu = False
                    
                elif 225 <= mousePos[1] <= 300:
                    #Change the color palette
                    step = colorSets[0]
                    colorSets.remove(colorSets[0])
                    colorSets.append(step)

                    count += 1
                    if count == len(colorSets) + 1:
                        count = 1
                            
                    black = colorSets[0][0]
                    white = colorSets[0][1]
                    red = colorSets[0][2]
                    green = colorSets[0][3]
                    blue = colorSets[0][4]
                    gold = colorSets[0][5]

                    #The menu screen shows the new color palette
                    window.fill(white)
                    Draw("100x100",blue,(0,0),5,"box",0)

                    DrawRect(black,(120,120),(260,85))
                    DrawRect(black,(120,220),(260,85))
                    DrawRect(black,(120,320),(260,85))

                    DrawRect(gold,(125,125),(250,75))
                    DrawRect(gold,(125,225),(250,75))
                    DrawRect(gold,(125,325),(250,75))

                    Draw("ZAP's Rolling",green,(25,25),4,"text",0,True)
                    Draw("Dice Game",blue,(25,75),5,"text",0,True)
                    Draw("START",white,(125,135),5,"text",0,True)
                    Draw("THEME " + str(count),white,(125,235),5,"text",0,True)
                    Draw("CREDITS",white,(125,335),5,"text",0,True)
                    Draw("- Zayan Pannun",red,(275,450),3,"text",0)

                    diceA.baseColor, diceA.lineColor = blue, red
                    diceB.baseColor, diceB.lineColor = green, red
                    
                elif 325 <= mousePos[1] <= 400:
                    #Jokey credits
                    DrawRect(blue,(125,325),(250,75))
                    Draw("CREDITS",white,(125,335),5,"text",2,True)
                    Draw("- Zayan Pannun",white,(275,450),3,"text",0)
                    Draw("It was all done by one person;",red,(25,410),3,"text",True,True)
                    Draw("That one person is Zayan Pannun.",red,(25,450),3,"text",True,True)
                    
                    DrawRect(gold,(125,325),(250,75))
                    Draw("CREDITS",white,(125,335),5,"text",0,True)

        #The spinning dice show which button the cursor is above 
        elif 125 <= mousePos[0] <= 375:
            if 125 <= mousePos[1] <= 200:
                #Above START
                diceA.__init__((75,160,0),diceA.length,diceA.rotation,diceA.lineColor,diceA.baseColor)
                diceB.__init__((425,160,0),diceB.length,diceB.rotation,diceB.lineColor,diceB.baseColor)
            elif 225 <= mousePos[1] <= 300:
                #Above THEME
                diceA.__init__((75,260,0),diceA.length,diceA.rotation,diceA.lineColor,diceA.baseColor)
                diceB.__init__((425,260,0),diceB.length,diceB.rotation,diceB.lineColor,diceB.baseColor)
            elif 325 <= mousePos[1] <= 400:
                #Above CREDITS
                diceA.__init__((75,360,0),diceA.length,diceA.rotation,diceA.lineColor,diceA.baseColor)
                diceB.__init__((425,360,0),diceB.length,diceB.rotation,diceB.lineColor,diceB.baseColor)
        else:
            #Return next to title
            diceA.__init__((75,75,0),diceA.length,diceA.rotation,diceA.lineColor,diceA.baseColor)
            diceB.__init__((425,75,0),diceB.length,diceB.rotation,diceB.lineColor,diceB.baseColor)
                
    #Rotate dice
    diceA.erase()
    diceB.erase()
    
    diceA.rotate((-1/2,-1/2,-1/2))
    diceB.rotate((-1/2,1/2,1/2))

    diceA.update()
    diceB.update()
    
    pygame.display.update()

#Draw format lines
Transition()
window.fill(white)
Draw("100x100",blue,(0,0),5,"box",0)

Draw("50x100",black,(0,0),5,"box")
Draw("50x100",black,(250,0),5,"box")

pygame.display.update()

#Login for Player 1
loggingIn = True

#Display

Draw("lock",red,(108,226),5,"icon")
Draw("lock",red,(358,226),5,"icon")

pygame.display.update()

#Animation of lock
value = 0

#Y axis: 226 --> 106
while value < 13:
    clock.tick(framerate)
    DrawRect(white,(108,100),(50,200))
    Draw("lock",red,(108,226-value*10),5,"icon",0)
    value += 1
    time.sleep(0.1)
    pygame.display.update()
    
doDelay = True

#Input Fields for Player 1
Draw("Username:",red,(20,175),5,"text",2)
Draw("46x15",red,(10,220),5,"box")

Draw("Password:",red,(20,300),5,"text",2)
Draw("46x15",red,(10,345),5,"box")

pygame.display.update()

#Core login for Player 1
while loggingIn:
    
    for event in pygame.event.get():
        #When QUIT pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
      
    login1 = Login((25,230),(25,355),5,200)
    
    if login1 != None:
        loggingIn = False
        doDelay = False
        DrawRect(white,(108,106),(35,50))
        Draw("unlock",green,(108,101),5,"icon",0)

#Login for Player 2

#Animation of lock
value = 0

#Y axis: 226 --> 106
while value < 13:
    clock.tick(framerate)
    DrawRect(white,(358,106),(50,200))
    Draw("lock",red,(358,226-value*10),5,"icon",0)
    value += 1
    time.sleep(0.1)
    pygame.display.update()

#Input Fields for Player 2
Draw("Username:",red,(270,175),5,"text",2)
Draw("46x15",red,(260,220),5,"box")

Draw("Password:",red,(270,300),5,"text",2)
Draw("46x15",red,(260,345),5,"box")

pygame.display.update()

#Core login for Player 2
loggingIn = True

while loggingIn:
    login2 = Login((275,230),(275,355),5,200,login1)
    
    if login2 != None:
        loggingIn = False
        doDelay = False
        DrawRect(white,(358,106),(35,50))
        Draw("unlock",green,(358,101),5,"icon",0)

#Instantiate players          
player1 = Player(accounts[login1][0])
player2 = Player(accounts[login2][0])
    
    
#Startup info & Tutorial
Transition()
window.fill(white)
Draw("100x100",blue,(0,0),5,"box")
pygame.display.update()

for event in pygame.event.get():
    #When QUIT pressed
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()

Draw("Welcome to ZAP's Rolling Dice Game!",black,(10,10),3,"text",0,True)

Draw("Would you like a tutorial?",black,(10,100),4,"text",0,True)


tutorial = TwoButtons((125,250),(375,250),50,green,red,"YES","NO",5,white)

if tutorial == 0:
    Transition()
    window.fill(white)
    Draw("100x100",blue,(0,0),5,"box",0)
    pygame.display.update()

    Draw("There are",black,(25,25),4,"text",2)
    Draw("5 rounds",blue,(25,75),10,"text",1,True)

    Draw("Each round",black,(25,200),2,"text")
    Draw("Each player rolls",black,(25,240),2,"text")
    Draw("2 dice",blue,(25,300),10,"text",1,True)

    Draw("Press SPACE to continue",black,(25,450),3,"text",2,True)

    WaitForInputKey(pygame.K_SPACE)

    Transition()
    window.fill(white)
    Draw("100x100",blue,(0,0),5,"box",0)

    Draw("The points on your dice",black,(25,25),4,"text",2,True)
    Draw("are added to your score",black,(25,75),4,"text",2,True)

    Draw("If the sum",green,(25,150),3,"text",2,True,0,250)
    Draw("added is",green,(25,190),3,"text",2,True,0,250)
    Draw("EVEN",green,(25,230),5,"text",1,True,0,250)

    Draw("Then you GAIN",green,(25,310),3,"text",2,True,0,250)
    Draw("+10 ",green,(25,350),5,"text",1,True,0,250)

    Draw("If the sum",red,(25,150),3,"text",2,True,250,500)
    Draw("added is",red,(25,190),3,"text",2,True,250,500)
    Draw("ODD",red,(25,230),5,"text",1,True,250,500)

    Draw("Then you LOSE",red,(25,310),3,"text",2,True,250,500)
    Draw("-5 ",red,(25,350),5,"text",1,True,250,500)

    Draw("Press SPACE to continue",black,(25,450),3,"text",2,True)

    WaitForInputKey(pygame.K_SPACE)

    Transition()
    window.fill(white)
    Draw("100x100",blue,(0,0),5,"box",0)

    Draw("If you roll a",black,(25,25),3,"text",2,True)
    Draw("DOUBLE",green,(25,75),5,"text",1,True)
    Draw("(When both die roll the same number)",black,(25,140),2,"text",1,True)

    Draw("Then you get a",black,(25,200),3,"text",2,True)
    Draw("BONUS ROLL",green,(25,250),5,"text",1,True)

    Draw("Press SPACE to continue",black,(25,450),3,"text",2,True)

    WaitForInputKey(pygame.K_SPACE)

    Transition()
    window.fill(white)
    Draw("100x100",blue,(0,0),5,"box",0)
    
    Draw("After 5 rounds, whoever has the",black,(25,25),3,"text",2,True)
    Draw("HIGHEST SCORE",blue,(25,75),5,"text",1,True)
    Draw("is declared the",black,(25,130),3,"text",2,True)
    Draw("WINNER!",gold,(25,180),5,"text",1,True)

    Draw("In the case of a draw",black,(25,270),3,"text",1,True)
    Draw("Both players roll an extra die each",black,(25,310),3,"text",1,True)
    Draw("- the greatest roll wins!",black,(25,360),3,"text",1,True)

    Draw("Press SPACE to continue",black,(25,450),3,"text",2,True)
    
    WaitForInputKey(pygame.K_SPACE)

MainGame()
