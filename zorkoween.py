#do stuff

class Monster(observable):

    
class House(Observer):
    def update(self):
        print Observer + " added"

class Person(Monster):

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

    def getMonsters(self):
        return self.observers

