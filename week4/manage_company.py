import sqlite3

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
            break

        elif command[0] == "yearly_spending":
            yearly_spending(c)
            print(command)
            break
        elif command[0] == "add_employee":
            print(command)
            break

        elif command[0] == "delete_employee <employee_id>":
            print(command)
            break

        elif command[0] == "update_employee <employee_id>":
            print(command)
            break

        elif command[0] == "help":
            break


if __name__ == '__main__':
    main()
