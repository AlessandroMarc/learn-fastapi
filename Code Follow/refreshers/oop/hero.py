from weapon import *


class Hero:  #Superclass

    def __init__(self, health_points, attack_damage):
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.is_weapon_equipped = False
        self.weapon = None

    def equip_weapon(self):
        if self.weapon is not None:
            self.is_weapon_equipped = True
            self.attack_damage += self.weapon.attack_increase

    def attack(self):
        print(f'Attacking and inflicting {self.attack_damage} damage')
