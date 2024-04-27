from cryptography.fernet import Fernet


def key_generate():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def key_load():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = key_load()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, ", Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account name: ')
    pwd = input("Password: ")

    # w - write: create a new file or override existing file(clear file and write over)
    # r - read: can only read a file
    # a - append: add something to the end of the existing file. Can write to and read from file
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode()+ "\n")



while(True):        
    mode = input("Would you like to add a new password or view an existing one (view, add). Press q to quit: ").lower()
    if mode == "q":
        break


    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode")
        continue