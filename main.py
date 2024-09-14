import env
import sensors
import pygame

from streetGenerator import VEHICLES, StreetGenerator

# Example usage
streetWidth = 600
streetHeight = 800

street_generator = StreetGenerator(streetWidth, streetHeight, 0.5, VEHICLES)
street_generator.createStreet()

environment = env.buildEnvironment((800, 600))
environment.originalMap = environment.map.copy()
laser = sensors.LaserSensor(500, environment.originalMap, uncertainity=(0.5,0.01))
environment.map.fill((0,0,0))
environment.infomap = environment.map.copy()

running = True

while running:
    sensorON = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            sensorON = True
        elif not pygame.mouse.get_focused():
            sensorON = False
    
    if sensorON:
        position = pygame.mouse.get_pos()
        laser.position = position
        sensor_data = laser.sense()
        environment.dataStorage(sensor_data)
        environment.render()
    environment.map.blit(environment.infomap, (0, 0))
    pygame.display.update()
pygame.quit()

    


