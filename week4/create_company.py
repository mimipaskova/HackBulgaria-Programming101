import sqlite3
from os.path import basename

def create_table(cursor):
    cursor.execute('''CREATE TABLE company
        (my_id INTEGER PRIMER KEY, name text, monthly_salary int, yearly_bonus int, position text)''')

def insert(item, cursor):
    my_id = item["my_id"]
    name = item["name"]
    monthly_salary = item["monthly_salary"]
    yearly_bonus = item["yearly_bonus"]
    position = item["position"]

    query_lang = "INSERT INTO company VALUES(?, ?, ?, ?, ?)"
    cursor.execute(query_lang,(my_id, name, monthly_salary, yearly_bonus, position))


data = [{
    'my_id': 1,
    'name' : 'Ivan Ivanov',
    'monthly_salary':5000,
    'yearly_bonus': '10000',
    'position' : 'Software Developer'
},{
    'my_id': 2,
    'name' : 'Rado Rado',
    'monthly_salary':500,
    'yearly_bonus': '0',
    'position' : 'Technical Support Intern'
},{
    'my_id': 3,
    'name' : 'Ivo Ivo',
    'monthly_salary':10000,
    'yearly_bonus': '100000',
    'position' : 'CEO'
},{
    'my_id': 4,
    'name' : 'Petar Petrov',
    'monthly_salary':3000,
    'yearly_bonus': '1000',
    'position' : 'Marketing Manager'
},{
    'my_id': 5,
    'name' : 'Maria Georgieva',
    'monthly_salary':8000,
    'yearly_bonus': '10000',
    'position' : 'COO'
}]

connectoin=sqlite3.connect("create_bank.db")
c=connectoin.cursor()

create_table(c)

for item in data:
    insert(item, c)

connectoin.commit()
connectoin.close()
