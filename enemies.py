class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        self.name = "Giant Spider"
        self.hp = 10
        self.damage = 2
        
class Zombie(Enemy):
    def __init__(self):
        self.name = "Zombie"
        self.hp = 25
        self.damage = 10


class Ogre(Enemy):
    def __init__(self):
        self.name = "Ogre"
        self.hp = 30
        self.damage = 10


class BatColony(Enemy):
    def __init__(self):
        self.name = "Colony of bats"
        self.hp = 100
        self.damage = 4


class RockMonster(Enemy):
    def __init__(self):
        self.name = "Rock Monster"
        self.hp = 80
        self.damage = 15

def modify_player(self, player):
    if self.enemy.is_alive():
        player.hp = player.hp - self.enemy.damage
        print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))

