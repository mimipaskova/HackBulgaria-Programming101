import string_utils
import unittest

class string_utils_test(unittest.TestCase):
	"""docstring for string_utils_test"""
	def test_lines1(self):
		self.assertEqual(['Hack', 'bulgaria', 'programming', "101"],string_utils.lines("Hack bulgaria programming 101"))		

	def test_lines2(self):
		self.assertEqual(['Hack', 'bulgaria', 'programming', "101", "blq"],string_utils.lines("Hack bulgaria programming 101 blq "))	

	def test_unlines1(self):
		self.assertEqual("Hack bulgaria programming 101 blq", string_utils.unlines(['Hack ', 'bulgaria ', 'programming ', "101 ", "blq"]))

	def test_unlines2(self):
		self.assertEqual("qwerty", string_utils.unlines(['qw', 'er', 'ty']))

	def test_tabs_to_spaces(self):
		self.assertEqual("blq    lqlq    fefe    ty", string_utils.tabs_to_spaces('blq	lqlq	fefe	ty'))


if __name__ == '__main__':
	unittest.main()