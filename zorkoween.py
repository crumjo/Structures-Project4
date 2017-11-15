#! /usr/bin/env python3
from observe import Observable
from observe import Observer
import random


class Monster(Observable):

    name = ""
    health = -1
    attack = -1

    if name == "Vampire":
        health = random.randint(100, 200)
        attack = random.randint(10, 20)

    elif name == "Ghoul":
        health = random.randint(40, 80)
        attack = random.randint(15, 30)

    elif name == "Zombie":
        health = random.randint(50, 100)
        attack = random.randint(0, 10)

    elif name == "Werewolf":
        health = 200
        attack = random.randint(0, 40)

    elif name == "Person":
        health = 100
        attack = -1
        
    def get_health(self):
        return self.health
    
    def get_name(self):
        return self.name
    
    def get_attack(self):
        return self.attack
    
    def update_health(self, dmg):
        self.health = self.health - dmg


class Vampire(Monster):
    name = "Vampire"
    health = random.randint(100, 200)
    attack = random.randint(10, 20)


class Ghoul(Monster):
    name = "Ghoul"
    health = random.randint(40, 80)
    attack = random.randint(15, 30)


class Zombie(Monster):
    name = "Zombie"
    health = random.randint(50, 100)
    attack = random.randint(0, 10)


class Werewolf(Monster):
    name = "Werewolf"
    health = 200
    attack = random.randint(0, 40)


class Person(Monster):
    name = "Person"
    health = 100
    attack = -1


class House(Observer):
    def update(self):
        print "Monster Updated."


class Player(object):
    
    health = random.randint(100, 125)
    attack = random.randint(10, 20)
    inventory = []
    for i in range(0, 9):
        temp = random.randint(1, 4)
        if temp == 1:
            print("Hershey Kisses")
        if temp == 2:
            print ("Sour Straws")
        if temp == 3:
            print ("Chocolate Bars")
        if temp == 4:
            print ("Nerd Bombs")
            
    def update_p_health(self, dmg):
        self.health = self.health - dmg

    def get_p_health(self):
        return self.health

    def get_p_attack(self):
        return self.attack


class Weapon(object):

    name = ""
    attack = 0.0
    uses = 0

    def get_name(self):
        return self.name

    def get_attack(self):
        return self.attack

    def get_uses(self):
        return self.uses

    def update_use(self):
        self.uses = self.uses - 1


class HersheyKisses(Weapon):
    name = "Hershey Kisses"
    attack = 1
    uses = 1


class SourStraws(Weapon):
    name = "Sour Straw"
    attack = random.uniform(1, 1.75)
    uses = 2


class ChocolateBars(Weapon):
    name = "Chocolate Bar"
    attack = random.uniform(2, 2.4)
    uses = 4


class NerdBombs(Weapon):
    name = "Nerd bomb"
    attack = random.uniform(3.5, 5)
    uses = 1


if __name__ == '__main__':
    house = House()
    random = random.randint(0, 4)

    if random == 0:
        print("Vampire")
        vampire = Monster()

    if random == 1:
        print("Ghoul")
        ghoul = Monster()

    if random == 2:
        print ("Zombie")
        zombie = Monster()

    if random == 3:
        print ("Werewolf")
        werewolf = Monster()

    if random == 4:
        print ("Person")
        person = Monster()