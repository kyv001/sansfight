import pygame
from locals_ import *

class Player:
    '''
    玩家本人
    改变type改变类型
    改变direction改变方向
    '''
    def __init__(self, pos):
        self.HP = 92
        self.KR = 0
        self.going_up = False
        self.going_down = False
        self.going_left = False
        self.going_right = False

        self.pos = pos
        self.type = 1
        self.falling = False
        self.jump_time = 0
        self.direction = 1
        self.jumping_speed = 4
        self.falling_speed = 0

        self.heart = pygame.image.load("res/PlayerHeart/Default/000.png")
        self.heart_blue = pygame.image.load("res/PlayerHeart/Blue/000.png")
        self.heart_blue_right = pygame.transform.rotate(self.heart_blue, 90)
        self.heart_blue_left = pygame.transform.rotate(self.heart_blue, 270)
        self.heart_blue_up = pygame.transform.rotate(self.heart_blue, 180)
        self.blue_images = [self.heart_blue_up, self.heart_blue, self.heart_blue_left, self.heart_blue_right]

        self.options = []
        self.choice = 0
        self.cursor_sound = pygame.mixer.Sound("res/MenuCursor.ogg")
        self.select_sound = pygame.mixer.Sound("res/MenuSelect.ogg")
        self.choose = False
        self.back = False

        self.pos = [round(self.pos[0]), round(self.pos[1])]
        self.rect = pygame.Rect(self.pos, (8, 8))
        self.mask = pygame.mask.from_surface(self.heart)
        self.mask_pos = (self.rect.x - 4, self.rect.y - 4)

    def show(self, screen, BOX_POS, BOX_SIZE):
        self.rect = pygame.Rect(self.pos, (8, 8))
        self.mask = pygame.mask.from_surface(self.heart)
        self.mask_pos = (self.rect.x - 4, self.rect.y - 4)
        
        if self.KR > 0:
            self.KR -= self.KR / 40
        
        if self.type == 1:
            if self.going_up and self.pos[1] > BOX_POS[1] + 5:
                self.pos[1] -= 2
            if self.going_down and self.pos[1] < BOX_POS[1] + BOX_SIZE[1] - 13:
                self.pos[1] += 2
            if self.going_left and self.pos[0] > BOX_POS[0] + 5:
                self.pos[0] -= 2
            if self.going_right and self.pos[0] < BOX_POS[0] + BOX_SIZE[0] - 13:
                self.pos[0] += 2

            screen.blit(self.heart, (self.rect.x - 4, self.rect.y - 4))
# ----------------------------------------------------------------------------------------------------------
        elif self.type == 2:
            if self.direction == DOWN: # 下
                if self.going_up and self.pos[1] > BOX_POS[1] + 5 and not self.falling:
                    self.pos[1] -= self.jumping_speed
                    self.jump_time += 2
                    if self.jumping_speed > 0.1:
                        self.jumping_speed -= 0.1
                if not self.going_up:
                    self.falling = True
                if self.jump_time > 100:
                    self.falling = True
                if self.going_left and self.pos[0] > BOX_POS[0] + 5:
                    self.pos[0] -= 2
                if self.going_right and self.pos[0] < BOX_POS[0] + BOX_SIZE[0] - 13:
                    self.pos[0] += 2

                if self.pos[1] >= BOX_POS[1] + BOX_SIZE[1] - 13:
                    self.falling = False
                    self.falling_speed = 0

                if self.falling:
                    self.pos[1] += self.falling_speed
                    if self.falling_speed < 3:
                        self.falling_speed += 0.2
                    self.jump_time = 0
                    self.jumping_speed = 4

            if self.direction == UP: # 上
                if self.going_down and self.pos[1] < BOX_POS[1] + BOX_SIZE[1] - 13 and not self.falling:
                    self.pos[1] += self.jumping_speed
                    self.jump_time += 2
                    if self.jumping_speed > 0.1:
                        self.jumping_speed -= 0.1
                if not self.going_down:
                    self.falling = True
                if self.jump_time > 100:
                    self.falling = True
                if self.going_left and self.pos[0] > BOX_POS[0] + 5:
                    self.pos[0] -= 2
                if self.going_right and self.pos[0] < BOX_POS[0] + BOX_SIZE[0] - 13:
                    self.pos[0] += 2

                if self.pos[1] <= BOX_POS[1] + 5:
                    self.falling = False
                    self.falling_speed = 0

                if self.falling:
                    self.pos[1] -= self.falling_speed
                    if self.falling_speed < 3:
                        self.falling_speed += 0.2
                    self.jump_time = 0
                    self.jumping_speed = 4

            if self.direction == LEFT: # 左
                if self.going_right and self.pos[0] < BOX_POS[0] + BOX_SIZE[0] - 13 and not self.falling:
                    self.pos[0] += self.jumping_speed
                    self.jump_time += 2
                    if self.jumping_speed > 0.1:
                        self.jumping_speed -= 0.1
                if self.going_up and self.pos[1] > BOX_POS[1] + 5:
                    self.pos[1] -= 2
                if self.going_down and self.pos[1] < BOX_POS[1] + BOX_SIZE[1] - 13:
                    self.pos[1] += 2
                if not self.going_right:
                    self.falling = True
                if self.jump_time > 100:
                    self.falling = True

                if self.pos[0] <= BOX_POS[0] + 5:
                    self.falling = False
                    self.falling_speed = 0

                if self.falling:
                    self.pos[0] -= self.falling_speed
                    if self.falling_speed < 3:
                        self.falling_speed += 0.2
                    self.jump_time = 0
                    self.jumping_speed = 4

            if self.direction == RIGHT: # 右
                if self.going_left and self.pos[0] > BOX_POS[0] + 5 and not self.falling:
                    self.pos[0] -= self.jumping_speed
                    self.jump_time += 2
                    if self.jumping_speed > 0.1:
                        self.jumping_speed -= 0.1
                if self.going_up and self.pos[1] > BOX_POS[1] + 5:
                    self.pos[1] -= 2
                if self.going_down and self.pos[1] < BOX_POS[1] + BOX_SIZE[1] - 13:
                    self.pos[1] += 2
                if not self.going_left:
                    self.falling = True
                if self.jump_time > 100:
                    self.falling = True

                if self.pos[0] >= BOX_POS[0] + BOX_SIZE[0] - 13:
                    self.falling = False
                    self.falling_speed = 0

                if self.falling:
                    self.pos[0] += self.falling_speed
                    if self.falling_speed < 3:
                        self.falling_speed += 0.2
                    self.jump_time = 0
                    self.jumping_speed = 4

            screen.blit(self.blue_images[self.direction], (self.rect.x - 4, self.rect.y - 4))

        elif self.type == 3:
            if self.going_left:
                self.choice -= 1
                if self.choice < 0:
                    self.choice = len(self.options) - 1
                self.cursor_sound.play()
                self.going_left = False
            elif self.going_right:
                self.choice += 1
                if self.choice > len(self.options) - 1:
                    self.choice = 0
                self.cursor_sound.play()
                self.going_right = False

            if self.going_up:
                self.choice -= 1
                if self.choice < 0:
                    self.choice = len(self.options) - 1
                self.cursor_sound.play()
                self.going_up = False
            elif self.going_down:
                self.choice += 1
                if self.choice > len(self.options) - 1:
                    self.choice = 0
                self.cursor_sound.play()
                self.going_down = False
                
            if self.pos[0] != (self.options[self.choice][0] + 4):
                if abs((self.options[self.choice][0] + 4) - self.pos[0]) < 0.1:
                    self.pos[0] = (self.options[self.choice][0] + 4)
                else:
                    self.pos[0] += ((self.options[self.choice][0] + 4) - self.pos[0]) / 3
                    
            if self.pos[1] != (self.options[self.choice][1] + 4):
                if abs((self.options[self.choice][1] + 4) - self.pos[1]) < 0.1:
                    self.pos[1] = (self.options[self.choice][1] + 4)
                else:
                    self.pos[1] += ((self.options[self.choice][1] + 4) - self.pos[1]) / 3
                            
            screen.blit(self.heart, (self.rect.x - 4, self.rect.y - 4))

        if self.type != 3:
            if self.pos[1] <= BOX_POS[1] + 5:
                self.pos[1] = BOX_POS[1] + 5
            if self.pos[1] >= BOX_POS[1] + BOX_SIZE[1] - 13:
                self.pos[1] = BOX_POS[1] + BOX_SIZE[1] - 13
            if self.pos[0] <= BOX_POS[0] + 5:
                self.pos[0] = BOX_POS[0] + 5
            if self.pos[0] >= BOX_POS[0] + BOX_SIZE[0] - 13:
                self.pos[0] = BOX_POS[0] + BOX_SIZE[0] - 13
