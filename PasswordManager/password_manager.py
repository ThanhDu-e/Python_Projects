master_pwd = input("What is the master password? ")


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip()) # takes off the \n 

def add():
    name = input('Account name: ')
    pwd = input("Password: ")

    # w - write: create a new file or override existing file(clear file and write over)
    # r - read: can only read a file
    # a - append: add something to the end of the existing file. Can write to and read from file
    with open('passwords.txt', 'a') as f:
        f.write(name + " | " + pwd + "\n")



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