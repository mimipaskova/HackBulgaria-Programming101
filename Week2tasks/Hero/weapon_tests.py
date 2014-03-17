import weapon
import unittest

class weapon_test(unittest.TestCase):
    """docstring for hero_test"""

    def setUp(self):
        self.new_weapon=weapon.weapon("mimi",100, 0.5)


if __name__ == '__main__':
    unittest.main()
