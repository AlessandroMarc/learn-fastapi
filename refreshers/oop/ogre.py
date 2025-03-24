from enemy import *

class Orgre(Enemy): #Subclass
  def __init__(self, health_points, attach_damage):
   super().__init__("Ogre", health_points=health_points, attach_damage=attach_damage)

  def talk(self):
   print('G')