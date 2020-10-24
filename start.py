from connect import connector
from session import session_start
import hashlib

def login():
    print("Enter your name:")
    name = input().lower()
    print("Enter your mater key:")
    mkey = input()
    mkeyhash = hashlib.sha256(mkey.encode())
    cn = connector()
    cur = cn.cursor()
    query = "SELECT id FROM tbl_users WHERE master_hash = \'" + mkeyhash.hexdigest() +"\' and username = \'" + name +"\'"
    cur.execute(query)
    res = cur.fetchall()
    cn.close()
    if(len(res) == 0):
        print("Invalid credentials entered")
    else:
        session_start(res[0][0])


def register():
    print("Enter your name:")
    tname = input().lower()
    print("Enter a masterkey you would like to use: (Should be atleast 8 characters long)")
    tmkey = input()
    tmkeyhash = hashlib.sha256(tmkey.encode())
    if(len(tmkey) >= 8):
        query = "INSERT INTO tbl_users(master_hash, username) values(\'"+tmkeyhash.hexdigest()+"\',\'"+tname+"\')"
        cn = connector()
        cur = cn.cursor()
        cur.execute(query)
        cn.commit()
        cn.close()
        login()
    else:
        print("Please make sure it is atleast 8 characters long")
        register()
