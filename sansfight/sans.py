import pygame
from locals_ import *

def image(path): # 懒得一个一个整了
    img = pygame.image.load(path)
    size = img.get_size()
    img_big = pygame.transform.scale(img, (round(size[0] * 2), round(size[1] * 2)))
    return img_big

class Sans:
    '''
    鳝丝本人
    改变headtype改变表情
    改变hand_direction重力控制
    '''
    def __init__(self, pos):
        self.target_pos = pos
        self.pos = pos
        self.speak_sound = pygame.mixer.Sound("res/SansSpeak.ogg")
        
        self.torso = image("res/SansTorso/Default/000.png")
        self.shrug_torso = image("res/SansTorso/Shrug/000.png")
        self.legs = image("res/SansLegs/Standing/000.png")
        self.head = image("res/SansHead/Default/000.png")
        self.closed_eyes_head = image("res/SansHead/ClosedEyes/000.png")
        self.no_eyes_head = image("res/SansHead/NoEyes/000.png")
        self.look_left_head = image("res/SansHead/LookLeft/000.png")
        self.wink_head = image("res/SansHead/Wink/000.png")
        self.blue_eyes_head = [
            image("res/SansHead/BlueEye/000.png"),
            pygame.image.load("res/SansHead/BlueEye/001.png")
        ]
        self.heads = [self.head,
                      self.closed_eyes_head,
                      self.no_eyes_head,
                      self.look_left_head,
                      self.wink_head,
                      self.blue_eyes_head]
        self.headtype = 0
        self.bubble = pygame.transform.scale(
            pygame.image.load("res/SpeechBubble/Default/000.png"),
            (150, 75)
        )
        self.upani = [
            image("res/SansBody/HandUp/000.png"),
            image("res/SansBody/HandUp/001.png"),
            image("res/SansBody/HandUp/002.png"),
            image("res/SansBody/HandUp/003.png"),
            image("res/SansBody/HandUp/004.png")
        ]
        self.downani = [
            image("res/SansBody/HandDown/000.png"),
            image("res/SansBody/HandDown/001.png"),
            image("res/SansBody/HandDown/002.png"),
            image("res/SansBody/HandDown/003.png")
        ]
        self.leftani = [
            image("res/SansBody/HandLeft/000.png"),
            image("res/SansBody/HandLeft/001.png"),
            image("res/SansBody/HandLeft/002.png"),
            image("res/SansBody/HandLeft/003.png"),
            image("res/SansBody/HandLeft/004.png")
        ]
        self.rightani = [
            image("res/SansBody/HandRight/000.png"),
            image("res/SansBody/HandRight/001.png"),
            image("res/SansBody/HandRight/002.png"),
            image("res/SansBody/HandRight/003.png"),
            image("res/SansBody/HandRight/004.png")
        ]
        self.handani = [self.upani,self.downani,self.leftani,self.rightani]
        self.hand_direction = -1
        self.ani_index = 0
        self.body = self.torso
        self.shrug = False
        self.saying = False
        self.show_text = False
        self.text = ""
        self.showing_text = ""
        self.show_index = 0
        self.font = pygame.font.Font("res/sans.ttf", 15)
        self.head_flag = True
        self.time = 1
        self.head_offset_index = 0
        self.body_offset_index = 1
        self.offsets = [
        #    x   y
            [0 , 0 ],
            [0 , 0 ],
            [1 , -1],
            [1 , -1],
            [1 , 0 ],
            [1 , 0 ],
            [1 , 1 ],
            [1 , 1 ],
            [0 , 0 ],
            [0 , 0 ],
            [-1, -1],
            [-1, -1],
            [-1, 0 ],
            [-1, 0 ],
            [-1, 1 ],
            [-1, 1 ]
        ]

    def show(self,screen):
        self.time += 1
        if self.pos[0] != self.target_pos[0]:
            if abs(self.target_pos[0] - self.pos[0]) < 0.1:
                self.pos[0] = self.target_pos[0]
            else:
                self.pos[0] += (self.target_pos[0] - self.pos[0]) / 6
        if self.pos[1] != self.target_pos[1]:
            if abs(self.target_pos[1] - self.pos[1]) < 0.1:
                self.pos[1] = self.target_pos[1]
            else:
                self.pos[1] += (self.target_pos[1] - self.pos[1]) / 6
                
        if self.time >= 5:
            self.time = 0
            self.head_offset_index += 1
            self.body_offset_index += 1
        if self.head_offset_index >= len(self.offsets):
            self.head_offset_index = 0
        if self.body_offset_index >= len(self.offsets):
            self.body_offset_index = 0
        if self.hand_direction != -1:
            self.ani_index += 1
            self.show_normal_body = False
            if self.hand_direction == 0:
                self.body = self.handani[self.hand_direction][self.ani_index // 7]
                screen.blit(self.body, (self.pos[0] - 30, self.pos[1] + 4))
            elif self.hand_direction == 1:
                self.body = self.handani[self.hand_direction][self.ani_index // 7]
                screen.blit(self.body, (self.pos[0] - 30, self.pos[1] + 4))
            elif self.hand_direction == 2:
                self.body = self.handani[self.hand_direction][self.ani_index // 7]
                screen.blit(self.body, (self.pos[0] - 31, self.pos[1] + 46))
            elif self.hand_direction == 3:
                self.body = self.handani[self.hand_direction][self.ani_index // 7]
                screen.blit(self.body, (self.pos[0] - 31, self.pos[1] + 46))
            if self.ani_index >= len(self.handani[self.hand_direction]) * 7 - 1:
                self.ani_index = 0
                self.body = self.torso
                self.hand_direction = -1

        else:
            if self.shrug:
                screen.blit(self.shrug_torso, (
                    self.pos[0] - 36 + self.offsets[self.body_offset_index][0],
                    self.pos[1] + 48 + self.offsets[self.body_offset_index][1]))
            else:
                screen.blit(self.body, (
                    self.pos[0] - 22 + self.offsets[self.body_offset_index][0],
                    self.pos[1] + 48 + self.offsets[self.body_offset_index][1]))
        
        screen.blit(self.legs, (self.pos[0] - 7, self.pos[1] + 99))
        if self.headtype != 5:
            screen.blit(self.heads[self.headtype], [
                self.pos[0] + self.offsets[self.head_offset_index][0],
                self.pos[1] + self.offsets[self.head_offset_index][1]])
        else:
            screen.blit(self.heads[self.headtype][int(self.head_flag)], [
                self.pos[0] + self.offsets[self.head_offset_index][0],
                self.pos[1] + self.offsets[self.head_offset_index][1]])
            self.head_flag = not self.head_flag
        if self.show_text:
            if self.show_index < len(self.text):
                self.show_index += 0.1
                if self.headtype != SANS_NO_EYES:
                    self.speak_sound.play()
                    self.show_index += 0.4
            self.showing_text = self.text[:int(self.show_index)]
            screen.blit(self.bubble, (self.pos[0] + 80, self.pos[1] + 20))
            x = self.pos[0] + 105
            y = self.pos[1] + 25
            for char in list(self.showing_text):
                screen.blit(self.font.render(char, True, (0, 0, 0)), (x, y))
                if '\u4e00' <= char <= '\u9fa5':
                    x += 6
                x += 10
                if x > self.pos[0] + 210:
                    y += 15
                    x = self.pos[0] + 105
    def say(self, text):
        self.text = text
        self.show_text = True
        self.show_index = 0
