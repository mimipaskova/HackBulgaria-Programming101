import create_company
import unittest
import sqlite3
from subprocess import call

class create_company_test(unittest.TestCase):
    """docstring for manage_company"""

    def setUp(self):
        #self.new_db=manage_company.hero("mimi",100, 'mimito')
        self.connectoin=sqlite3.connect("test_database.db")
        self.cursor=self.connectoin.cursor()
        create_company.create_table(self.cursor)

    def test_create_table(self):

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
        self.connectoin.commit()


    def tearDown(self):
        self.connectoin.close()
        call("rm -r test_database.db", shell=True)

if __name__ == '__main__':
    unittest.main()
