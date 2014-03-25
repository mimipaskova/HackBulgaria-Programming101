import sqlite3

def command_split(command):
    return command.split(" ")


def main():
    while True:
        command = command_split(input("command>"))

        if command[0] == "list_employees":
            print(command)
        elif command[0] == "monthly_spending":

        elif command[0] == "yearly_spending":

        elif command[0] == "add_employee":

        elif command[0] == "delete_employee <employee_id>":

        elif command[0] == "update_employee <employee_id>":

        elif command[0] == "help":
        break


if __name__ == '__main__':
    main()
