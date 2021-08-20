import pygame
import os
from locals_ import *

def damage(player):
    '''伤血'''
    if not DEBUG:
        if player.HP > 1 and player.KR <= 40:
            player.HP -= 1
            player.KR += 1
        else:
            player.KR -= 1
    damage_sound.play()

def heal(player, num):
    '''加血'''
    heal_sound.play()
    for _ in range(num):
        if player.HP + player.KR < 92:
            player.HP += 1

def mask_collide(a, b, apos, bpos):
    '''mask碰撞检测'''
    offset = (int(bpos[0] - apos[0]), int(bpos[1] - apos[1]))
    if a.overlap(b, offset):
        return True
    return False
