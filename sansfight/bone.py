import pygame
from locals_ import *
from math import cos, sin, radians

class Bone:
    '''
    骨头
    pos 位置
    length 长度
    direction 方向
    speed 速度
    time1 显示时间
    time2 延迟时间
    color 颜色（蓝色、橙色、白色）
    type_ 类型：0正常；1左边/上边显示；2右边/下边显示
    '''
    def __init__(self, pos, length, direction, time1, time2=0, speed=[0, 0, 0], color=WHITE, type_=0, spec=False):
        if direction in [UP, DOWN]:
            self.direction = 0
        else:
            self.direction = 1
        self.type_ = type_
        self.color = color
        if color == WHITE:
            self.image = pygame.image.load("res/Bone/Default/000.png")
        elif color == BLUE:
            self.image = pygame.image.load("res/Bone/Blue/000.png")
        else:
            self.image = pygame.image.load("res/Bone/Orange/000.png")
        self.bone_img1 = pygame.transform.rotate(
            pygame.transform.chop(
                self.image,
                [11, 8, 12, 24]
            ),
            self.direction * 90
        )
        self.bone_img2 = pygame.transform.rotate(
            pygame.transform.chop(
                self.image,
                [11, 0, 12, 16]
            ),
            self.direction * 90
        )
        self.length = length
        self.pos = pos
        self.speed = speed
        self.time = 0
        self.time1 = time1
        self.time2 = time2
        self.show_bone = False
        self.stop = False
        self.spec = spec

        self.rotatable = False

    def show(self, screen,
             mask_surface_blue,
             mask_surface_orange,
             mask_surface_normal):
        self.time += 1
        if not self.direction:
            self.rect = pygame.Rect(self.pos[0] + 3, self.pos[1] + 8, 6, self.length)
        else:
            self.rect = pygame.Rect(self.pos[0] + 8, self.pos[1] + 3, self.length, 6)
        if not self.show_bone and self.time >= self.time2:
            self.show_bone = True
            self.time = 0
        if self.show_bone and self.time >= self.time1:
            self.stop = True
        if self.show_bone:
            if self.type_ in (0, 1):
                screen.blit(self.bone_img1, self.pos)
            if not self.direction:
                if self.type_ in (0, 2):
                    screen.blit(self.bone_img2, (self.pos[0], self.pos[1] + self.length + 8))
            else:
                if self.type_ in (0, 2):
                    screen.blit(self.bone_img2, (self.pos[0] + self.length + 8, self.pos[1]))
                    
            if self.color == WHITE:
                pygame.draw.rect(screen, (255, 255, 255), self.rect)
                pygame.draw.rect(mask_surface_normal, (255, 255, 255, 255), self.rect)
            elif self.color == BLUE:
                pygame.draw.rect(screen, (0, 170, 255), self.rect)
                pygame.draw.rect(mask_surface_blue, (255, 255, 255, 255), self.rect)
            else:
                pygame.draw.rect(screen, (255, 150, 0), self.rect)
                pygame.draw.rect(mask_surface_orange, (255, 255, 255, 255), self.rect)
                
            self.pos = (self.pos[0] + self.speed[0], self.pos[1] + self.speed[1])
            if len(self.speed) == 3:
                self.length += self.speed[2]
            if self.spec:print(self.time)

class RotatableBone:
    '''
    可以旋转的骨头
    pos 位置
    length 长度
    angle 角度
    speed 速度 [x, y, 长度, 角度]
    time1 显示时间
    time2 延迟时间
    color 颜色（蓝色、橙色、白色）
    '''
    def __init__(self, pos, length, angle, time1, time2=0, speed=[0, 0, 0, 0], color=WHITE, spec=False):
        self.angle = angle
        self.color = color
        self.image = pygame.image.load("res/Bone/Default/000.png")
        self.bone_img1 = pygame.transform.rotate(
            pygame.transform.chop(
                self.image,
                [11, 8, 12, 24]
            ),
            360 - self.angle - 90
        )
        self.bone_img2 = pygame.transform.rotate(
            pygame.transform.chop(
                self.image,
                [11, 0, 12, 16]
            ),
            360 - self.angle - 90
        )
        self.length = length
        self.pos = pos
        self.speed = speed
        self.time = 0
        self.time1 = time1
        self.time2 = time2
        self.show_bone = False
        self.stop = False
        self.spec = spec
        
        self.rotatable = True

    def show(self, screen,
             mask_surface_blue,
             mask_surface_orange,
             mask_surface_normal):
        if not self.show_bone and self.time >= self.time2:
            self.show_bone = True
            self.time = 0
        if self.show_bone and self.time >= self.time1:
            self.stop = True
        if self.show_bone and not self.stop:
            self.pos[0] += self.speed[0]
            self.pos[1] += self.speed[1]
            if len(self.speed) >= 3:
                self.length += self.speed[2]
                if len(self.speed) >= 4:
                    self.angle += self.speed[3]
            self.bone_img1 = pygame.transform.rotate(
                pygame.transform.chop(
                    self.image,
                    [11, 8, 12, 24]
                ),
                360 - self.angle - 90
            )
            self.bone_img2 = pygame.transform.rotate(
                pygame.transform.chop(
                    self.image,
                    [11, 0, 12, 16]
                ),
                360 - self.angle - 90
            )
            rect1 = self.bone_img1.get_rect()
            rect2 = self.bone_img2.get_rect()

            rect1.center = [
                self.pos[0] + cos(radians(self.angle)) * self.length / 2,
                self.pos[1] + sin(radians(self.angle)) * self.length / 2
            ]
            rect2.center = [
                self.pos[0] - cos(radians(self.angle)) * self.length / 2,
                self.pos[1] - sin(radians(self.angle)) * self.length / 2
            ]
            screen.blit(self.bone_img1, rect1)
            screen.blit(self.bone_img2, rect2)
            if self.color == WHITE:
                pygame.draw.line(screen, (255, 255, 255, 255), rect1.center, rect2.center, 6)
                pygame.draw.line(mask_surface_normal, (255, 255, 255, 255), rect1.center, rect2.center, 6)
            elif self.color == BLUE:
                pygame.draw.line(screen, (0, 170, 255), rect1.center, rect2.center, 6)
                pygame.draw.line(mask_surface_blue, (255, 255, 255, 255), rect1.center, rect2.center, 6)
            else:
                pygame.draw.line(screen, (255, 150, 0), rect1.center, rect2.center, 6)
                pygame.draw.line(mask_surface_orange, (255, 255, 255, 255), rect1.center, rect2.center, 6)
            
        self.time += 1
