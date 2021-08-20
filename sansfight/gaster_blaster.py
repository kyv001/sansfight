import pygame
import math
from locals_ import *

cos = math.cos
sin = math.sin
radians = math.radians

ani_0 = pygame.image.load("res/GasterBlaster/Default/000.png")
ani_1 = pygame.image.load("res/GasterBlaster/Fire/000.png")
ani_2 = pygame.image.load("res/GasterBlaster/Fire/001.png")
ani_3 = pygame.image.load("res/GasterBlaster/Fire/002.png")
ani_4 = pygame.image.load("res/GasterBlaster/Fire/003.png")
ani_5 = pygame.image.load("res/GasterBlaster/Fire/004.png")

class GasterBlaster:
    '''
    GB炮
    pos 位置
    angle 角度
    time1 开炮等待时间
    time2 激光持续时间
    time3 延迟时间
    width 宽度
    color 颜色(橙色、蓝色、白色)
    norecoil 无后坐力
    '''
    def __init__(self, pos, angle, time1, time2, time3=0, width=44, color=WHITE, norecoil=False):
        self.stop = False
        self.show_light = False

        self.blast_sound = pygame.mixer.Sound("res/GasterBlast.ogg")
        self.load_sound = pygame.mixer.Sound("res/GasterBlaster.ogg")
        
        self.animation = [ani_0, ani_1, ani_2, ani_3, ani_4, ani_5]
        self.time1 = int(time1 + 20)
        self.time2 = int(time2 / 2)
        self.time3 = int(time3)
        self.t_start = 0
        self.ani_index = 0
        self.end_angle = angle if angle >= 0 else 360 + angle
        self.radian = self.end_angle * math.pi / 180
        self.pos = [0, 0]
        self.pos[0] = pos[0] - 100 * math.cos(self.radian)
        self.pos[1] = pos[1] - 100 * math.sin(self.radian)
        self.end_pos = pos
        self.back_speed = 0
        self.sleeping = True
        self.angle = 0
        self.width = 0
        self.end_width = width
        self.color = color
        self.alpha = 0
        self.target_alpha = 255
        self.norecoil = norecoil
        if self.color == WHITE:
            self.line_color = [255, 255, 255]
        elif self.color == BLUE:
            self.line_color = [0, 170, 255]
        else:
            self.line_color = [255, 150, 0]

    def show(self, screen,
             mask_surface_blue,
             mask_surface_orange,
             mask_surface_normal):
        self.t_start += 1
        if self.t_start <= self.time3:
            return 0
        self.sleeping = False
        if self.time1 * 2 + 8 >= self.ani_index >= self.time1 * 2:
            img = pygame.transform.rotate(
                pygame.transform.scale(self.animation[(1 + (self.ani_index - (self.time3 + self.time1) * 2)) % 12 // 4],
                    (80, self.end_width)),
                self.angle
            )
        elif self.ani_index >= self.time1 * 2 + 8:
            img = pygame.transform.rotate(
                pygame.transform.scale(self.animation[4 + (self.ani_index - (self.time3 + self.time1) * 2) % 8 // 4],
                    (80, self.end_width)),
                self.angle
            )
        else:
            img = pygame.transform.rotate(
                pygame.transform.scale(self.animation[0],
                    (80, self.end_width)),
                self.angle
            )
        if not self.stop:
            self.rect = img.get_rect()
            self.rect.center = self.pos

            if self.ani_index == self.time1 * 2 + 3:
                self.blast_sound.play()
                self.show_light = True

            if self.show_light and self.width > 4:
                # 按sin律动的激光
                offset = sin(self.ani_index / 8) * round(self.width / 5)
                # 用多边形代替pygame的👇👆画线
                l = 80
                w = round(self.width / 44 * 34) + abs(offset)
                x = self.pos[0]
                y = self.pos[1]

                point0 = [
                    x + (1 / 3) * l * cos(self.radian),
                    y + (1 / 3) * l * sin(self.radian)] # 基准点
                point1 = [
                    point0[0] + (1 / 6) * w * cos(radians(360 - self.angle - 90)),
                    point0[1] + (1 / 6) * w * sin(radians(360 - self.angle - 90))]
                point2 = [
                    point1[0] + (1 / 6) * l * cos(self.radian),
                    point1[1] + (1 / 6) * l * sin(self.radian)]
                point3 = [
                    point2[0] + (1 / 6) * w * cos(radians(360 - self.angle - 90)),
                    point2[1] + (1 / 6) * w * sin(radians(360 - self.angle - 90))]
                point4 = [
                    point3[0] + (1 / 6) * l * cos(self.radian),
                    point3[1] + (1 / 6) * l * sin(self.radian)]
                point5 = [
                    point4[0] + (1 / 6) * w * cos(radians(360 - self.angle - 90)),
                    point4[1] + (1 / 6) * w * sin(radians(360 - self.angle - 90))]
                point6 = [
                    point5[0] + 825 * cos(self.radian),
                    point5[1] + 825 * sin(self.radian)]

                point7 = [
                    point0[0] + (1 / 6) * w * cos(radians(360 - self.angle + 90)),
                    point0[1] + (1 / 6) * w * sin(radians(360 - self.angle + 90))]
                point8 = [
                    point7[0] + (1 / 6) * l * cos(self.radian),
                    point7[1] + (1 / 6) * l * sin(self.radian)]
                point9 = [
                    point8[0] + (1 / 6) * w * cos(radians(360 - self.angle + 90)),
                    point8[1] + (1 / 6) * w * sin(radians(360 - self.angle + 90))]
                point10 = [
                    point9[0] + (1 / 6) * l * cos(self.radian),
                    point9[1] + (1 / 6) * l * sin(self.radian)]
                point11 = [
                    point10[0] + (1 / 6) * w * cos(radians(360 - self.angle + 90)),
                    point10[1] + (1 / 6) * w * sin(radians(360 - self.angle + 90))]
                point12 = [
                    point11[0] + 825 * cos(self.radian),
                    point11[1] + 825 * sin(self.radian)]

                pygame.draw.polygon(screen, self.line_color + [self.alpha],
                    [
                        point1,
                        point2,
                        point3,
                        point4,
                        point5,
                        point6,
                        point12,
                        point11,
                        point10,
                        point9,
                        point8,
                        point7
                    ])

                if self.alpha >= 200:
                    if self.color == BLUE:
                        pygame.draw.polygon(mask_surface_blue, (255, 255, 255),
                            [
                                point1,
                                point2,
                                point3,
                                point4,
                                point5,
                                point6,
                                point12,
                                point11,
                                point10,
                                point9,
                                point8,
                                point7
                            ])
                    elif self.color == ORANGE:
                        pygame.draw.polygon(mask_surface_orange, (255, 255, 255),
                            [
                                point1,
                                point2,
                                point3,
                                point4,
                                point5,
                                point6,
                                point12,
                                point11,
                                point10,
                                point9,
                                point8,
                                point7
                            ])
                    else:
                        pygame.draw.polygon(mask_surface_normal, (255, 255, 255),
                            [
                                point1,
                                point2,
                                point3,
                                point4,
                                point5,
                                point6,
                                point12,
                                point11,
                                point10,
                                point9,
                                point8,
                                point7
                            ])
                
            screen.blit(
                img,
                self.rect
            )

            if self.ani_index == 0:
                self.load_sound.play()

            self.ani_index += 1

            if self.ani_index < self.time1 * 2:
                self.pos[0] += (self.end_pos[0] - self.pos[0]) / 20 * 3
                self.pos[1] += (self.end_pos[1] - self.pos[1]) / 20 * 3
                self.angle  -= (self.end_angle  + self.angle)  / 20 * 3

            elif self.ani_index == self.time1 * 2:
                self.pos   = self.end_pos
                self.angle = 360 - self.end_angle

            elif self.ani_index >= (self.time1 + 5) * 2:
                if self.pos[0] > -200 and \
                   self.pos[1] > -200 and \
                   self.pos[0] < SCREEN_SIZE[0] + 200 and \
                   self.pos[1] < SCREEN_SIZE[1] + 200 and \
                   not self.norecoil:
                    self.pos[0] -= self.back_speed * math.cos(self.radian)
                    self.pos[1] -= self.back_speed * math.sin(self.radian)
                    if not self.norecoil:
                        self.back_speed += 0.25

                if self.ani_index > (self.time1 + self.time2) * 2:
                    if (self.pos[0] < -200 or \
                        self.pos[1] < -200 or \
                        self.pos[0] > SCREEN_SIZE[0] + 200 or \
                        self.pos[1] > SCREEN_SIZE[1] + 200) and \
                        not self.show_light:
                        self.stop = True
                    if self.width > self.end_width / 5:
                        self.width -= self.width / 10
                        self.alpha -= self.alpha / 10
                        if self.alpha < 1:
                            self.alpha = 1
                    else:
                        self.show_light = False

                elif self.width < self.end_width:
                    self.width += (self.end_width - self.width) / 5
                    self.alpha += (self.target_alpha - self.alpha) / 5
