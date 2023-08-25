import subprocess
print("Checking if mysql-connector-python is installed...\n")
subprocess.check_call(["pip", "install", "mysql-connector-python"])
import mysql.connector


print("Connecting to mysql...")

#host=input("\nEnter hostname(i.e. localhost): "),
user=input("Enter user name(i.e. root): "),
password=input(f"Enter password for {user}: ")
db_connection = mysql.connector.connect(user=user[0], password=password)

cursor = db_connection.cursor()
print(f"Successfully connected as {user[0]}")

#create_new_local_user = f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}';"
#give_all_local_privileges = f"GRANT ALL PRIVILEGES ON *.* TO '{username}'@'localhost' WITH GRANT OPTION;"
#create_new_global_user = f"CREATE USER '{username}'@'%' IDENTIFIED BY '{password}';"
#give_all_global_privileges = f"GRANT ALL PRIVILEGES ON *.* TO '{username}'@'%' WITH GRANT OPTION;"

def new_super_user():
    print('test')
    username = input("Enter a username: ")
    password = input("Enter a new password: ")

    create_new_local_user = f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}';"
    give_all_local_privileges = f"GRANT ALL PRIVILEGES ON *.* TO '{username}'@'localhost' WITH GRANT OPTION;"
    create_new_global_user = f"CREATE USER '{username}'@'%' IDENTIFIED BY '{password}';"
    give_all_global_privileges = f"GRANT ALL PRIVILEGES ON *.* TO '{username}'@'%' WITH GRANT OPTION;"


    cursor.execute(create_new_local_user)
    cursor.execute(give_all_local_privileges)
    cursor.execute(create_new_global_user)
    cursor.execute(give_all_global_privileges)
    print(f"Super user {username} has been created")

    end_command()

def create_database():
    db_name = input("Enter new database name")
    cursor.execute(f"CREATE DATABASE {db_name};")
    end_command()

def menu():
    print("\n 🐱🐱🐱🐱🐱🐱🐱🐱")
    print("\n 0 - Create new super user")
    print("\n 1 - Create database")
    print("\n q - Exit")
    print("\n 🐱🐱🐱🐱🐱🐱🐱🐱")
    choice = input("ENTER CHOICE: ")

    if choice == '0':
        print("Entering new_super_user() function...")
        new_super_user()
    elif choice == '1':
        print("Entering Create_Database() function...")
        create_database()
    elif choice == 'q':
        print("Now exiting...")
        cursor.close()
        db_connection.close()
        exit()


def end_command():
    print("Returning to menu...")
    menu()
    



menu()
