from variables import Variables
import pygame 

class Circle:
    # circles = set()

    def __init__(self, coords, r, color):
        self.coords = coords
        self.r = r
        self.color = color
        self.growing = True
        # Circle.circles.add(self)

    def __eq__(self, other):
        return self.coords == other.coords

    def __hash__(self):
        return hash(self.coords)

    def grow(self):
        if self.growing:
            self.r += 1

    def edges(self):
        return (self.coords[0] + self.r >= Variables.width) or (self.coords[0] - self.r <= 0) or (self.coords[1] + self.r >= Variables.height) or (self.coords[1] - self.r <= 0)

    def show(self, screen):
        pygame.draw.circle(screen, self.color, self.coords, self.r, width=Variables.lw)

    def getColor(self):
        return self.color

    def getCoords(self):
        return self.coords

    def getRadius(self):
        return self.r
