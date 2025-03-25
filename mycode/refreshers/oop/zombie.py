from enemy import Enemy
import random


class Zombie(Enemy):  #Subclass

    def __init__(self, health_points, attack_damage):
        super().__init__("Zombie",
                         health_points=health_points,
                         attack_damage=attack_damage)

    def talk(self):
        print('Grumbling')

    def spread_disease(self):
        print('Spreading disease')

    def special_attack(self):
        did_special_attack = random.choice([True, False])

        if did_special_attack:
            self.health_points += 2
            print('Special attack: Health points increased by 2')
