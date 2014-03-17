class Entity():
    def __init__(self, name, health):
        self.name=name
        self.health=health
        self.max_health=health

    def is_alive(self):
        if self.health>0:
            return True
        return False

    def get_health(self):
        return self.health

    def take_damage(self,damage_points):
        if self.health<=damage_points:
            self.health=0
        else:
            self.health=self.health - damage_points
        return self.health

    def take_healing(self, healing_points):
        if self.health+healing_points>self.max_health:
            self.health=self.max_health
            return True
        elif self.health == 0:
            return False
        else:
            self.health=self.health + healing_points
            return True

    def has_weapon(self):
        if "weapon" in self.__dict__:
            return True
        return False

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if not self.has_weapon():
            return 0
        else:
            return self.weapon.damage

    #def equip_weapon(self, weapon):








