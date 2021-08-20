import pygame
pygame.init()

'''常量（这么多的flag可惜不能用enum）'''
SANS_NORMAL      = 0
SANS_CLOSED_EYES = 1
SANS_NO_EYES     = 2
SANS_LOOK_LEFT   = 3
SANS_WINK        = 4
SANS_BLUE_EYES   = 5

SCREEN_SIZE = [640, 480]

BOX_POS = [0, 0]
BOX_SIZE = [0, 0]

RED_SOUL    = 1
BLUE_SOUL   = 2
CURSOR_SOUL = 3

UP    = 0
DOWN  = 1
LEFT  = 2
RIGHT = 3

WHITE  = 0
BLUE   = 1
ORANGE = 2

MAIN_PAGE        = 0
FIGHT            = 1
FIGHT_SANS       = 2
ACT              = 3
ACT_SANS         = 4
CHECK_SANS       = 5
HEAL_SANS        = 6
HEAL_SANS_CANT   = 7
MERCY            = 8
MERCY_SANS       = 9
MERCY_SANS_SPARE = 10
MERCY_SANS_FLEE  = 11

MISS = -1

DEBUG = 0
DEAD = 0
FULL_SCREEN = 0

damage_sound = pygame.mixer.Sound("res/PlayerDamaged.ogg") # 受伤声
heal_sound = pygame.mixer.Sound("res/PlayerHeal.ogg")      # 治疗声
pygame.mixer.music.load("res/mus_zz_megalovania.ogg")      # BGM
text_sound = pygame.mixer.Sound("res/BattleText.ogg")      # 旁白声
flash_sound = pygame.mixer.Sound("res/Flash.ogg")          # 旁白声

target_img = pygame.image.load("res/Target/Default/000.png")             # 战斗界面
choice_img = pygame.image.load("res/TargetChoice/Default/000.png")       # 战斗光标
choice_blink_img = pygame.image.load("res/TargetChoice/Default/001.png") # 闪烁光标

hp_image = pygame.image.load("res/HP/Default/000.png")
kr_image = pygame.image.load("res/KR/Default/000.png")

alive_img = pygame.image.load("res/PlayerHeart/Default/000.png")
dead_img = pygame.image.load("res/PlayerHeart/Split/000.png")

fight_default_image = pygame.image.load("res/UIFight/Default/000.png")
fight_highlight_image = pygame.image.load("res/UIFight/HighLight/000.png")

act_default_image = pygame.image.load("res/UIAct/Default/000.png")
act_highlight_image = pygame.image.load("res/UIAct/HighLight/000.png")

item_default_image = pygame.image.load("res/UIItem/Default/000.png")
item_highlight_image = pygame.image.load("res/UIItem/HighLight/000.png")

mercy_default_image = pygame.image.load("res/UIMercy/Default/000.png")
mercy_highlight_image = pygame.image.load("res/UIMercy/HighLight/000.png")

miss_image = pygame.image.load("res/Damage/Miss/000.png")

slam_sound = pygame.mixer.Sound("res/Slam.ogg")
split_sound = pygame.mixer.Sound("res/HeartSplit.ogg")

fight_pos = (25, 430)
act_pos = (185, 430)
item_pos = (345, 430)
mercy_pos = (505, 430)

spinning_left = False
spinning_right = False

fight = False
act = False
item = False
mercy = False

stop = False
restarting = False

is_players_turn = False
page = 0

battle_font = pygame.font.Font("res/battle.ttf", 24)
battle_text = ""
font        = pygame.font.Font("res/sans.ttf", 24)
font2       = pygame.font.Font("res/default.ttf", 24)

shown_index = 0

choice_pos = [50, 246]
choice_going = False
choice_ani_index = 0
choice_blink = False
target_alpha = 0
blink_time = 0

sans_damage = -1
show_sans_damage = False

heal_times_left = 5

blackout = False

screen_angle = 0

screen_shaking = False
screen_offset = [0, 0]

attacks = []

