class Enemy: #Superclass
  __type_of_enemy : str
  health_points : int = 10
  attach_damage : int = 1

  def __init__(self, type_of_enemy, health_points=10, attach_damage=1):
    self.__type_of_enemy = type_of_enemy
    self.health_points = health_points
    self.attach_damage = attach_damage

  def talk(self):
    print('I am an enemy. I am a {self.__type_of_enemy}. Be afraid of me')

  def walk_forward(self):
    print('Walking forward to you')

  def attack(self):
    print(f'Attacking and inflicting {self.attach_damage} damage')

  def get_type_of_enemy(self):
    return self.__type_of_enemy