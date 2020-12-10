from connect import connector
import hashlib
import string
import random
from des import DesKey
import os
from time import sleep

<<<<<<< HEAD
=======
def session_start(id, masterpass):
    os.system('CLS')
    print("1. Access Password")
    print("2. Add Password")
    print("3. Delete Password")
    print("4. Exit")
    i = int(input("Enter choice: "))
    print("\n")

    if(i == 1):
        access(id, masterpass)
    elif(i == 2):
        add(id, masterpass)
    elif(i == 3):
        rem(id, masterpass)
    elif(i == 4):
        exit()
    else:
        print("Wrong input")
        a = input("Press enter to continue")
        session_start(id, masterpass)
>>>>>>> 3584a0ec3a744c24353f49d22e5e637bbc0011f5

# def session_start(id, masterpass):
# print("1. Access device")
# print("2. Add device")
# print("3. Delete device")
# print("4. Logout")
# i = int(input("Enter choice: "))
# print("\n\n")

# if (i == 1):
# access(id, masterpass)
# elif (i == 2):
# add(id, masterpass)
# elif (i == 3):
# rem(id, masterpass)
# elif (i == 4):
# return
# else:
# print("Wrong input")
# session_start(id, masterpass)
'''
def access(id, masterpass):
    global root4
    root4 = Toplevel(logged_message)
    root4.title("My devices")
    root4.geometry("450x300")
    root4.config(bg="white")

    cn = connector()
    cur = cn.cursor()
    query = "SELECT acc_id, device_name FROM tbl_cryptostore WHERE id = \'" + str(id) + "\'"
    cur.execute(query)
    res = cur.fetchall()
    cn.close()
<<<<<<< HEAD
    if (len(res) == 0):
        print("No passwords of devices stored yet", end='\n\n')
=======
    if(len(res) == 0):
        print("No passwords stored yet", end='\n\n')
        a = input("Press enter to continue")
>>>>>>> 3584a0ec3a744c24353f49d22e5e637bbc0011f5
        session_start(id, masterpass)
    else:
        print("\nAvailable devices:")
        for i in range(len(res)):
            print(str(i + 1) + " " + str(res[i][1]))
        i = int(input())
        i = i - 1
        if (i >= len(res)):
            print("Wrong Option")
            a = input("Press enter to continue")
        else:
            acc_id = res[i][0]
            cryptocheck(id, acc_id, masterpass)
        session_start(id, masterpass)
        
        
        


def cryptocheck(id, acc_id, masterpass):
    print("Enter device ID used for this device")
    username = input()
    user_hash = hashlib.sha256(username.encode())
    cn = connector()
    cur = cn.cursor()
    query = "SELECT crypto_pass FROM tbl_cryptostore WHERE userid_hash = \'" + user_hash.hexdigest() + "\'"
    cur.execute(query)
    res = cur.fetchall()
    cn.close()
    if (len(res) <= 0):
        print("Invalid username entered\n\n")
        sleep(2)
        session_start(id, masterpass)
    else:
        print("Password:  " + decrypt(masterpass, username, res[0][0]), end='\n\n\n')
<<<<<<< HEAD
'''
=======
        a = input("Press enter to continue")
>>>>>>> 3584a0ec3a744c24353f49d22e5e637bbc0011f5

def decrypt(masterpass, userid, cipher):
    # masterpass = hashlib.shake_256(masterkey.encode())
    userpass = hashlib.shake_256(userid.encode())

    masterpass = masterpass.hexdigest(24)
    userpass = userpass.hexdigest(24)

    masterpass = bytearray.fromhex(masterpass)
    userpass = bytearray.fromhex(userpass)

    masterpass = DesKey(masterpass)
    userpass = DesKey(userpass)

    cipher1 = bytes.fromhex(cipher)
    plain = masterpass.decrypt(cipher1, padding=True)
    plain = userpass.decrypt(plain, padding=True)
    plain = masterpass.decrypt(plain, padding=True)

    return plain.decode()


def encrypt(masterpass, userid, plain):
    # masterpass = hashlib.shake_256(masterkey.encode())
    userpass = hashlib.shake_256(userid.encode())

    masterpass = masterpass.hexdigest(24)
    userpass = userpass.hexdigest(24)

    masterpass = bytearray.fromhex(masterpass)
    userpass = bytearray.fromhex(userpass)

    masterpass = DesKey(masterpass)
    userpass = DesKey(userpass)

    cipher = masterpass.encrypt(bytes(plain, 'utf-8'), padding=True)
    cipher = userpass.encrypt(cipher, padding=True)
    cipher = masterpass.encrypt(cipher, padding=True)

    cipher1 = ''
    for i in cipher:
        cipher1 = cipher1 + format(i, '02x')
    return cipher1

'''
def add(id, masterpass):
<<<<<<< HEAD
    global root5
    root5 = Toplevel(logged_message)
    root5.title("Add devices")
    root5.geometry("450x300")
    root5.config(bg="white")

    global device_name
    global device_id
    global device_password

    Label(root5, text='Please Enter your Device Details', bd=5, font=('arial', 12, 'bold'), relief="groove",
          fg="white",
          bg="blue", width=300).pack()

    device_name = StringVar()
    device_id = StringVar()
    device_password = StringVar()

    Label(root5, text="").pack()
    Label(root5, text="Device Name ", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root5, textvariable=device_name).pack()
    Label(root5, text="").pack()
    Label(root5, text="Device Id", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root5, textvariable=device_id).pack()
    Label(root5, text="").pack()
    Label(root5, text="Device Password", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root5, textvariable=device_password).pack()

    Button(root5, text="ADD", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=add_device(id, masterpass)).pack()
    Label(root5, text="")


def add_device(id, masterpass):
    d_name = device_name.get()
    d_id = device_id.get()
    d_pass = device_password.get()
    crypto_pass = encrypt(masterpass, d_name, d_pass)
    userid_hash = hashlib.sha256(d_name.encode())
    query = "INSERT INTO tbl_cryptostore(device_name, userid_hash, crypto_pass, id) VALUES(\'" + d_name + "\', \'" + userid_hash.hexdigest() + "\', \'" + crypto_pass + "\', " + str(
        id) + ")"
=======
    web = input("Enter website name: ")
    username = input("Enter username or email id used for this website: ")
    passGen(random.randint(10,14))
    password = input("Enter password used for this website: ")
    crypto_pass = encrypt(masterpass, username, password)
    userid_hash = hashlib.sha256(username.encode())
    query = "INSERT INTO tbl_cryptostore(website_name, userid_hash, crypto_pass, id) VALUES(\'"+web+"\', \'"+userid_hash.hexdigest()+"\', \'"+crypto_pass+"\', "+str(id)+")"
>>>>>>> 3584a0ec3a744c24353f49d22e5e637bbc0011f5
    cn = connector()
    cur = cn.cursor()
    cur.execute(query)
    cn.commit()
    cn.close()
<<<<<<< HEAD
    logged(id, masterpass)

=======
    print("Done...")
    a = input("Press enter to continue")
    session_start(id, masterpass)
>>>>>>> 3584a0ec3a744c24353f49d22e5e637bbc0011f5

def rem(id, masterpass):
    cn = connector()
    cur = cn.cursor()
    query = "SELECT acc_id, device_name FROM tbl_cryptostore WHERE id = \'" + str(id) + "\'"
    cur.execute(query)
    res = cur.fetchall()
    cn.close()
    i = 0
    n = len(res)
    if res:
        global root6
        root6 = Toplevel(logged_message)
        root6.title("Add devices")
        root6.geometry("450x300")
        root6.config(bg="white")

        Label(root6, text='Available devices', bd=5, font=('arial', 12, 'bold'), relief="groove",
              fg="white",
              bg="blue", width=300).pack()
        for x in res:
            for j in range(len(res)):
                e = Entry(root6, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, res[j])
            i = i + 1
            # print(str(i + 1) + " " + str(res[i][1]))
        # i = int(input())
        # i = i - 1

        Label(root6, text="Device to be removed", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=i, show="*").pack()
        Label(root2, text="").pack()

        Button(root2, text="Remove", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
               command=remove_device(res[i][0], n, i)).pack()
        Label(root2, text="")


    else:
<<<<<<< HEAD
        failed_removal()


def remove_device(num, n, i):
    global acc_id
    acc_id = num
    if (i >= n):
        failed_removal()
    else:
        query = "DELETE FROM tbl_cryptostore WHERE acc_id = " + str(acc_id)
        cn = connector()
        cur = cn.cursor()
        cur.execute(query)
        cn.commit()
        cn.close()
        logged(id, masterpass)


def failed_removal():
    global failed_remove
    failed_remove = Toplevel(root6)
    failed_remove.title("Error")
    failed_remove.geometry("500x100")
    Label(failed_remove, text="No devices available or wrong option selected", fg="red", font="bold").pack()
    Label(failed_remove, text="").pack()
    Button(failed_remove, text="try again", bg="blue", fg="white", relief="groove", font=('ariel', 12, 'bold'),
           command=removal_destroy).pack()


def removal_destroy():
    failed_remove.destroy()
    root6.destroy()
'''
=======
        print("\nAvailable Accounts:")
        for i in range(len(res)):
            print(str(i + 1) + " " + str(res[i][1]))
        i = int(input())
        i = i - 1
        if(i >= len(res)):
            print("Wrong Option")
        else:
            acc_id = res[i][0]
            query = "DELETE FROM tbl_cryptostore WHERE acc_id = "+ str(acc_id)
            cn = connector()
            cur = cn.cursor()
            cur.execute(query)
            cn.commit()
            cn.close()
        a = input("Press enter to continue")
        session_start(id, masterpass)


def passGen(size):
    sample = string.ascii_letters + string.digits + '!@#$%^&*-_+=?><'
    passwd = ''.join((random.choice(sample) for i in range(size)))
    print("Suggested Password: " + passwd)
>>>>>>> 3584a0ec3a744c24353f49d22e5e637bbc0011f5
