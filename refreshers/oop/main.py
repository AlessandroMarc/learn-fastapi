from enemy import *

enemy = Enemy("Zombie", 20, 2)
enemy.get_type_of_enemy()
enemy.talk() # It's an abstraction because it is hidden how the talk method is implemented

def battle(e : Enemy):
    e.talk() 
    e.attack()