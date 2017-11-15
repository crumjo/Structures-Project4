#! /usr/bin/env python3
from abc import ABCMeta, abstractmethod
import random


class Monster(Observable):
    #this random should be used in the house
    random = random.randint(0,5)
    if(random == 0):
        #add vampire
    if(random == 1):
        #add ghoul
    if(random == 2):
        #add zombie
    if(random == 3):
        #add Lich
    if(random == 4):
        #add ghost
    if(random == 5):
        #add human
        
    def getHealth(self):
        return health
    
    def getName(self):
        return name
    
    def getAttack(self):
        return attack
    
    def updateHealth(self,int):
        health = health - int

class Vampire(Monster):
    name = "Vampire"
    health = random.randint(100,200)
    attack = random.randint(10,20)

class Ghoul(Monster):
    name = "Ghoul"
    health = random.randint(40,80)
    attack = random.randint(15,30)

class Zombie(Monster):
    name = "Zombie"
    health = random.randint(50,100)
    attack = random.randint(0,10)

class Werewolves(Monster):
    name = "Werewolves"
    health = 200
    attack = random.randint(0,40)

class Person(Monster):
    name = "Person"
    health = 100
    attack = -1

class House(Observer):
    def update(self):
        print Observer + " added"


class Observable(object):

    def __init__(self):
        self.observers = [];

    def add_observer(self, observer):
        if not observer in self.observers:
            self.observers.append(observer);

    def remove_observe(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def remove_all_observers(self):
        self.observers = []

    def get_monsters(self):
        return self.observers


class Observer(object):

    __metaclass__ = abd
    @abstractmethod
    def update(self, *args, **kwargs):
        pass

class player(object):
    
    health = random.randint(100,125)
    attack = random.randint(10,20)
    inventory = []
    for i in 10:
        temp = random.randint(1,4)
        if(temp == 1):
            
            #add hersheykisses
        if(temp == 2):
            #add sourStraws
        if(temp == 3):
            #add choclatebars
        if(temp == 4):
            #add nerdbombs
            
    def updateHealth(self, int):
        health = health - int

    def getHealth(self):
        return health

    def getAttack(self):
        return attack

class weapon(object):
    def getName(self):
        return name
    def getAttack(self):
        return attack
    def getUses(self):
        return uses
    def use(self):
        uses = uses - 1

class HersheyKisses(weapon):
    name = "Hershey Kisse"
    attack = 1
    uses = 2^16
    
class SourStraws(weapon):
    name = "Sour Straw"
    attack = random.uniform(1, 1.75)
    uses = 2

class ChocolateBars:
    name = "Chocolate bar"
    attack = random.uniform(2, 2.4)
    uses = 4

class NerdBombs:
    name =  "Nerd bomb"
    attack = random.uniform(3.5, 5)
    uses = 1
