import sqlite3

def command_split(command):
    return command.split(" ")


def main():
    while True:
        command = command_split(input("command>"))

        if command[0] == "list_employees":
            print(command)
        break


if __name__ == '__main__':
    main()
