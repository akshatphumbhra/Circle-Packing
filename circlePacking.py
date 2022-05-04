import pygame
import random
import math
from PIL import Image
from variables import Variables
from circle import Circle
from postscript import PostScript

pygame.init()

# Set screen dimensions
screen = pygame.display.set_mode([Variables.width, Variables.height])

pic = Image.open(Variables.image).resize((Variables.width, Variables.height))
pic = pic.convert('RGB')
im = pic.load()

circles = set()

possibleCoords = set()
Xlist = [i for i in range(Variables.width)]
Ylist = [j for j in range(Variables.height)]

for x in Xlist:
    for y in Ylist:
        possibleCoords.add((x, y))

numCircles = Variables.numCircles
screen.fill((0,0,0))
def main():
    running = True
    while running:

        # clock.tick(20)
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                convertToPostScript()
                running = False 


        if len(circles) < numCircles and running:
            addCircles()
            for circ in circles:
                if circ.growing:
                    if circ.edges():
                        circ.growing = False
                    else:
                        for other in circles:
                            if other == circ:
                                continue
                            d = dist(other.coords, circ.coords)
                            if d - 1 <= circ.r + other.r:
                                circ.growing = False
                # toUpdate.append(pygame.Rect((circ.coords[0] - circ.r, circ.coords[1] - circ.r), (2*circ.r, 2*circ.r)))
                circ.show(screen)
                circ.grow()

        # Flip the display
        pygame.display.update()
    # Done! Time to quit.
    pygame.quit()

def addCircles():
    i = 0
    r = 1
    
    attempts = 0
    while(i < Variables.resolution):
        newP = possibleCoords.pop()
        
        valid = True
        for circ in circles:
            d = dist(circ.coords, newP)
            if d < circ.r:
                attempts += 1
                valid = False
                break
        if valid:
            circles.add(Circle(newP, r, im[newP[0], newP[1]]))
            i += 1
        
        if attempts > 1000:
            break

def dist(p1, p2):
    return math.sqrt( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 )

def convertToPostScript():
    file = PostScript(Variables.output, Variables.width, Variables.height)
    file.setLine(lineJoin=1, lineCap=1)
    for circ in circles:
        color = circ.getColor()
        center = adjustCoords(circ.getCoords())
        radius = circ.getRadius()
        file.setRGB(color)
        file.makeCircle(center, radius, fill=Variables.fill)
    file.createFile()

def adjustCoords(coords):
    newCoords = (coords[0], Variables.height - coords[1])
    return newCoords

main()
# addCircles()
# simulate()
        