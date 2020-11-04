from connect import connector
import hashlib
from des import DesKey

def session_start(id, masterpass):
    print("1. Access Password")
    print("2. Add Password")
    print("3. Delete Password")
    print("4. Logout")
    i = int(input("Enter choice: "))
    print("\n\n")

    if(i == 1):
        access(id, masterpass)
    elif(i == 2):
        add(id, masterpass)
    elif(i == 3):
        rem(id, masterpass)
    elif(i == 4):
        return
    else:
        print("Wrong input")
        session_start(id, masterpass)

def access(id, masterpass):
    cn = connector()
    cur = cn.cursor()
    query = "SELECT acc_id, website_name FROM tbl_cryptostore WHERE id = \'" + str(id) +"\'"
    cur.execute(query)
    res = cur.fetchall()
    cn.close()
    if(len(res) == 0):
        print("No passwords stored yet", end='\n\n')
        session_start(id, masterpass)
    else:
        print("\nAvailable Accounts:")
        for i in range(len(res)):
            print(str(i + 1) + " " + str(res[i][1]))
        i = int(input())
        i = i - 1
        if(i >= len(res)):
            print("Wrong Option")
            access(id)
        else:
            acc_id = res[i][0]
            cryptocheck(id, acc_id, masterpass)
        session_start(id, masterpass)

def cryptocheck(id, acc_id, masterpass):
    print("Enter username/email id used for this account")
    username = input()
    user_hash = hashlib.sha256(username.encode())
    cn = connector()
    cur = cn.cursor()
    query = "SELECT crypto_pass FROM tbl_cryptostore WHERE userid_hash = \'" + user_hash.hexdigest() +"\'"
    cur.execute(query)
    res = cur.fetchall()
    cn.close()
    if(len(res) <= 0):
        print("Invalid username entered\n\n")
        session_start(id, masterpass)
    else:
        print("Password:  " + decrypt(masterpass, username, res[0][0]), end='\n\n\n')

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
    plain = masterpass.decrypt(cipher1, padding = True)
    plain = userpass.decrypt(plain, padding = True)
    plain = masterpass.decrypt(plain, padding = True)

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

    cipher = masterpass.encrypt(bytes(plain, 'utf-8') , padding = True)
    cipher = userpass.encrypt(cipher, padding = True)
    cipher = masterpass.encrypt(cipher, padding = True)

    cipher1 = ''
    for i in cipher:
    	cipher1 = cipher1 + format(i, '02x')
    return cipher1

def add(id, masterpass):
    web = input("Enter website name: ")
    username = input("Enter username or email id used for this website: ")
    password = input("Enter password used for this website: ")
    crypto_pass = encrypt(masterpass, username, password)
    userid_hash = hashlib.sha256(username.encode())
    query = "INSERT INTO tbl_cryptostore(website_name, userid_hash, crypto_pass, id) VALUES(\'"+web+"\', \'"+userid_hash.hexdigest()+"\', \'"+crypto_pass+"\', "+str(id)+")"
    cn = connector()
    cur = cn.cursor()
    cur.execute(query)
    cn.commit()
    cn.close()
    session_start(id, masterpass)

def rem(id, masterpass):
    cn = connector()
    cur = cn.cursor()
    query = "SELECT acc_id, website_name FROM tbl_cryptostore WHERE id = \'" + str(id) +"\'"
    cur.execute(query)
    res = cur.fetchall()
    cn.close()
    if(len(res) == 0):
        print("No passwords stored yet", end='\n\n')
        session_start(id, masterpass)
    else:
        print("\nAvailable Accounts:")
        for i in range(len(res)):
            print(str(i + 1) + " " + str(res[i][1]))
        i = int(input())
        i = i - 1
        if(i >= len(res)):
            print("Wrong Option")
            access(id)
        else:
            acc_id = res[i][0]
            query = "DELETE FROM tbl_cryptostore WHERE acc_id = "+ str(acc_id)
            cn = connector()
            cur = cn.cursor()
            cur.execute(query)
            cn.commit()
            cn.close()
        print("\n\n\n")
        session_start(id, masterpass)
