from enemy import *
import random


class Ogre(Enemy):  #Subclass

    def __init__(self, health_points, attack_damage):
        super().__init__("Ogre",
                         health_points=health_points,
                         attack_damage=attack_damage)

    def talk(self):
        print('G')

    def special_attack(self):
        did_special_attack = random.random() < 0.2

        if did_special_attack:
            self.attack_damage += 4
            print('Special attack: Attack damage increased by 4')
