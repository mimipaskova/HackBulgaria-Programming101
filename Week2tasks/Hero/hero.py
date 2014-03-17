from entity import Entity

class hero(Entity):
    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.nickname=nickname
        self.max_health=health

    def known_as(self):
        return self.name + " the " + self.nickname
