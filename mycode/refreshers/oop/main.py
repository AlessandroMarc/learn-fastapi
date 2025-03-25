from hero import *
from enemy import *
from zombie import Zombie
from ogre import Ogre


def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print('------------------')
        e1.special_attack()
        e2.special_attack()
        print(f'{e1.get_type_of_enemy()} health points: {e1.health_points}')
        print(f'{e2.get_type_of_enemy()} health points: {e2.health_points}')
        e1.attack()
        e2.attack()
        e1.health_points -= e2.attack_damage
        e2.health_points -= e1.attack_damage

    print('------------------')

    if e1.health_points <= 0:
        print(f'{e2.get_type_of_enemy()} wins')
    else:
        print(f'{e1.get_type_of_enemy()} wins')


def hero_battle(hero: Hero, enemy: Enemy):

    while hero.health_points > 0 and enemy.health_points > 0:
        print('------------------')
        enemy.special_attack()
        print(f'hero health points: {hero.health_points}')
        print(
            f'{enemy.get_type_of_enemy()} health points: {enemy.health_points}'
        )
        hero.attack()
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        enemy.health_points -= hero.attack_damage

    print('------------------')

    if hero.health_points <= 0:
        print(f'{enemy.get_type_of_enemy()} wins')
    else:
        print(f'hero wins')


zombie = Zombie(10, 1)
ogre = Ogre(20, 3)
hero = Hero(10, 1)
weapon = Weapon('Sword', 10)
hero.weapon = weapon
hero.equip_weapon()

hero_battle(hero, ogre)
