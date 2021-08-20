import pygame

class Task:
    '''定时执行self.func'''
    def __init__(self, func, time):
        self.func = func
        self.time = 0
        self.runtime = time
        self.stop = False

    def show(self, screen):
        if self.time >= self.runtime:
            self.func(screen)
            self.stop = True
        self.time += 1

class Strike(Task):
    '''The thing that can make ME happy.=)'''
    def __init__(self, pos):
        self.time = 0
        self.runtime = 25
        self.stop = False
        self.ani = [
            pygame.image.load("res/Strike/Default/00{}.png".format(n)) \
            for n in range(5 + 1)
        ]
        self.sound = pygame.mixer.Sound("res/PlayerFight.ogg")
        self.pos = pos
    def show(self, screen):
        if self.time == 0:
            self.sound.play()
        self.time += 1
        screen.blit(self.ani[self.time // 5], self.pos)
        if self.time >= self.runtime:
            self.stop = True

class Warn:
    '''警示框'''
    def __init__(self, pos, size, time1, time2=0):
        self.pos = pos
        self.size = size
        self.time = 0
        self.time1 = time1
        self.runtime = time2
        self.stop = False
    def show(self, screen):
        if self.time >= self.runtime:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.pos, self.size), 1)
        if self.time >= self.runtime + self.time1:
            self.stop = True
        self.time += 1
            
