from entity import Entity
from hero import hero
from orc import orc
from weapon import Weapon

def main():
    w = Weapon("Axe", 25, 1)
    o = orc("Orkat", 50, 1.2);
    h = hero("Mimi", 100, "The Slayer")
    h.equip_weapon(w)
    print(o.health)
    o.take_damage(h.attack())
    print(o.health)


if __name__ == '__main__':
    main()
