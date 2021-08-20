import pygame
from locals_ import *

class Board:
    '''
    板子
    pos 位置
    time2 等待时间
    time1 持续时间
    speed 移动速度
    direction 方向
    '''
    def __init__(self, pos, length, speed, time1, time2=0, direction=UP):
        self.pos = pos
        self.direction = direction
        if direction in [UP, DOWN]:
            self.size = [length, 6]
        else:
            self.size = [6, length]
        self.speed = speed

        self.rect = pygame.Rect(self.pos, self.size)
        self.stop = False
        self.showing = False

        self.time = 0
        self.time1 = time1
        self.time2 = time2

    def show(self, screen):
        if self.time >= self.time2:
            self.showing = True

        if self.showing:
            self.rect = pygame.Rect(self.pos, self.size)
            if self.direction == UP:
                green_rect = pygame.Rect((self.pos[0], self.pos[1] - 3), self.size)
            elif self.direction == DOWN:
                green_rect = pygame.Rect((self.pos[0], self.pos[1] + 3), self.size)
            elif self.direction == LEFT:
                green_rect = pygame.Rect((self.pos[0] - 3, self.pos[1]), self.size)
            elif self.direction == RIGHT:
                green_rect = pygame.Rect((self.pos[0] + 3, self.pos[1]), self.size)
            pygame.draw.rect(screen, (0  , 120, 0  ), green_rect, 1)
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 1)
            self.pos[0] += self.speed[0]
            self.pos[1] += self.speed[1]

        if self.time >= self.time1 + self.time2:
            self.stop = True

        self.time += 1
