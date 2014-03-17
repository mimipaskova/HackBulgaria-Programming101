from entity import Entity

class orc(Entity):
    def __init__(self, name, health,berserk_factor):
        super().__init__(name, health)
        self.berserk_factor=berserk_factor# to do - normalize (if bigger than 2, make 2, else make 1)
        self.max_health=health

    def attack(self):
        if not self.has_weapon():
            return 0
        else:
            return self.weapon.damage*self.berserk_factor
