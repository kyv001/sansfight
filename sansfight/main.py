import pygame
import time as time_
import random
import os
from pygame.locals import *
from math import sin, cos, pi
from sys import exit
# ---------------------------
from unzip import *
unzip()
# ---------------------------
from others import *
from gaster_blaster import *
from board import *
from bone import *
from sans import *
from player import *
from functions import *
# ----------------------------------------------------------------
'''初始化'''
os.environ["SDL_VIDEO_WINDOW_POS"] = "100,100"
pygame.init()
if FULL_SCREEN:
    display = pygame.display.set_mode((1920, 1080), FULLSCREEN)
else:
    display = pygame.display.set_mode(SCREEN_SIZE)
screen = pygame.Surface(SCREEN_SIZE).convert_alpha()
mask_surface_blue = pygame.Surface(SCREEN_SIZE).convert_alpha()   # 蓝色攻击的mask
mask_surface_orange = pygame.Surface(SCREEN_SIZE).convert_alpha() # 橙色攻击的mask
mask_surface_normal = pygame.Surface(SCREEN_SIZE).convert_alpha() # 普通攻击的mask
pygame.display.set_caption("UPPERTALE") #标题
pygame.display.set_icon(pygame.image.load("res/icon-32.png")) #图标

fps = pygame.time.Clock() # 帧数计时器
frames = 60

# -----------------------------------
'''因为需要修改全局变量
所以不得不写在主文件里的函数'''
def players_turn(text):
    def tmp():
        global is_players_turn, battle_text, shown_index
        is_players_turn = True
        battle_text = text
        shown_index = 0
        bones.clear()
        blasters.clear()
        boards.clear()
    attacks.append(tmp)

def set_turn_time(time):
    def next_turn(screen):
        global stop
        stop = False
    tasks.append(Task(next_turn, time))

def add_attack(func):
    attacks.append(func)
    return func

def shake(screen):
    global screen_shaking
    screen_shaking = True

def unshake(screen):
    global screen_shaking
    screen_shaking = False

def set_screen_angle(angle):
    global screen_angle
    screen_angle = angle

def start_testing():
    attacks.clear()

# -------------------------------------
'''回合'''
# 吟唱
@add_attack
def yinchang_1():
    global BOX_POS, BOX_SIZE
    BOX_POS = [230, 230]
    BOX_SIZE = [170, 160]
    if DEBUG:
        # 测试区开始
        pass
    # 测试区结束
    sans.say("准备好了？")

# 开头杀
@add_attack
def first_round1():
    set_turn_time(50)
    sans.hand_direction = DOWN
    player.type = BLUE_SOUL
    player.direction = DOWN
    player.falling_speed = 10
    player.falling = True
    tasks.append(Task(shake,
        (BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10))
    tasks.append(Task(unshake,
        ((BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10) + 5))
    tasks.append(Task(lambda screen : slam_sound.play(),
        (BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10))
    for x in range(BOX_POS[0], BOX_POS[0] + BOX_SIZE[0], 10):
        bones.append(
            Bone(
                pos=[x, BOX_POS[1] + BOX_SIZE[1] - 7],
                speed=[0, -5],
                direction=UP,
                time1=8,
                time2=40,
                length=1000,
                type_=1
            )
        )

        bones.append(
            Bone(
                pos=[x, BOX_POS[1] + BOX_SIZE[1] - 47],
                speed=[0, 0],
                direction=UP,
                time1=200,
                time2=48,
                length=1000,
                type_=1
            )
        )

        bones.append(
            Bone(
                pos=[x, BOX_POS[1] + BOX_SIZE[1] - 47],
                speed=[0, 5],
                direction=UP,
                time1=8,
                time2=248,
                length=1000,
                type_=1
            )
        )
@add_attack
def first_round2():
    set_turn_time(50)
    sans.hand_direction = LEFT
    player.type = BLUE_SOUL
    player.direction = LEFT
    player.falling_speed = 10
    player.falling = True
    tasks.append(Task(shake,
        (player.pos[0] - BOX_POS[0]) // 10))
    tasks.append(Task(unshake,
        ((player.pos[0] - BOX_POS[0]) // 10) + 5))
    tasks.append(Task(lambda screen : slam_sound.play(),
        (player.pos[0] - BOX_POS[0]) // 10))
    for y in range(BOX_POS[1], BOX_POS[1] + BOX_SIZE[1], 10):
        bones.append(
            Bone(
                pos=[BOX_POS[0] - 7, y],
                speed=[0, 0, 5],
                direction=LEFT,
                time1=8,
                time2=30,
                length=0,
                type_=2
            )
        )
        bones.append(
            Bone(
                pos=[BOX_POS[0] - 7, y],
                speed=[0, 0, 0],
                direction=LEFT,
                time1=150,
                time2=38,
                length=40,
                type_=2
            )
        )
        bones.append(
            Bone(
                pos=[BOX_POS[0] - 7, y],
                speed=[0, 0, -5],
                direction=LEFT,
                time1=8,
                time2=188,
                length=40,
                type_=2
            )
        )

@add_attack
def first_round3():
    set_turn_time(450)
    player.type = RED_SOUL
    for _ in range(0, 300, 2):
        bones.append(
            Bone(
                pos=BOX_POS,
                length=40 + sin(_ / 20) * 40,
                direction=UP,
                speed=[7, 0],
                time1=1000,
                time2=_,
            )
        )
        bones.append(
            Bone(
                pos=[BOX_POS[0], BOX_POS[1] + 25 + (sin(_ / 20) * 40) + 60],
                length=1000,
                direction=UP,
                speed=[7, 0],
                time1=1000,
                time2=_,
            )
        )

@add_attack
def first_round4():
    sans.headtype = SANS_LOOK_LEFT
    sans.say("只是第一个回合而已，何必用尽全力？")

@add_attack
def first_round5():
    set_turn_time(1)
    sans.headtype = SANS_NORMAL
    pygame.mixer.music.play(-1)

players_turn("* ...")

@add_attack
def zjj_1():
    set_turn_time(60)
    global BOX_POS, BOX_SIZE
    BOX_POS = [200, 230]
    BOX_SIZE = [200, 150]
    sans.hand_direction = DOWN
    player.type = BLUE_SOUL
    player.direction = DOWN
    player.falling_speed = 10
    tasks.append(Task(shake,
        (BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10))
    tasks.append(Task(unshake,
        ((BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10) + 5))
    tasks.append(Task(lambda screen : slam_sound.play(),
        (BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10))

@add_attack
def zjj_2():
    set_turn_time(11 * 100)
    def zjj(screen):
        angle = random.randint(240, 300)
        blasters.append(GasterBlaster(
            pos=[
                player.pos[0] + math.cos(math.radians(angle)) * 200,
                player.pos[1] + math.sin(math.radians(angle)) * 200],
            angle=angle - 180,
            time1=10,
            time2=30,
            width=30,
            color=BLUE
            ))
    for _ in range(10):
        tasks.append(Task(zjj, _ * 100))
        bones.append(
            Bone(
                pos=[BOX_POS[0] - 20, BOX_POS[1] - 8],
                length=BOX_SIZE[1] - 30 - 16,
                direction=DOWN,
                time1=1000,
                time2=_ * 100 + 60,
                speed=[2, 0],
                type_=2
                ))
            
        bones.append(
            Bone(
                pos=[BOX_POS[0] + BOX_SIZE[0] + 20, BOX_POS[1] - 8],
                length=BOX_SIZE[1] - 30 - 16,
                direction=DOWN,
                time1=1000,
                time2=_ * 100 + 60,
                speed=[-2, 0],
                type_=2
                ))

        
        bones.append(
            Bone(
                pos=[BOX_POS[0] - 20, BOX_POS[1] + BOX_SIZE[1] - 10 - 8],
                length=1000,
                direction=DOWN,
                time1=1000,
                time2=_ * 100 + 60,
                speed=[2, 0],
                type_=1
                ))
            
        bones.append(
            Bone(
                pos=[BOX_POS[0] + BOX_SIZE[0] + 20, BOX_POS[1] + BOX_SIZE[1] - 10 - 8],
                length=1000,
                direction=DOWN,
                time1=1000,
                time2=_ * 100 + 60,
                speed=[-2, 0],
                type_=1
                ))

players_turn("* ...")

@add_attack
def blue_bone():
    set_turn_time(700)
    global BOX_POS, BOX_SIZE
    BOX_POS = [150, 250]
    BOX_SIZE = [350, 120]
    sans.hand_direction = DOWN
    player.type = BLUE_SOUL
    player.direction = DOWN
    player.falling_speed = 10
    tasks.append(Task(shake,
        (BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10))
    tasks.append(Task(unshake,
        ((BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10) + 5))
    tasks.append(Task(lambda screen : slam_sound.play(),
        (BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10))
    for _ in range(10):
        bones.append(
            Bone(
                pos=[BOX_POS[0], BOX_POS[1] - 8],
                length=BOX_SIZE[1] - 30 - 16,
                direction=DOWN,
                time1=1000,
                time2=_ * 60 + 60,
                speed=[4, 0],
                type_=2
                ))
        
        bones.append(
            Bone(
                pos=[BOX_POS[0], BOX_POS[1] + BOX_SIZE[1] - 10 - 8],
                length=1000,
                direction=DOWN,
                time1=1000,
                time2=_ * 60 + 60,
                speed=[4, 0],
                type_=1
                ))
        
        bones.append(
            Bone(
                pos=BOX_POS,
                length=1000,
                direction=DOWN,
                time1=1000,
                time2=_ * 60 + 60 + 16,
                speed=[4, 0],
                type_=1,
                color=BLUE
                ))
        
@add_attack
def orange_bone():
    def start_spinning(screen):
        global spinning_left
        spinning_left = True
    def stop_spinning(screen):
        global spinning_left
        spinning_left = False
    tasks.append(Task(start_spinning, 0))
    tasks.append(Task(stop_spinning, 180))
    tasks.append(Task(lambda screen:set_screen_angle(180), 181))
    tasks.append(Task(start_spinning, 520))
    tasks.append(Task(stop_spinning, 700))
    tasks.append(Task(lambda screen:set_screen_angle(0), 701))
    set_turn_time(700)
    sans.hand_direction = UP
    player.type = BLUE_SOUL
    player.direction = UP
    player.falling_speed = 10
    tasks.append(Task(shake,
        (player.pos[1] - BOX_POS[1]) // 10))
    tasks.append(Task(unshake,
        ((player.pos[1] - BOX_POS[1]) // 10) + 5))
    tasks.append(Task(lambda screen : slam_sound.play(),
        (BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10))
    for _ in range(10):
        bones.append(
            Bone(
                pos=[BOX_POS[0], BOX_POS[1] - 8],
                length=10,
                direction=DOWN,
                time1=1000,
                time2=_ * 60 + 60,
                speed=[8, 0],
                type_=2
                ))
        
        bones.append(
            Bone(
                pos=[BOX_POS[0], BOX_POS[1] + 30 + 16],
                length=1000,
                direction=DOWN,
                time1=1000,
                time2=_ * 60 + 60,
                speed=[8, 0],
                type_=1
                ))
        
        bones.append(
            Bone(
                pos=BOX_POS,
                length=1000,
                direction=DOWN,
                time1=1000,
                time2=_ * 60 + 60 + 8,
                speed=[8, 0],
                type_=1,
                color=ORANGE
                ))

players_turn("* ...")

@add_attack
def bone_gap():
    set_turn_time(1000)
    global BOX_POS, BOX_SIZE
    BOX_POS = [150, 230]
    BOX_SIZE = [300, 150]
    sans.hand_direction = DOWN
    player.type = BLUE_SOUL
    player.direction = DOWN
    player.falling_speed = 10
    tasks.append(Task(shake,
        (BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10))
    tasks.append(Task(unshake,
        ((BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10) + 5))
    tasks.append(Task(lambda screen : slam_sound.play(),
        (BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10))
    for _ in range(10):
        x = BOX_POS[0] + random.randint(100, BOX_SIZE[0] - 100)
        bones.append(Bone(
            pos=[x, BOX_POS[1]],
            time1=10,
            time2=_ * 100,
            speed=[0, 0, BOX_SIZE[1] / 10],
            length=0,
            direction=DOWN,
            color=BLUE
        ))
        bones.append(Bone(
            pos=[x, BOX_POS[1]],
            time1=10,
            time2=_ * 100 + 10,
            speed=[0, 0, -BOX_SIZE[1] / 10],
            length=BOX_SIZE[1],
            direction=DOWN,
            color=BLUE
        ))
        tasks.append(Task(shake,_ * 100 + 10))
        tasks.append(Task(unshake,_ * 100 + 15))
        tasks.append(Task(lambda screen : slam_sound.play(),
                          _ * 100 + 15))
        
        y = BOX_POS[1] + random.randint(70, BOX_SIZE[1] - 30)
        bones.append(Bone(
            pos=[BOX_POS[0], y],
            time1=10,
            time2=_ * 100,
            speed=[0, 0, BOX_SIZE[0] / 10],
            length=0,
            direction=RIGHT,
            color=ORANGE
        ))
        bones.append(Bone(
            pos=[BOX_POS[0], y],
            time1=10,
            time2=_ * 100 + 10,
            speed=[0, 0, -BOX_SIZE[0] / 10],
            length=BOX_SIZE[0],
            direction=RIGHT,
            color=ORANGE
        ))

        
        bones.append(
            Bone(
                pos=[BOX_POS[0], BOX_POS[1] - 8],
                length=y - BOX_POS[1] - 16,
                direction=DOWN,
                time1=1000,
                time2=_ * 100 + 60,
                speed=[(x - BOX_POS[0]) / 30, 0],
                type_=2
                ))
            
        bones.append(
            Bone(
                pos=[BOX_POS[0] + BOX_SIZE[0], BOX_POS[1] - 8],
                length=y - BOX_POS[1] - 16,
                direction=DOWN,
                time1=1000,
                time2=_ * 100 + 60,
                speed=[-((BOX_SIZE[0] + BOX_POS[0] - x) / 30), 0],
                type_=2
                ))

        
        bones.append(
            Bone(
                pos=[BOX_POS[0], y + 8],
                length=1000,
                direction=DOWN,
                time1=1000,
                time2=_ * 100 + 60,
                speed=[(x - BOX_POS[0]) / 30, 0],
                type_=1
                ))
            
        bones.append(
            Bone(
                pos=[BOX_POS[0] + BOX_SIZE[0], y + 8],
                length=1000,
                direction=DOWN,
                time1=1000,
                time2=_ * 100 + 60,
                speed=[-((BOX_SIZE[0] + BOX_POS[0] - x) / 30), 0],
                type_=1
                ))

players_turn("* ...")

@add_attack
def board_1():
    set_turn_time(10)
    global BOX_POS, BOX_SIZE
    BOX_POS = [50, 240]
    BOX_SIZE = [500, 140]
    sans.hand_direction = DOWN
    player.type = BLUE_SOUL
    player.direction = DOWN
    player.falling_speed = 10
    tasks.append(Task(shake,
        (BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10))
    tasks.append(Task(unshake,
        ((BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10) + 5))
    tasks.append(Task(lambda screen : slam_sound.play(),
        (BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10))
    
@add_attack
def board_2():
    set_turn_time(600)
    tasks.append(Task(shake, 70))
    tasks.append(Task(unshake, 75))
    blasters.append(
        GasterBlaster(
            pos=[10, BOX_POS[1] + BOX_SIZE[1]],
            angle=0,
            time1=10,
            time2=70,
            time3=10,
            width=70
        )
    )

    blasters.append(
        GasterBlaster(
            pos=[10, BOX_POS[1]],
            angle=0,
            time1=10,
            time2=70,
            time3=10,
            width=30
        )
    )

    for x in range(BOX_POS[0], BOX_POS[0] + BOX_SIZE[0], 12):
        bones.append(
            Bone(
                pos=[x, BOX_POS[1] + BOX_SIZE[1] - 30],
                length=1000,
                direction=UP,
                time1=1000,
                time2=100,
                speed=[0, 0],
                type_=1
            )
        )
        bones.append(
            Bone(
                pos=[x, BOX_POS[1] - 8],
                length=5,
                direction=DOWN,
                time1=1000,
                time2=100,
                speed=[0, 0],
                type_=2
            )
        )
    boards.append(
        Board(
            pos=[BOX_POS[0],BOX_POS[1] + BOX_SIZE[1] - 40],
            length=40,
            speed=[1, 0],
            time1=BOX_SIZE[0],
            time2=100,
            direction=UP
        )
    )

    for _ in range(0, 20, 4):
        bones.append(
            Bone(
                pos=[BOX_POS[0] + BOX_SIZE[0],
                     BOX_POS[1] + BOX_SIZE[1] - 40 - 25],
                length=1000,
                direction=UP,
                time1=BOX_SIZE[0] // 4,
                time2=150 + (_ * 30),
                speed=[-4, 0]
            )
        )
    def start_spinning(screen):
        global spinning_left
        spinning_left = True
    def stop_spinning(screen):
        global spinning_left
        spinning_left = False
    tasks.append(Task(start_spinning, 200))
    tasks.append(Task(stop_spinning, 380))
    tasks.append(Task(start_spinning, 500))
    tasks.append(Task(stop_spinning, 680))
    tasks.append(Task(lambda screen:set_screen_angle(0), 682))

@add_attack
def board_3():
    set_turn_time(100)
    sans.hand_direction = LEFT
    player.type = BLUE_SOUL
    player.direction = LEFT
    player.falling_speed = 10
    tasks.append(Task(shake,
        (player.pos[0] - BOX_POS[0]) // 10))
    tasks.append(Task(unshake,
        ((player.pos[0] - BOX_POS[0]) // 10) + 5))
    tasks.append(Task(lambda screen : slam_sound.play(),
        (player.pos[0] - BOX_POS[0]) // 10))
    
    tasks.append(Task(shake, 60))
    tasks.append(Task(unshake, 65))
    blasters.append(
        GasterBlaster(
            pos=[BOX_POS[0], 10],
            angle=90,
            time1=10,
            time2=50,
            time3=0,
            width=50
        )
    )

@add_attack
def board_4():
    set_turn_time(0)
    bones.clear()

players_turn("* ...")

@add_attack
def board_2_1():
    set_turn_time(10)
    global BOX_POS, BOX_SIZE
    BOX_POS = [50, 240]
    BOX_SIZE = [500, 140]
    sans.hand_direction = DOWN
    player.type = BLUE_SOUL
    player.direction = DOWN
    player.falling_speed = 10
    tasks.append(Task(shake,
        (BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10))
    tasks.append(Task(unshake,
        ((BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10) + 5))
    tasks.append(Task(lambda screen : slam_sound.play(),
        (BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10))

@add_attack
def board_2_2():
    set_turn_time(600)
    tasks.append(Task(shake, 70))
    tasks.append(Task(unshake, 75))
    blasters.append(
        GasterBlaster(
            pos=[10, BOX_POS[1] + BOX_SIZE[1]],
            angle=0,
            time1=10,
            time2=70,
            time3=10,
            width=70
        )
    )
    
    tasks.append(Task(shake, 250))
    tasks.append(Task(unshake, 255))
    blasters.append(
        GasterBlaster(
            pos=[10, BOX_POS[1] + BOX_SIZE[1] - 20],
            angle=0,
            time1=10,
            time2=70,
            time3=250,
            width=70
        )
    )

    boards.append(
        Board(
            pos=[BOX_POS[0] + BOX_SIZE[0],
                 BOX_POS[1] + BOX_SIZE[1] - 30 - 10],
            time1=1000,
            time2=0,
            speed=[-2, 0],
            length=40
        )
    )

    boards.append(
        Board(
            pos=[BOX_POS[0] + BOX_SIZE[0],
                 BOX_POS[1] + BOX_SIZE[1] - 30 - 10],
            time1=1000,
            time2=100,
            speed=[-1.5, 0],
            length=40
        )
    )

    boards.append(
        Board(
            pos=[BOX_POS[0] + BOX_SIZE[0],
                 BOX_POS[1] + BOX_SIZE[1] - 30 - 10],
            time1=1000,
            time2=200,
            speed=[-1, 0],
            length=40
        )
    )

    boards.append(
        Board(
            pos=[BOX_POS[0] + BOX_SIZE[0],
                 BOX_POS[1] + BOX_SIZE[1] - 30 - 30],
            time1=1000,
            time2=300,
            speed=[-3, 0],
            length=80
        )
    )
    
    for x in range(BOX_POS[0], BOX_POS[0] + BOX_SIZE[0], 12):
        bones.append(
            Bone(
                pos=[x, BOX_POS[1] + BOX_SIZE[1] - 30],
                length=1000,
                direction=UP,
                time1=400,
                time2=100,
                speed=[0, 0],
                type_=1
            )
        )

        bones.append(
            Bone(
                pos=[x, BOX_POS[1] + BOX_SIZE[1] - 30],
                length=1000,
                direction=UP,
                time1=1000,
                time2=500,
                speed=[0, 0],
                type_=1
            )
        )

players_turn("* ...")

@add_attack
def bone_lid1():
    set_turn_time(70)
    global BOX_SIZE, BOX_POS
    BOX_POS = [200, 240]
    BOX_SIZE = [200, 150]
    sans.hand_direction = DOWN
    player.type = BLUE_SOUL
    player.direction = DOWN
    player.falling_speed = 10
    tasks.append(Task(shake,
        (BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10))
    tasks.append(Task(unshake,
        ((BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10) + 5))
    tasks.append(Task(lambda screen : slam_sound.play(),
        (BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10))
    bones.append(
        RotatableBone(
            pos=[BOX_POS[0] - 70, BOX_POS[1] + BOX_SIZE[1]],
            time1=1000,
            length=130,
            angle=45,
            speed=[5, 0, 0, 0]
        )
    )
    bones.append(
        RotatableBone(
            pos=[BOX_POS[0] + BOX_SIZE[0] + 70, BOX_POS[1] + BOX_SIZE[1]],
            time1=1000,
            length=130,
            angle=-45,
            speed=[-5, 0, 0, 0]
        )
    )

@add_attack
def bone_lid2():
    set_turn_time(60)
    sans.hand_direction = UP
    player.type = BLUE_SOUL
    player.direction = UP
    player.falling_speed = 10
    player.falling = True
    tasks.append(Task(shake,
        (player.pos[1] - BOX_POS[1]) // 10))
    tasks.append(Task(unshake,
        ((player.pos[1] - BOX_POS[1]) // 10) + 5))
    tasks.append(Task(lambda screen : slam_sound.play(),
        (BOX_POS[1] + BOX_SIZE[1] - player.pos[1]) // 10))
    bones.append(
        RotatableBone(
            pos=[BOX_POS[0] - 20, BOX_POS[1]],
            time1=1000,
            length=130,
            angle=-45,
            speed=[5, 0, 0, 0]
        )
    )
    bones.append(
        RotatableBone(
            pos=[BOX_POS[0] + BOX_SIZE[0] + 20, BOX_POS[1]],
            time1=1000,
            length=130,
            angle=45,
            speed=[-5, 0, 0, 0]
        )
    )

@add_attack
def bone_lid3():
    set_turn_time(1300)
    player.type = RED_SOUL
    for _ in range(20):
        bones.append(
            RotatableBone(
                pos=[BOX_POS[0], BOX_POS[1] - 20],
                time1=1000,
                time2=_ * 60,
                length=260,
                angle=-45,
                speed=[0, 2, 0, 0]
            )
        )
        bones.append(
            RotatableBone(
                pos=[BOX_POS[0], BOX_POS[1] + BOX_SIZE[1] + 20],
                time1=1000,
                time2=_ * 60,
                length=260,
                angle=45,
                speed=[0, -2, 0, 0]
            )
        )
        
        bones.append(
            RotatableBone(
                pos=[BOX_POS[0] + BOX_SIZE[0], BOX_POS[1] - 20],
                time1=1000,
                time2=_ * 60 + 30,
                length=260,
                angle=45,
                speed=[0, 2, 0, 0]
            )
        )
        bones.append(
            RotatableBone(
                pos=[BOX_POS[0] + BOX_SIZE[0], BOX_POS[1] + BOX_SIZE[1] + 20],
                time1=1000,
                time2=_ * 60 + 30,
                length=260,
                angle=-45,
                speed=[0, -2, 0, 0]
            )
        )

players_turn("* ...")

@add_attack
def mercy1():
    pygame.mixer.music.pause()
    sans.say("好了，我也累了，不如我们休息一下？")

@add_attack
def mercy2():
    sans.say("这也是一个改过自新的机会，")

@add_attack
def mercy3():
    sans.say("赶紧按下饶恕，")

@add_attack
def mercy4():
    sans.headtype = SANS_NO_EYES
    sans.say("否则你绝对不想见到下一个回合")

@add_attack
def mercy5():
    set_turn_time(0)
    sans.headtype = SANS_NORMAL
    
players_turn("* ...")
@add_attack
def before_flash():
    sans.say("好吧，看来你已经做出了自己的选择。")
    
@add_attack
def flash_round():
    set_turn_time(10)
    global blackout
    flash_sound.play()
    blackout = True
    bones.clear()
    blasters.clear()
    boards.clear()
    def flash(screen):
        global blackout
        blackout = False
        flash_sound.play()
        pygame.mixer.music.unpause()
    tasks.append(Task(flash, 10))
    
def flash_round_1():
    set_turn_time(150)
    global _boxsize, _boxpos, BOX_POS, BOX_SIZE
    player.type = BLUE_SOUL
    player.direction = DOWN
    BOX_SIZE = _boxsize = [150, 150]
    BOX_POS = _boxpos = [230, 230]
    player.pos = [BOX_POS[0] + BOX_SIZE[0] / 2,
                  100000]
    direction = random.randint(0, 1)
    blasters.append(
        GasterBlaster(
            pos=[BOX_POS[0] - 30, BOX_POS[1] + BOX_SIZE[1] - 30],
            angle=0,
            time1=0,
            time2=30,
            time3=10,
            width=90
        )
    )
    blasters.append(
        GasterBlaster(
            pos=[BOX_POS[0] - 30, BOX_POS[1] - 30],
            angle=0,
            time1=0,
            time2=30,
            time3=60,
            width=90
        )
    )
    if direction:
        blasters.append(
            GasterBlaster(
                pos=[BOX_POS[0] + BOX_SIZE[0], BOX_POS[1] - 30],
                angle=90,
                time1=0,
                time2=30,
                time3=10,
                width=90
            )
        )
        blasters.append(
            GasterBlaster(
                pos=[BOX_POS[0], BOX_POS[1] - 30],
                angle=90,
                time1=0,
                time2=30,
                time3=60,
                width=90
            )
        )
    else:
        blasters.append(
            GasterBlaster(
                pos=[BOX_POS[0], BOX_POS[1] - 30],
                angle=90,
                time1=0,
                time2=30,
                time3=10,
                width=90
            )
        )
        blasters.append(
            GasterBlaster(
                pos=[BOX_POS[0] + BOX_SIZE[0], BOX_POS[1] - 30],
                angle=90,
                time1=0,
                time2=30,
                time3=60,
                width=90
            )
        )
    for angle in range(0, 360, 10):
        bones.append(RotatableBone(
            pos=[BOX_POS[0] + BOX_SIZE[0] / 2 + cos(radians(angle)) * BOX_SIZE[0] / 2,
                 BOX_POS[1] + BOX_SIZE[1] / 2 + 25 + sin(radians(angle)) * BOX_SIZE[1] / 2],
            length=25,
            angle=angle,
            time1=150
            )
        )
        if angle % 30 == 0:
            bones.append(RotatableBone(
                pos=[BOX_POS[0] + BOX_SIZE[0] / 2,
                     BOX_POS[1] + BOX_SIZE[1] / 2 + 25],
                length=40,
                angle=angle,
                speed=[0, 0, 0, 5],
                time1=130,
                time2=20
                )
            )

def flash_round_2():
    set_turn_time(100)
    global _boxsize, _boxpos, BOX_POS, BOX_SIZE
    BOX_SIZE = _boxsize = [150, 150]
    BOX_POS = _boxpos = [230, 230]
    player.type = RED_SOUL
    player.pos = [BOX_POS[0] + BOX_SIZE[0] / 2,
                  BOX_POS[1] + BOX_SIZE[1] / 2]
    def zjj(screen):
        angle = random.randint(-140, -40)
        d = random.randint(10, 200)
        blasters.append(GasterBlaster(
            pos=[
                player.pos[0] + math.cos(math.radians(angle)) * d,
                player.pos[1] + math.sin(math.radians(angle)) * d],
            angle=angle - 180,
            time1=0,
            time2=20,
            width=50
            ))
    for _ in range(0, 50):
        tasks.append(Task(zjj, _ / 2))

def flash_round_3():
    set_turn_time(100)
    global _boxsize, _boxpos, BOX_POS, BOX_SIZE
    BOX_SIZE = _boxsize = [150, 150]
    BOX_POS = _boxpos = [200, 230]
    player.type = RED_SOUL
    player.pos = [BOX_POS[0] + BOX_SIZE[0] / 2,
                  BOX_POS[1] + BOX_SIZE[1] / 2]
    blasters.append(
        GasterBlaster(
            pos=[BOX_POS[0] + BOX_SIZE[0] / 2, 50],
            angle=90,
            time1=10,
            time2=70,
            time3=0,
            width=60
        )
    )
    blasters.append(
        GasterBlaster(
            pos=[50, BOX_POS[1] + BOX_SIZE[1] / 2],
            angle=0,
            time1=10,
            time2=70,
            time3=0,
            width=60
        )
    )
    
def flash_round_4():
    set_turn_time(100)
    global _boxsize, _boxpos, BOX_POS, BOX_SIZE
    BOX_SIZE = _boxsize = [150, 150]
    BOX_POS = _boxpos = [230, 230]
    player.type = RED_SOUL
    player.pos = [BOX_POS[0] + BOX_SIZE[0] / 2,
                  BOX_POS[1] + BOX_SIZE[1] / 2]
    blasters.append(
        GasterBlaster(
            pos=[BOX_POS[0] - 10, BOX_POS[1] - 10],
            angle=45,
            time1=10,
            time2=70,
            time3=0,
            width=60
        )
    )
    blasters.append(
        GasterBlaster(
            pos=[BOX_POS[0] - 10, BOX_POS[1] + BOX_SIZE[1] + 10],
            angle=-45,
            time1=10,
            time2=70,
            time3=0,
            width=60
        )
    )
    
def flash_round_5():
    set_turn_time(100)
    global _boxsize, _boxpos, BOX_POS, BOX_SIZE
    BOX_SIZE = _boxsize = [150, 150]
    BOX_POS = _boxpos = [230, 230]
    player.type = RED_SOUL
    player.pos = [BOX_POS[0] + BOX_SIZE[0] / 2,
                  BOX_POS[1] + BOX_SIZE[1] / 2]
    blasters.append(
        GasterBlaster(
            pos=[BOX_POS[0], 50],
            angle=90,
            time1=10,
            time2=70,
            time3=0,
            width=60
        )
    )
    blasters.append(
        GasterBlaster(
            pos=[BOX_POS[0] + BOX_SIZE[0], 50],
            angle=90,
            time1=10,
            time2=70,
            time3=0,
            width=60
        )
    )
    blasters.append(
        GasterBlaster(
            pos=[50, BOX_POS[1] + 50],
            angle=0,
            time1=10,
            time2=70,
            time3=0,
            width=100
        )
    )
    
def flash_round_6():
    set_turn_time(100)
    global _boxsize, _boxpos, BOX_POS, BOX_SIZE
    BOX_SIZE = _boxsize = [150, 150]
    BOX_POS = _boxpos = [230, 230]
    player.type = RED_SOUL
    player.pos = [BOX_POS[0] + BOX_SIZE[0] / 2,
                  BOX_POS[1] + BOX_SIZE[1] / 2]
    blasters.append(
        GasterBlaster(
            pos=[BOX_POS[0], 50],
            angle=90,
            time1=10,
            time2=70,
            time3=0,
            width=60
        )
    )
    blasters.append(
        GasterBlaster(
            pos=[BOX_POS[0] + BOX_SIZE[0], 50],
            angle=90,
            time1=10,
            time2=70,
            time3=0,
            width=60
        )
    )
    blasters.append(
        GasterBlaster(
            pos=[50, BOX_POS[1] + BOX_SIZE[1] - 50],
            angle=0,
            time1=10,
            time2=70,
            time3=0,
            width=100
        )
    )
    
def flash_round_7():
    set_turn_time(150)
    global BOX_SIZE, BOX_POS, _boxpos, _boxsize
    BOX_POS = _boxpos = [230, 230]
    BOX_SIZE = _boxsize = [150, 150]
    player.type = RED_SOUL
    player.pos = [BOX_POS[0] + BOX_SIZE[0] / 2,
                  BOX_POS[1] + BOX_SIZE[1] / 2]
    for _ in range(3):
        bones.append(
            RotatableBone(
                pos=[BOX_POS[0], BOX_POS[1] - 20],
                time1=1000,
                time2=_ * 50 + 20,
                length=150,
                angle=-20,
                speed=[0, 4, 0, 0]
            )
        )
        bones.append(
            RotatableBone(
                pos=[BOX_POS[0], BOX_POS[1] + BOX_SIZE[1] + 20],
                time1=1000,
                time2=_ * 50 + 20,
                length=150,
                angle=20,
                speed=[0, -4, 0, 0]
            )
        )
        
        bones.append(
            RotatableBone(
                pos=[BOX_POS[0] + BOX_SIZE[0], BOX_POS[1] - 20],
                time1=1000,
                time2=_ * 50 + 50,
                length=150,
                angle=20,
                speed=[0, 4, 0, 0]
            )
        )
        bones.append(
            RotatableBone(
                pos=[BOX_POS[0] + BOX_SIZE[0], BOX_POS[1] + BOX_SIZE[1] + 20],
                time1=1000,
                time2=_ * 50 + 50,
                length=150,
                angle=-20,
                speed=[0, -4, 0, 0]
            )
        )
    

random_attacks = [flash_round_1,
                  flash_round_2,
                  flash_round_3,
                  flash_round_4,
                  flash_round_5,
                  flash_round_6,
                  flash_round_7]
for _ in range(5):
    attacks.append(random.choice(random_attacks))
    attacks.append(flash_round)
    
players_turn("* ...")
        
@add_attack
def windmill():
    set_turn_time(1200)
    global BOX_POS, BOX_SIZE, before_strike, after_strike
    def before_strike():
        global sans_damage
        sans_damage = 1
    after_strike = lambda : ...
    BOX_POS = [150, 240]
    BOX_SIZE = [150, 150]

    def movegb(screen):
        for i in range(4):
            blasters[i].angle += 1
            blasters[i].end_angle += 1
            blasters[i].radian += radians(-1)
            blasters[i].back_speed = 0

    for angle in range(360 * 5):
        tasks.append(Task(movegb, angle * 0.4 + 100))
        
    def enablerecoil(screen):
        for b in blasters:
            b.norecoil = False

    tasks.append(Task(enablerecoil, 800))

    for angle in range(0, 360, 90):
        blasters.append(GasterBlaster(
            pos=[150 + 150 / 2, 240 + 150 / 2],
            angle=angle,
            time1=10,
            time2=1000,
            width=30,
            time3=0,
            norecoil=True
        ))

players_turn("* ...")

@add_attack
def gameend():
    ...

# ------------------------------------
"""主程序"""

while True:
    # ---------------------------------------------------------
    '''实例化'''
    from locals_ import *
    time = 0
    _boxpos = [0, 0]
    _boxsize = SCREEN_SIZE[:]
    rightdown = SCREEN_SIZE[:]

    time1 = 0
    time2 = 0
    delta = 1
    blasters = []
    bones = []
    tasks = []
    warns = []
    texts = []
    boards = []
    before_strike = None
    after_strike = None
    sans = Sans([280, 80])
    player = Player([0, 0])
    actions = {
        "* check" : CHECK_SANS,
        "* heal ({} time(s) left)" : HEAL_SANS
    }
    mc_actions = {
        "* spare" : MERCY_SANS_SPARE,
        "* flee"  : MERCY_SANS_FLEE
    }
    pygame.mixer.music.stop()
    if FULL_SCREEN:
        display = pygame.display.set_mode((1920, 1080), FULLSCREEN)
    else:
        display = pygame.display.set_mode(SCREEN_SIZE)
    while True:
        time1 = time_.time()
        # 屏幕震动
        if screen_shaking:
            screen_offset[0] = random.randint(-5, 5)
            screen_offset[1] = random.randint(-5, 5)
        else:
            screen_offset = [0, 0]
        # 屏幕旋转
        if spinning_left:
            screen_angle -= 1
        # 屏幕旋转
        if spinning_right:
            screen_angle += 1
        # 测试区
        if DEBUG:...
        # 战斗框位移
        if _boxpos[0] != BOX_POS[0]:
            if abs(BOX_POS[0] - _boxpos[0]) < 0.1:
                _boxpos[0] = BOX_POS[0]
            else:
                _boxpos[0] += (BOX_POS[0] - _boxpos[0]) / 5
        if _boxpos[1] != BOX_POS[1]:
            if abs(BOX_POS[1] - _boxpos[1]) < 0.1:
                _boxpos[1] = BOX_POS[1]
            else:
                _boxpos[1] += (BOX_POS[1] - _boxpos[1]) / 5

        # 战斗框大小
        if rightdown[0] != BOX_POS[0] + BOX_SIZE[0]:
            if abs(BOX_POS[0] + BOX_SIZE[0] - rightdown[0]) < 0.1:
                rightdown[0] = BOX_POS[0] + BOX_SIZE[0]
            else:
                rightdown[0] += (BOX_POS[0] + BOX_SIZE[0] - rightdown[0]) / 5
        if rightdown[1] != BOX_POS[1] + BOX_SIZE[1]:
            if abs(BOX_POS[1] + BOX_SIZE[1] - rightdown[1]) < 0.1:
                rightdown[1] = BOX_POS[1] + BOX_SIZE[1]
            else:
                rightdown[1] += (BOX_POS[1] + BOX_SIZE[1] - rightdown[1]) / 5
        _boxsize = [
            rightdown[0] - _boxpos[0],
            rightdown[1] - _boxpos[1]
        ]

        if time >= len(attacks):
            exit()
        if not stop and not is_players_turn:
            attacks[time]()
            time += 1
            stop = True

        screen.fill((0, 0, 0, 255))
        display.fill((0, 0, 0))
        mask_surface_blue.fill((0, 0, 0, 0))
        mask_surface_orange.fill((0, 0, 0, 0))
        mask_surface_normal.fill((0, 0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key in (K_z, K_RETURN):
                    if sans.show_index >= len(sans.text) and sans.show_text == True:
                        sans.show_text = False
                        stop = False
                    elif page in (CHECK_SANS, HEAL_SANS, HEAL_SANS_CANT) and shown_index >= len(battle_text):
                        is_players_turn = False
                        stop = False
                        page = MAIN_PAGE
                        player.pos = [
                            BOX_POS[0] + BOX_SIZE[0] / 2,
                            BOX_POS[1] + BOX_SIZE[1] / 2
                        ]
                        player.select_sound.play()
                    else:
                        player.choose = is_players_turn
                        if is_players_turn and page != FIGHT_SANS:
                            player.select_sound.play()
                if event.key in (K_x, K_RSHIFT):
                    sans.show_index = len(sans.text)
                    shown_index = len(battle_text)
                    player.back = True
                    player.choice = 0
                if event.key == K_UP:
                    player.going_up = True
                if event.key == K_DOWN:
                    player.going_down = True
                if event.key == K_LEFT:
                    player.going_left = True
                if event.key == K_RIGHT:
                    player.going_right = True
                if event.key == K_F4:
                    if FULL_SCREEN:
                        display = pygame.display.set_mode(SCREEN_SIZE)
                        FULL_SCREEN = 0
                    else:
                        display = pygame.display.set_mode((1920, 1080), FULLSCREEN)
                        FULL_SCREEN = 1
                if event.key == K_F2:
                    restarting = True
                        
                if DEBUG:
                    if event.key == K_n:
                        bones.clear()
                        boards.clear()
                        blasters.clear()
                        stop = False
                    if event.key == K_EQUALS:
                        frames += 1
                    if event.key == K_MINUS:
                        frames -= 1
            if event.type == KEYUP:
                if event.key == K_UP:
                    player.going_up = False
                if event.key == K_DOWN:
                    player.going_down = False
                if event.key == K_LEFT:
                    player.going_left = False
                if event.key == K_RIGHT:
                    player.going_right = False
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key in (K_z, K_RETURN):
                    player.choose = False
                if event.key in (K_x, K_RSHIFT):
                    player.back = False

        '''检测&更新'''
        
        # 战斗框
        pygame.draw.rect(screen, (255, 255, 255, 255), pygame.Rect((_boxpos[0] - 5, _boxpos[1] - 5),
                                                       (_boxsize[0] + 10, _boxsize[1] + 10)))
        pygame.draw.rect(screen, (0, 0, 0, 255), pygame.Rect(_boxpos, _boxsize)) # 内遮挡
        # 骨头
        for b in bones:
            b.show(screen,
                   mask_surface_blue,
                   mask_surface_orange,
                   mask_surface_normal)
            if b.stop:
                bones.remove(b)
        # 警告框
        for w in warns:
            w.show(screen)
            if w.stop:
                warns.remove(w)
        # 板子
        for b in boards:
            b.show(screen)
            if b.stop:
                boards.remove(b)
                
            if b.rect.colliderect(player.rect) and player.falling:
                player.pos[0] += b.speed[0]
                player.pos[1] += b.speed[1]
                if player.direction == DOWN:
                    player.pos[1] = b.rect.top - 7
                elif player.direction == UP:
                    player.pos[1] = b.rect.bottom - 1
                elif player.direction == RIGHT:
                    player.pos[0] = b.rect.left - 7
                elif player.direction == LEFT:
                    player.pos[0] = b.rect.right - 1
                player.falling = False

        """外遮挡"""
        pygame.draw.rect(screen, (0, 0, 0, 255), pygame.Rect((0, 0), (SCREEN_SIZE[0], _boxpos[1] - 5)))
        pygame.draw.rect(screen, (0, 0, 0, 255), pygame.Rect((0, _boxpos[1] - 5), (_boxpos[0] - 5, _boxsize[1] + 10)))
        pygame.draw.rect(screen, (0, 0, 0, 255), pygame.Rect((0, _boxpos[1] + _boxsize[1] + 5),
                                                       (SCREEN_SIZE[0], SCREEN_SIZE[1] - (_boxpos[1] + _boxsize[1]) - 5)))
        pygame.draw.rect(screen, (0, 0, 0, 255), pygame.Rect((_boxpos[0] + _boxsize[0] + 5, _boxpos[1] - 5),
                                                       (SCREEN_SIZE[0] - (_boxpos[0] + _boxsize[0]) - 5, _boxsize[1] + 10)))
                
        '''显示UI（外面）'''
        pygame.draw.rect(screen, (191, 0, 0, 255), pygame.Rect((275, 400), (92, 20)))
        if player.KR:
            pygame.draw.rect(screen, (255, 0, 255, 255), pygame.Rect((275 + player.HP, 400), (round(player.KR), 20)))
        pygame.draw.rect(screen, (255, 255, 0, 255), pygame.Rect((275, 400), (player.HP, 20)))
        screen.blit(
            font2.render(
                "{:0>2.0f} / 92".format(player.HP + player.KR),
                True,
                (255, 255, 255) if not round(player.KR) else (255, 0, 255)
            ),
            (
                415,
                400
            )
        )
        screen.blit(hp_image, (240, 405))
        screen.blit(kr_image, (375, 405))
        screen.blit(
            font2.render(
                "Chara    LV 19", True, (255, 255, 255)
            ), (30, 400)
        )
        
        # 显示文本
        for text in texts:
            screen.blit(
                font.render(
                    text[1], True, (255, 255, 255)
                ), text[0]
            )

        if DEBUG:
            screen.blit(
                font2.render(
                    "DEBUG", True, (0, 0, 255)
                ), (200, 0)
            )
        # 显示帧数
        screen.blit(
            font2.render(
                "FPS:{:0>3d}".format(round(1 / delta)), True, (0, 0, 255)
            ), (0, 0)
        )
        if fight:
            screen.blit(fight_highlight_image, fight_pos)
        else:
            screen.blit(fight_default_image, fight_pos)
        if act:
            screen.blit(act_highlight_image, act_pos)
        else:
            screen.blit(act_default_image, act_pos)
        if item:
            screen.blit(item_highlight_image, item_pos)
        else:
            screen.blit(item_default_image, item_pos)
        if mercy:
            screen.blit(mercy_highlight_image, mercy_pos)
        else:
            screen.blit(mercy_default_image, mercy_pos)
            
        # 鳝丝（要放在外面）
        sans.show(screen)
        if show_sans_damage:
            if sans_damage == MISS:
                screen.blit(miss_image, (250, 60))
        
        # GB炮（要放在外面）
        for t in blasters:
            t.show(screen,
                   mask_surface_blue,
                   mask_surface_orange,
                   mask_surface_normal)
            if t.stop:
                blasters.remove(t)

        # 其他东西，blahblahblah（外面）
        for t in tasks:
            t.show(screen)
            if t.stop:
                tasks.remove(t)

        if is_players_turn: # 玩家回合
            BOX_POS = [30, 250]
            BOX_SIZE = [570, 130]
            if page == MAIN_PAGE:
                if shown_index < len(battle_text):
                    shown_index += 1
                    text_sound.play()
                x = 40
                y = 250
                for char in battle_text[:shown_index]:
                    if char != '\n':
                        screen.blit(
                            battle_font.render(char, True, (255, 255, 255)),
                            (x, y)
                        )
                    x += 12
                    if x > BOX_POS[0] + BOX_SIZE[0] or char == "\n":
                        y += 16
                        x = 40
                player.type = CURSOR_SOUL
                player.options = (
                    (fight_pos[0] + 10, fight_pos[1] + 15),
                    (  act_pos[0] + 10,   act_pos[1] + 15),
                    ( item_pos[0] + 10,  item_pos[1] + 15),
                    (mercy_pos[0] + 10, mercy_pos[1] + 15)
                )

                if player.choice == 0:
                    fight = True
                    act = False
                    item = False
                    mercy = False

                if player.choice == 1:
                    fight = False
                    act = True
                    item = False
                    mercy = False

                if player.choice == 2:
                    fight = False
                    act = False
                    item = True
                    mercy = False

                if player.choice == 3:
                    fight = False
                    act = False
                    item = False
                    mercy = True

                if player.choose:
                    page = [FIGHT, ACT, 0, MERCY][player.choice]
                    player.choose = False
                    player.choice = 0
                    fight = False
                    act = False
                    item = False
                    mercy = False

            if page == ACT:
                player.options = [(40, 255)]
                screen.blit(
                    battle_font.render("* sans", True, (255, 255, 255)),
                    (40, 250)
                )
                if player.choose:
                    page = [ACT_SANS][player.choice]
                    player.choose = False
                    player.choice = 0
                if player.back:
                    page = MAIN_PAGE

            if page == ACT_SANS:
                player.options = []
                y = 250
                for _ in actions.keys():
                    if actions[_] == HEAL_SANS:
                        _ = _.format(heal_times_left)
                    screen.blit(
                        battle_font.render(_, True, (255, 255, 255)),
                        (40, y)
                    )
                    player.options.append((40, y + 5))
                    y += 20
                    
                if player.choose:
                    page = list(actions.values())[player.choice]
                    if page == HEAL_SANS:
                        if heal_times_left > 0:
                            heal(player, 92)
                            heal_times_left -= 1
                        else:
                            page = HEAL_SANS_CANT
                    player.choose = False
                    player.choice = 0
                if player.back:
                    page = ACT

            if page == CHECK_SANS:
                player.type = RED_SOUL
                player.pos = [
                    -100,
                    -100
                ]
                battle_text = "* Sans\n  The TRUE HERO.\n  ATK:1\n  DEF:1\n  Nothing to say."
                if shown_index < len(battle_text):
                    shown_index += 1
                    text_sound.play()
                x = 40
                y = 250
                for char in battle_text[:shown_index]:
                    if char != '\n':
                        screen.blit(
                            battle_font.render(char, True, (255, 255, 255)),
                            (x, y)
                        )
                    x += 12
                    if x > BOX_POS[0] + BOX_SIZE[0] or char == "\n":
                        y += 20
                        x = 40

            if page == HEAL_SANS:
                player.type = RED_SOUL
                player.pos = [
                    -100,
                    -100
                ]
                battle_text = "* You are healthy again now.\n* {} time(s) left.".format(heal_times_left)
                if shown_index < len(battle_text):
                    shown_index += 1
                    text_sound.play()
                x = 40
                y = 250
                for char in battle_text[:shown_index]:
                    if char != '\n':
                        screen.blit(
                            battle_font.render(char, True, (255, 255, 255)),
                            (x, y)
                        )
                    x += 12
                    if x > BOX_POS[0] + BOX_SIZE[0] or char == "\n":
                        y += 20
                        x = 40

            if page == HEAL_SANS_CANT:
                player.type = RED_SOUL
                player.pos = [
                    -100,
                    -100
                ]
                battle_text = "* No more times for you to heal!"
                if shown_index < len(battle_text):
                    shown_index += 1
                    text_sound.play()
                x = 40
                y = 250
                for char in battle_text[:shown_index]:
                    if char != '\n':
                        screen.blit(
                            battle_font.render(char, True, (255, 255, 255)),
                            (x, y)
                        )
                    x += 12
                    if x > BOX_POS[0] + BOX_SIZE[0] or char == "\n":
                        y += 20
                        x = 40

            if page == FIGHT:
                player.options = [(40, 255)]
                screen.blit(
                    battle_font.render("* sans", True, (255, 255, 255)),
                    (40, 250)
                )
                if player.choose:
                    page = [FIGHT_SANS][player.choice]
                    player.choose = False
                    player.choice = 0
                    choice_pos = [50, 250]
                if player.back:
                    page = MAIN_PAGE

            if page == FIGHT_SANS:
                player.type = RED_SOUL
                player.pos = [
                    -100,
                    -100
                ]
                target_img.set_alpha(target_alpha)
                if not choice_blink:
                    if target_alpha >= 255:
                        choice_going = True
                    else:
                        target_alpha += 10
                screen.blit(target_img, [BOX_POS[0] + 10, BOX_POS[1] + 5])
                screen.blit([choice_img, choice_blink_img][choice_ani_index // 5 % 2], choice_pos)
                choice_ani_index += choice_blink
                choice_pos[0] += choice_going * 8
                if choice_going and (player.choose or choice_pos[0] > BOX_POS[0] + BOX_SIZE[0]):
                    choice_going = False
                    choice_blink = True
                    tasks.append(Strike(sans.pos[:]))
                    if not before_strike:
                        sans.target_pos = [100, 80]
                    else:
                        before_strike()
                if choice_blink:
                    blink_time += 1
                    if blink_time > 60:
                        show_sans_damage = False
                        choice_going = False
                        choice_blink = False
                        choice_ani_index = 0
                        target_alpha = 0
                        blink_time = 0
                        is_players_turn = False
                        stop = False
                        page = MAIN_PAGE
                        if not after_strike:
                            sans.target_pos = [250, 80]
                        else:
                            after_strike()
                        player.pos = [
                            BOX_POS[0] + BOX_SIZE[0] / 2,
                            BOX_POS[1] + BOX_SIZE[1] / 2
                        ]
                    elif blink_time > 30:
                        target_alpha -= 10
                        show_sans_damage = True

            if page == MERCY:
                player.options = [(40, 255)]
                screen.blit(
                    battle_font.render("* sans", True, (255, 255, 255)),
                    (40, 250)
                )
                if player.choose:
                    page = [MERCY_SANS][player.choice]
                    player.choose = False
                    player.choice = 0
                if player.back:
                    page = MAIN_PAGE

            if page == MERCY_SANS:
                player.options = []
                y = 250
                for _ in mc_actions.keys():
                    screen.blit(
                        battle_font.render(_, True, (255, 255, 255)),
                        (40, y)
                    )
                    player.options.append((40, y + 5))
                    y += 20
                    
                if player.choose:
                    page = list(mc_actions.values())[player.choice]
                    player.choose = False
                    player.choice = 0
                if player.back:
                    page = MERCY

            if page == MERCY_SANS_SPARE: # 你都饶恕了，想必也不想继续玩了（）
                exit()

            if page == MERCY_SANS_FLEE: # 你都逃跑了，想必也不想继续玩了（）
                exit()

        # 你死了
        if player.HP + player.KR <= 0:
            DEAD = True
        if DEAD or restarting:
            break

        # 判定伤害
        blue_mask = pygame.mask.from_surface(mask_surface_blue)
        orange_mask = pygame.mask.from_surface(mask_surface_orange)
        normal_mask = pygame.mask.from_surface(mask_surface_normal)
        if mask_collide(blue_mask, player.mask, [0, 0], player.mask_pos):
            if any([player.going_up, player.going_down, player.going_left, player.going_right, player.falling]):
                damage(player)
        if mask_collide(orange_mask, player.mask, [0, 0], player.mask_pos):
            if not any([player.going_up, player.going_down, player.going_left, player.going_right, player.falling]):
                damage(player)
        if mask_collide(normal_mask, player.mask, [0, 0], player.mask_pos):
            damage(player)

        # 玩家
        player.show(screen, _boxpos, _boxsize)

        # 黑屏攻击
        if blackout:
            screen.fill(0x000000)

        """将screen的图像加工后放入display"""
        if not FULL_SCREEN:
            rotated_screen = pygame.transform.rotate(screen, screen_angle)
        else:
            screen_rect = screen.get_rect()
            rotated_screen = pygame.transform.rotate(
                pygame.transform.scale(
                    screen,
                    (
                        round(screen_rect.size[1] / screen_rect.size[0] * 1920),
                        1080
                    )
                ),
                screen_angle
            )
        rotated_rect = rotated_screen.get_rect()
        if not FULL_SCREEN:
            rotated_rect.center = [SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2]
        else:
            rotated_rect.center = [960,  540]
        display.blit(rotated_screen,
                     (rotated_rect.x + screen_offset[0],
                      rotated_rect.y + screen_offset[1]))
        fps.tick(frames)
        pygame.display.update()
        time2 = time_.time()
        delta = time2 - time1

    if not restarting:
        ticks = 0
        heart_offset = [0, 0]
        while True:
            '''死后的'''
            pygame.mixer.music.stop()
            ticks += 1
            screen.fill((0, 0, 0, 255))
            if ticks >= 200:
                break
            
            if ticks >= 160:
                screen.blit(alive_img, player.rect)
                if ticks == 160:
                    split_sound.play()
                    
            elif ticks >= 100:
                screen.blit(dead_img,
                            (player.rect.x + heart_offset[0],
                             player.rect.y + heart_offset[1]))
                heart_offset = [random.randint(-2, 2), random.randint(-2, 2)]
                
            elif ticks >= 60:
                screen.blit(dead_img, player.rect)
                if ticks == 60:
                    split_sound.play()
                    
            else:
                screen.blit(alive_img, player.rect)
                
            if not FULL_SCREEN:
                rotated_screen = pygame.transform.rotate(screen, screen_angle)
            else:
                screen_rect = screen.get_rect()
                rotated_screen = pygame.transform.rotate(
                    pygame.transform.scale(
                        screen,
                        (
                            round(screen_rect.size[1] / screen_rect.size[0] * 1920),
                            1080
                        )
                    ),
                    screen_angle
                )
            rotated_rect = rotated_screen.get_rect()
            if not FULL_SCREEN:
                rotated_rect.center = [SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2]
            else:
                rotated_rect.center = [960,  540]
            display.blit(rotated_screen,
                         (rotated_rect.x + screen_offset[0],
                          rotated_rect.y + screen_offset[1]))
            fps.tick(frames)
            pygame.display.update()
