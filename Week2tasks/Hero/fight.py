from random import randint
from hero import hero
from orc import orc


class Fight():
    def __init__(self, hero, orc):
        self.hero=hero
        self.orc=orc

    def rand_entity(self):
        r=randint(0,100)
        if r>50:
            return hero
        return orc


    def simulate_fight():
        if rand_entity() == hero:
            coin=0
        else:
            coin=1




