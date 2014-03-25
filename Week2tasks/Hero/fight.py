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
            rand= self.hero
        else:
            rand = self.orc
        return rand


    def simulate_fight(self):
        while(self.hero.get_health() >0 and self.orc.get_health()>0):
            self.rand.



