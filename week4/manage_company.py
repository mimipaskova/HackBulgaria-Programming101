import sqlite3

def create_connect():
    conn = sqlite3.connect("create_bank")
    c = conn.cursor()


def list_employees(c):
    my_list = "SELECT name, position FROM company;"
    print(c.execute(my_list))

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
            print(command)
            break

        elif command[0] == "yearly_spending":
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
