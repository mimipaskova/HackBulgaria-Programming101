import orc
import unittest

class orc_test(unittest.TestCase):

    def setUp(self):
        self.new_orc=orc.orc("mimi",100, 1.5)


    def test_is_alive(self):
        self.assertEqual(True,self.new_orc.is_alive())

    def test_is_alive_two(self):
        self.new_orc.health=0
        self.assertEqual(False,self.new_orc.is_alive())

    def test_get_health(self):
        self.assertEqual(100,self.new_orc.get_health())

    def test_get_health_two(self):
        self.new_orc.health=10
        self.assertEqual(10,self.new_orc.get_health())

    def test_take_damage(self):
        self.new_orc.health=10
        self.assertEqual(4,self.new_orc.take_damage(6))

    def test_take_damage_two(self):
        self.new_orc.health=10
        self.assertEqual(0,self.new_orc.take_damage(14))

    def test_take_healing(self):
        self.new_orc.health=50
        self.assertEqual(True,self.new_orc.take_healing(20))

    def test_take_healing_two(self):
        self.new_orc.health=50
        self.assertEqual(True,self.new_orc.take_healing(60))

    def test_take_healing_three(self):
        self.new_orc.health=0
        self.assertEqual(False,self.new_orc.take_healing(60))



if __name__ == '__main__':
    unittest.main()
