import sqlite3
#import create_company

global c

def create_connect():
    global c
    conn = sqlite3.connect("create_bank.db")
    c = conn.cursor()


def list_employees(c):
    my_list = "SELECT name, position FROM company"
    print(c.execute(my_list).fetchall())

def monthly_spending(c):
    my_sum=0
    sum_salary= c.execute("SELECT monthly_salary FROM company").fetchall()
    for salary in sum_salary:
        my_sum = my_sum + salary[0]
    print(my_sum)

def yearly_spending(c):
    my_sum=0
    sum_salary= c.execute("SELECT monthly_salary, yearly_bonus FROM company").fetchall()
    for salary in sum_salary:
        my_sum = my_sum + salary[0] + salary[1]
    print(my_sum)

def insert(item, cursor):
    my_id = item["my_id"]
    name = item["name"]
    monthly_salary = item["monthly_salary"]
    yearly_bonus = item["yearly_bonus"]
    position = item["position"]

    query_lang = "INSERT INTO company VALUES(?, ?, ?, ?, ?)"
    cursor.execute(query_lang,(my_id, name, monthly_salary, yearly_bonus, position))
    conn.commit()

def add_employee(item,c):
    insert(item,c)
    #item={dictionary}

def delete_employee (id,c):
    remove_name=c.execute("SELECT name FROM company WHERE my_id = id")
    c.execute("DELETE FROM company WHERE my_id = id;")
    return remove_name

def update_employee(id,c):
    name = input("new name: ")
    monthly_salary = input("new monthly salary: ")
    yearly_bonus = input("new yearly bonus: ")
    position = input("new position: ")
    c.execute(("UPDATE company SET name=?, monthly_salary=?, yearly_bonus=?, position=? WHERE my_id = id"),(name, monthly_salary, yearly_bonus,\
        position))

def help():
    print("list_employees - Prints out all employees, in the following format - \"name - position\" \nmonthly_spending - Prints out the total sum for monthly spending that the company is doing for salaries \nyearly_spending - Prints out the total sum for one year of operation (Again, salaries) \nadd_employee, the program starts to promt for data, to create a new employee. \ndelete_employee <employee_id>, the program should delete the given employee from the database \nupdate_employee <employee_id>, the program should prompt the user to change each of the fields for the given" )


def command_split(command):
    return command.split(" ")


def main():
    while True:
        create_connect()
        command = command_split(input("command>"))

        if command[0] == "list_employees":
            list_employees(c)
            print(command)
        elif command[0] == "monthly_spending":
            monthly_spending(c)
            print(command)
            #break

        elif command[0] == "yearly_spending":
            yearly_spending(c)
            print(command)
            #break
        elif command[0] == "add_employee":
            item={'my_id' : input("my_id: "),'name' : input("name: "), 'monthly_salary' : input("monthly salary: "), 'yearly_bonus' : input("new yearly bonus: "),'position' : input("new position: ")}
            insert(item, c)
            print(command)
            #break

        elif command[0] == "delete_employee <employee_id>":
            del_id=input()
            delete_employee(del_id,c)
            #break

        elif command[0] == "update_employee <employee_id>":
            up_id=input()
            update_employee(up_id,c)
            print(command)
            #break

        elif command[0] == "help":
            help()
            #break


if __name__ == '__main__':
    main()
