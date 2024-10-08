import math
import pygame

class buildEnvironment:
    ## COLORS

    BLACK = (0, 0, 0)
    GRAY = (70, 70, 70)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    def __init__(self, MapDimensions):
        pygame.init()
        self.pointCloud = []
        self.externalMap = pygame.image.load('maps/street.png')
        self.maph, self.mapw = MapDimensions
        self.MapWindowName = 'RRT path planning'
        pygame.display.set_caption(self.MapWindowName)
        self.map = pygame.display.set_mode((self.mapw, self.maph))
        self.map.blit(self.externalMap, (0, 0))

    def AD2pos(self, distance, angle, robotPosition):
        x = robotPosition[0] + distance * math.cos(angle)
        y = robotPosition[1] - distance * math.sin(angle)
        return [int(x), int(y)]
    
    def dataStorage(self, data):
        print(len(self.pointCloud))
        if data != False:
            for element in data:
                point = self.AD2pos(element[0], element[1], element[2])
                if point not in self.pointCloud:
                    self.pointCloud.append(point)
        
    def render(self):
        self.infomap = self.map.copy()
        for point in self.pointCloud:
            self.infomap.set_at((int(point[0]), int(point[1])), self.WHITE)
