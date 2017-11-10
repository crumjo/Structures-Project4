#! /usr/bin/env python3
from abc import ABCMeta, abstractmethod

class Monster(Observable):
    health = 1;
    attack = 0;

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