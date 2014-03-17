import hero
import unittest

class hero_test(unittest.TestCase):
    """docstring for hero_test"""

    def setUp(self):
        self.new_person=hero.hero("mimi",100, 'mimito')

    def test_known_as(self):
        self.assertEqual("mimi the mimito",self.new_person.known_as())


    def test_is_alive(self):
        self.assertEqual(True,self.new_person.is_alive())

    def test_is_alive_two(self):
        self.new_person.health=0
        self.assertEqual(False,self.new_person.is_alive())

    def test_get_health(self):
        self.assertEqual(100,self.new_person.get_health())

    def test_get_health_two(self):
        self.new_person.health=10
        self.assertEqual(10,self.new_person.get_health())

    def test_take_damage(self):
        self.new_person.health=10
        self.assertEqual(4,self.new_person.take_damage(6))

    def test_take_damage_two(self):
        self.new_person.health=10
        self.assertEqual(0,self.new_person.take_damage(14))

    def test_take_healing(self):
        self.new_person.health=50
        self.assertEqual(True,self.new_person.take_healing(20))

    def test_take_healing_two(self):
        self.new_person.health=50
        self.assertEqual(True,self.new_person.take_healing(60))

    def test_take_healing_three(self):
        self.new_person.health=0
        self.assertEqual(False,self.new_person.take_healing(60))



if __name__ == '__main__':
    unittest.main()
