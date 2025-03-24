from enemy import Enemy 

class Zombie(Enemy): #Subclass
  def __init__(self, health_points, attach_damage):
    super().__init__("Zombie", health_points=health_points, attach_damage=attach_damage)

def talk(self):
  print('Grumbling')

def spread_disease(self):
  print('Spreading disease')