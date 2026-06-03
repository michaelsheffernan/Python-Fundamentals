import random


class Enemy:

    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.type_of_enemy

    def talk(self):
        print("I am an enemy")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closer to you.")

    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage}.")

    def special_attack(self):
        print("Enemy has no special attacks")


class Zombie(Enemy):

    def __init__(self, health_points, attack_damage):

        super().__init__(type_of_enemy="Zombie",
                         health_points=health_points,
                         attack_damage=attack_damage)

    def talk(self):
        print("*Grumbling...*")

    def spread_disease(self):
        print("The zombie is trying to spread infection")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.5
        if did_special_attack_work:
            self.health_points += 2
            print("Zombie gained 2HP!")


class Ogre(Enemy):

    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Ogre",
                         health_points=health_points,
                         attack_damage=attack_damage)

    def talk(self):
        print("Ogre is salmming hands all around.")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.2
        if did_special_attack_work:
            self.attack_damage += 4
            print("Ogre Gained 4 attack damage!")
