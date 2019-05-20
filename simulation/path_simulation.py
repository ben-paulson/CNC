import pygame
import random
import time
import math

class Game:
    def __init__(self):
        # Initialize game window, etc.
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('GCODE SIMULATION')
        self.clock = pygame.time.Clock()
        self.running = True
        self.prev_line = None
        self.speed = 50

    def new(self):
        # Start a new game
        self.all_sprites = pygame.sprite.Group()
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(30)
            self.events()
            self.update()
            #self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def intro(self):
        self.read_gcode()

    def events(self):
        # Game Loop - Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop - Draw
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def read_gcode(self):
        with open('output_0002.ngc', 'r') as f_gcode:
            data = f_gcode.read()
            lines = data.split("\n")
            dist = 0
            for line in lines:
                try:
                    x = float(line.split('X')[1].split(' ')[0])
                    y = float(line.split('Y')[1].split(' ')[0])
                    #print self.prev_line
                    
                    if self.prev_line != None:
                        dist = abs(math.sqrt((y - self.prev_line[1])**2 + (x - self.prev_line[0])**2))
                        #print dist
                    

                    #print dist
                    
                    t = dist / self.speed
                    #print t
                    
                    #print str(x_val) + ', ' + str(y_val)
                    pygame.draw.line(self.screen, (255, 255, 255), (x, y), (x, y))
                    pygame.display.flip()
                    time.sleep(t)
                    self.prev_line = [x, y]
                except Exception as e:
                    pass

g = Game()
g.intro()
while g.running:
    g.new()

pygame.quit()
quit()


