import create_company
import unittest
import sqlite3

class create_company_test(unittest.TestCase):
    """docstring for manage_company"""

    def setUp(self):
        #self.new_db=manage_company.hero("mimi",100, 'mimito')
        self.connectoin=sqlite3.connect("test_database.db")
        self.cursor=self.connectoin.cursor()

    def test_create_table(self):
        create_company.create_table(self.cursor)
        #"SELECT * FROM employees"
        lang = self.cursor.execute("SELECT * FROM company").fetchall()
        self.assertEqual(0,len(lang))


    def test_insert(self):
        ins={
    'my_id': 1,
    'name' : 'Ivan Ivanov',
    'monthly_salary':5000,
    'yearly_bonus': '10000',
    'position' : 'Software Developer'
    }

        create_company.insert(ins, self.cursor)
        lines = self.cursor.execute("SELECT * FROM company").fetchall()
        #print(lines)
        self.assertEqual(1,len(lines))
        self.assertEqual([(1, 'Ivan Ivanov', 5000, 10000, 'Software Developer')], lines)



if __name__ == '__main__':
    unittest.main()
