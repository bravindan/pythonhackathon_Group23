
import datetime

lock_password = "1234"
lock_command = ""
lock_command_open = "open"
lock_command_close = "close"
lock_command_quit = "quit"
lock_command_invalid = "invalid"
lock_command_open_count = 0
lock_command_close_count = 0
lock_command_quit_count = 0
lock_command_invalid_count = 0
lock_command_open_date = ""
lock_command_close_date = ""

passw =input("Enter the password: ")
while passw != lock_password:
    print("Invalid password")
    passw =input("Enter the password: ")
while lock_command != lock_command_quit:
    lock_command = input("Enter the command: ")
    if lock_command == lock_command_open:
        lock_command_open_count += 1
        if lock_command_open_count == 1:
            lock_command_open_date = str(datetime.datetime.now())
            print("The door is now open")
            print("Door Last open at", lock_command_open_date)
        else:
            print("The door is already open")
    elif lock_command == lock_command_close:
        lock_command_close_count += 1
        if lock_command_close_count == 1:
            lock_command_close_date = str(datetime.datetime.now())
            print("The door is now locked")
            print("Door Last closed at", lock_command_close_date)
        else:
            print("The door is already locked")
    elif lock_command == lock_command_quit:
        lock_command_quit_count += 1
        if lock_command_quit_count == 1:
            print("The door is now closed")
        else:
            print("The door is already closed")
    elif lock_command == lock_command_invalid:
        lock_command_invalid_count += 1
        if lock_command_invalid_count == 1:
            print("Invalid input")
        else:
            print("Invalid input")
    else:
        print("Invalid input")