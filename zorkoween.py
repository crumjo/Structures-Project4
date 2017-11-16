#! /usr/bin/env python3

#READ ME!!!
#okay so I updated alot, I updated all monster and weapons class with a
#constructer to make the right type of monster or weapon. I made a
#constructer for player. I made the neigherhood and I dont think its a
#2d array but it should work. I made a game method to be called at start
#that will intaite player and neigherhood and fill it with houses and houses
#with monsters. I want to clean this up though would it be possible to make files
#for monsters and weapons seperatly? We still need to read from command line or
#gui to make it so the player moves from house to house and attacks. And we
#need to make sure edge cases our covered. Also im sorry if the if statements arent
#right. I left comments where stuff is kinda funky and I know that updating the
#monster isnt right. Maybe we should do a turn command? We also need a method for
#monsters to attack.

from observe import Observable
from observe import Observer
import random


class Monster(Observable):

    name = ""
    health = -1
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
    def Vampire(self):
        name = "Vampire"
        health = random.randint(100, 200)
        attack = random.randint(10, 20)


class Ghoul(Monster):
    def Ghoul(self):
        name = "Ghoul"
        health = random.randint(40, 80)
        attack = random.randint(15, 30)


class Zombie(Monster):
    def Zombie(self):
        name = "Zombie"
        health = random.randint(50, 100)
        attack = random.randint(0, 10)


class Werewolf(Monster):
    def Werewolf(self):
        name = "Werewolf"
        health = 200
        attack = random.randint(0, 40)


class Person(Monster):
    def Person(self):
        name = "Person"
        health = 100
        attack = -1


class House(Observer):
    def update(self):
        print "Monster Updated."


class neighborhood(object):
    def __init__(self,number):
        self.neighborhood = [number][number]


    def place_house(self,x,y,house)
        self.neighborhood[x][y] = house


    def get_house(self,x,y)
        return self.neighborhood[x][y]

    
class Player(object):

    def player():
        health = random.randint(100, 125)
        attack = random.randint(10, 20)
        inventory = []
        for i in range(0, 9):
            temp = random.randint(1, 4)
            if temp == 1:
                print("Hershey Kisses")
                item = new kisses()
                inventory.add(item)
            if temp == 2:
                print ("Sour Straws")
                item = new sour_straws()
                inventory.add(item)
            if temp == 3:
                print ("Chocolate Bars")
                item = new choc_bar()
                inventory.add(item)
            if temp == 4:
                print ("Nerd Bombs")
                item = new nerd_bomb()
                inventory.add(item)

                
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
    def kisses(self):
        name = "Hershey Kisses"
        attack = 1
        uses = 1


class SourStraws(Weapon):
    def sour_straws(self):
        name = "Sour Straw"
        attack = random.uniform(1, 1.75)
        uses = 2


class ChocolateBars(Weapon):
    def choc_bar(self):
        name = "Chocolate Bar"
        attack = random.uniform(2, 2.4)
        uses = 4


class NerdBombs(Weapon):
    def nerd_bomb(self):
        name = "Nerd bomb"
        attack = random.uniform(3.5, 5)
        uses = 1

class game():
    def main(self, argsv):
        
        #argsv = zorkoween.py main int
        #split args v
        edge = argsv[2]
        #builds neighborhood
        #should this be its own helper method??
        neighborhood caldesac = new neighborhood(edge)
        #builds houses in neighborhood
        for r in range(0,edge - 1):
            for c in range(0,edge - 1):
                house = House()
                temp = random.randint(0,9)
                for x in range(0, temp):
                    random = random.randint(0, 4)

                    if random == 0:
                        print("Vampire")
                        monseter = Vampire()
                        house().add_observer(monster)

                    if random == 1:
                        print("Ghoul")
                        monster = Ghoul()
                        house().add_observer(monster)

                    if random == 2:
                        print ("Zombie")
                        monster = Zombie()
                        house().add_observer(monster)

                    if random == 3:
                        print ("Werewolf")
                        monster = Werewolf()
                        house().add_observer(monster)

                    if random == 4:
                        print ("Person")
                        monster = Person()
                        house().add_observer(monster)

                caldesac.placehouse(r,c)
        
        #intiates player
        you = new player()
        
        #this is where you are at! postion x,y in the neigborhood
        x_position = 0;
        y_position = 0;
        
        #c_house is the current house you are in
        c_house = caldesac.get_house(x_position, y_position)


    #I think this is right 
    def movement(self, direction):
        #if to check if move is valid
        #then moves 
        if direction == "east":
            #this is gonna move you east if able
            if x_direction is not 0:
                print ("You are in a new house to the left!")
                x_direction = x_direction - 1
                c_house = caldasac.get_house(x_position, y_position)

        if direction == "north":
            #this is gonna move you west if able
            if x_direction is not 0:
                print ("You are in a new house to the north!")
                y_direction = y_direction - 1
                c_house = caldasac.get_house(x_position, y_position)

        if direction == "west":
            #this is gonna move you west if able
            if x_direction is not edge:
                print ("You are in a new house to the west!")
                x_direction = x_direction + 1
                c_house = caldasac.get_house(x_position, y_position)
                
        if direction == "south":
            #this is gonna move you west if able
            if x_direction is not edge:
                print ("You are in a new house to the south!")
                y_direction = y_direction + 1
                c_house = caldasac.get_house(x_position, y_position)
        
    #you attack entire house, pass in house at caldasac[x][y]
    #passes in weapon to see if monster is affected and figure out dmg
    #needs case checking if the item is in your inventory
    #if muiltiple instance of a weapon is in inventory need to make sure
    #only that one is updated :/
    def attack(self, house, weapon):
        damage = player.get_p_attack() * weapon.get_attack()
        residents = house.get_monsters()
        for x in residents:
            if weapon.get_name == "Nerd bomb":
                weapon.update_use()
                if x.get_name == "Ghoul":
                    x.update_health(attack*5)
                    #this should be position in array and monster in that spot
                    house.update_monster(x, x)
                else:
                    x.update_health(attack)
                    #this should be position in array and monster in that spot
                    house.update_monster(x, x)
                    
            if weapon.get_name == "Chocolate Bar":
                weapon.update_use()
                if x.get_name == "Vampire" || "Werewolf":
                    x.update_health(0)
                    #this should be position in array and monster in that spot
                    house.update_monster(x, x)
                else:
                    x.update_health(attack)
                    #this should be position in array and monster in that spot
                    house.update_monster(x, x)
                    
            if weapon.get_name == "Sour Straw":
                weapon.update_use()
                if x.get_name == "Werewolf":
                    x.update_health(0)
                    #this should be position in array and monster in that spot
                    house.update_monster(x, x)
                elif x.get_name == "Zombie":
                    x.update_health(attack*2)
                    #this should be position in array and monster in that spot
                    house.update_monster(x, x)
                else:
                    x.update_health(attack)
                    #this should be position in array and monster in that spot
                    house.update_monster(x, x)

            if weapon.get_name == "Hershey Kisses":
                    x.update_health(attack)
                    #this should be position in array and monster in that spot
                    house.update_monster(x, x)


if __name__ == '__main__':
    neighborhood caldesac = new neighborhood(3,3)
    
    for i in range(0,2):
        house = House()
        temp = random.randint(0,9)
        for j in range(0, temp):
            random = random.randint(0, 4)

            if random == 0:
                print("Vampire")
                vampire = Monster()
                house().add_observer(vampire)

            if random == 1:
                print("Ghoul")
                ghoul = Monster()
                house().add_observer(ghoul)

            if random == 2:
                print ("Zombie")
                zombie = Monster()
                house().add_observer(zombie)

            if random == 3:
                print ("Werewolf")
                werewolf = Monster()
                house().add_observer(werewolf)

            if random == 4:
                print ("Person")
                person = Monster()
                house().add_observer(person)
