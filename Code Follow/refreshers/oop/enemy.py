class Enemy:  #Superclass
    __type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print('I am an enemy. I am a {self.__type_of_enemy}. Be afraid of me')

    def walk_forward(self):
        print('Walking forward to you')

    def attack(self):
        print(f'Attacking and inflicting {self.attack_damage} damage')

    def get_type_of_enemy(self):
        return self.__type_of_enemy
