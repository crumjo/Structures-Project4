from abc import ABCMeta, abstractmethod


class Observable(object):

    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def remove_observe(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def remove_all_observers(self):
        self.observers = []

    def get_monsters(self):
        return self.observers

    #this is new! its updates the monster at location(ideally)
    def update_monster(self,locatoin, observer):
        self.observers[location] == observer

class Observer(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, *args, **kwargs):
        pass
