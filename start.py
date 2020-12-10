from session import *
from connect import *
import hashlib
from tkinter import *
import tkinter.messagebox


def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Account Login")
    root2.geometry("450x300")
    root2.config(bg="white")
    # print("Enter your name:")
    global name
    global mkey

    # print("Enter your master key:")

    Label(root2, text='Please Enter your Account Details', bd=5, font=('arial', 12, 'bold'), relief="groove",
          fg="white",
          bg="blue", width=300).pack()
    name = StringVar()
    mkey = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=name).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=mkey, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Login", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=login_verification).pack()
    Label(root2, text="")
    print("login")
    # mkeyhash = hashlib.sha256(mkey.encode())
    # masterpass = hashlib.shake_256(mkey.encode())
    # cn = connector()
    # cur = cn.cursor()
    # query = "SELECT id FROM tbl_users WHERE master_hash = \'" + mkeyhash.hexdigest() + "\' and username = \'" + name + "\'"
    # cur.execute(query)
    # res = cur.fetchall()
    # cn.close()
    # if len(res) == 0:
    # print("Invalid credentials entered")
    # else:
    # session_start(res[0][0], masterpass)


def failed_destroy():
    failed_message.destroy()


def logged_destroy():
    logged_message.destroy()
    root2.destroy()


def failedpass_destroy():
    failed_pass.destroy()
    root3.destroy()


def logged():
    global logged_message
    logged_message = Toplevel(root2)
    logged_message.title("Welcome")
    logged_message.geometry("500x500")
    Label(logged_message, text="Login Successfully!... Welcome {} ".format(name.get()), fg="green",
          font="bold").pack()
    Label(logged_message, text="").pack()

    Button(logged_message, text="Access devices", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=access).pack()
    Label(logged_message, text="").pack()
    Button(logged_message, text="Add device", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=add).pack()
    Label(logged_message, text="").pack()

    Button(logged_message, text="Delete device", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=rem).pack()
    Label(logged_message, text="").pack()

    Button(logged_message, text="Logout", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=logged_destroy).pack()


def failed():
    global failed_message
    failed_message = Toplevel(root2)
    failed_message.title("Invalid Message")
    failed_message.geometry("500x100")
    Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message, text="Ok", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=failed_destroy).pack()


def failed_password():
    global failed_pass
    failed_pass = Toplevel(root3)
    failed_pass.title("Incorrect length of password")
    failed_pass.geometry("500x100")
    Label(failed_pass, text="Incorrect length, should be atleast 8 characters", fg="red", font="bold").pack()
    Label(failed_pass, text="").pack()
    Button(failed_pass, text="try again", bg="blue", fg="white", relief="groove", font=('ariel', 12, 'bold'),
           command=failedpass_destroy).pack()


def login_verification():
    xname = name.get()
    xmkey = mkey.get()
    mkeyhash = hashlib.sha256(xmkey.encode())
    global masterpass
    masterpass = hashlib.shake_256(xmkey.encode())
    cn = connector()
    cur = cn.cursor()
    sql = "SELECT id FROM tbl_users WHERE master_hash = \'" + mkeyhash.hexdigest() + "\' and username = \'" + xname + "\'"
    cur.execute(sql)
    results = cur.fetchall()
    if results:
        print("login verification")
        global id
        id = results[0][0]
        logged()
    else:
        failed()


def register():
    global root3
    # print("Enter your name:")
    global tname
    global tmkey
    tname = StringVar()
    # print("Enter a masterkey you would like to use: (Should be atleast 8 characters long)")
    tmkey = StringVar()
    root3 = Toplevel(root)
    root3.title("Account Registration")
    root3.geometry("450x300")
    root3.config(bg="white")

    Label(root3, text="").pack()
    Label(root3, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root3, textvariable=tname).pack()
    Label(root3, text="").pack()
    Label(root3, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root3, textvariable=tmkey, show="*").pack()
    Label(root3, text="").pack()
    Label(root3, text="Password should be 8 characters or more!", fg="red", font=('arial', 12, 'bold')).pack()
    Label(root3, text="").pack()
    Button(root3, text="Register", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=registration).pack()
    Label(root3, text="")


def registration():
    txname = tname.get()
    txmkey = tmkey.get()
    tmkeyhash = hashlib.sha256(txmkey.encode())
    if len(txmkey) >= 8:
        cn = connector()
        cur = cn.cursor()
        query = "INSERT INTO tbl_users(master_hash, username) values(\'" + tmkeyhash.hexdigest() + "\',\'" + txname + "\')"
        cur.execute(query)
        cn.commit()
        cn.close()
        login()
    else:
        failed_password()


def Exit():
    wayOut = tkinter.messagebox.askyesno("Login System", "Do you want to exit the system")
    print(wayOut)
    if wayOut > 0:
        root.destroy()
    return


def failed_removal():
    global failed_remove
    failed_remove = Toplevel(root2)
    failed_remove.title("Error")
    failed_remove.geometry("500x100")
    Label(failed_remove, text="No devices available or wrong option selected", fg="red", font="bold").pack()
    Label(failed_remove, text="").pack()
    Button(failed_remove, text="try again", bg="blue", fg="white", relief="groove", font=('ariel', 12, 'bold'),
           command=removal_destroy).pack()


def removal_destroy():
    failed_remove.destroy()


def success_destroy():
    success_remove.destroy()
    root6.destroy()


def success_removal():
    global success_remove
    success_remove = Toplevel(root6)
    success_remove.title("Error")
    success_remove.geometry("500x100")
    Label(success_remove, text="Device removal successful!", fg="green", font="bold").pack()
    Label(success_remove, text="").pack()
    Button(success_remove, text="Close", bg="blue", fg="white", relief="groove", font=('ariel', 12, 'bold'),
           command=success_destroy).pack()


def remove_device():
    # i = i - 1
    global acc_id
    acc_id = device_tobe_removed.get()
    print(acc_id)
    cn = connector()
    cur = cn.cursor()
    q1 = "SELECT acc_id FROM tbl_cryptostore WHERE acc_id = \'" + str(acc_id) + "\'"
    cur.execute(q1)
    re1 = cur.fetchall()
    print(re1)
    cn.close()
    if re1:
        cn = connector()
        cur = cn.cursor()
        query = "DELETE FROM tbl_cryptostore WHERE acc_id = \'" + str(acc_id) + "\'"
        cur.execute(query)
        cn.commit()
        cn.close()
        success_removal()

    else:
        failed_removal()
    '''
    if (i >= n):
        failed_removal()
    else:
        query = "DELETE FROM tbl_cryptostore WHERE acc_id = " + str(acc_id)
        cn = connector()
        cur = cn.cursor()
        cur.execute(query)
        cn.commit()
        cn.close()
    '''


def rem():
    cn = connector()
    cur = cn.cursor()
    query = "SELECT acc_id, device_name FROM tbl_cryptostore WHERE id = \'" + str(id) + "\'"
    cur.execute(query)
    res = cur.fetchall()
    cn.close()
    print("in rem")
    if res:
        global root6
        root6 = Toplevel(root2)
        root6.title("Remove devices")
        root6.geometry("500x500")
        root6.config(bg="white")

        l1 = Label(root6, text='Available devices', bd=5, font=('arial', 12, 'bold'), relief="groove",
                   fg="white",
                   bg="blue")
        global device_tobe_removed
        device_tobe_removed = StringVar()
        # l1 = Label(root6, text=res, fg="black", font=('arial', 12))
        l1.grid(row=0, column=1, columnspan=3)
        i = 1
        for p in res:
            for q in range(len(res)):
                e = Entry(root6, width=10, fg='black', bg='yellow')
                e.grid(row=i, column=1)
                # b1 = Button(root4, text='ON', fg='green', bg='white', command=lambda x=i: color_change(x))
                # b1[i].grid(row=i, column=1)
                e.insert(END, p)
            i = i + 1
        '''
        print_tuple = ''
        for x in res:
            print_tuple += str(x) + "\n"
        #query_label = Label(root6, text=print_tuple)

        # query_label.grid(row=2, column=0, columnspan=2)

        for re in res:
            for j in range(len(res)):
                Label(root6, text=res[i])
            i = i + 1
            # print(str(i + 1) + " " + str(res[i][1]))
        # i = int(input())
        '''
        i = i + 1
        l2 = Label(root6, text="Device to be removed", fg="black", font=('arial', 12, 'bold'))
        l2.grid(row=i, column=0)
        e1 = Entry(root6, textvariable=device_tobe_removed)
        e1.grid(row=i, column=1)
        i = i + 2
        # deletion_tuple = device_tobe_removed.get()
        Button(root6, text="Remove", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
               command=remove_device).grid(row=i, column=1)


    else:
        failed_removal()


def successful_add():
    global success_add
    success_add = Toplevel(root5)
    success_add.title("Success")
    success_add.geometry("500x100")
    Label(success_add, text="Device added successfully!", fg="green", font="bold").pack()
    Label(success_add, text="").pack()
    Button(success_add, text="Close", bg="blue", fg="white", relief="groove", font=('ariel', 12, 'bold'),
           command=success_add_destroy).pack()


def success_add_destroy():
    success_add.destroy()
    root5.destroy()


def add_device():
    d_name = device_name.get()
    d_id = device_id.get()
    d_pass = device_password.get()
    crypto_pass = encrypt(masterpass, d_name, d_pass)
    userid_hash = hashlib.sha256(d_name.encode())
    query = "INSERT INTO tbl_cryptostore(device_name, userid_hash, crypto_pass, id) VALUES(\'" + d_name + "\', \'" + userid_hash.hexdigest() + "\', \'" + crypto_pass + "\', " + str(
        id) + ")"
    cn = connector()
    cur = cn.cursor()
    cur.execute(query)
    cn.commit()
    cn.close()
    successful_add()


def add():
    global root5
    root5 = Toplevel(root2)
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
           command=add_device).pack()
    Label(root5, text="")


def access_pass_error():
    global pass_error
    pass_error = Toplevel(root4)
    pass_error.title("Error")
    pass_error.geometry("500x100")
    Label(pass_error, text="No devices available or wrong option selected", fg="red", font="bold").pack()
    Label(pass_error, text="").pack()
    Button(pass_error, text="try again", bg="blue", fg="white", relief="groove", font=('ariel', 12, 'bold'),
           command=access_pass_destroy).pack()


def access_pass_destroy():
    pass_error.destroy()


def access_destroy():
    failed_acc.destroy()


def failed_access():
    global failed_acc
    failed_acc = Toplevel(root2)
    failed_acc.title("Error")
    failed_acc.geometry("500x100")
    Label(failed_acc, text="No devices added yet.", fg="red", font="bold").pack()
    Label(failed_acc, text="").pack()
    Button(failed_acc, text="try again", bg="blue", fg="white", relief="groove", font=('ariel', 12, 'bold'),
           command=access_destroy).pack()


def access_my_device():
    ac = device_tobe_access.get()
    global pass_e2
    pass_e2 = StringVar()
    username = ac
    user_hash = hashlib.sha256(username.encode())
    cn = connector()
    cur = cn.cursor()
    query = "SELECT crypto_pass FROM tbl_cryptostore WHERE userid_hash = \'" + user_hash.hexdigest() + "\'"  # from cryptocheck
    cur.execute(query)
    res = cur.fetchall()
    cn.close()
    if res:
        global root7
        root7 = Toplevel(root4)
        root7.title("Accessing {} ".format(ac))
        root7.geometry("450x300")
        root7.config(bg="white")

        def color_change():
            if b1['text'] == 'ON':
                b1['text'] = 'OFF'
                b1['fg'] = 'red'
                l1['text'] = 'The device is ON'
                l1['fg'] = 'green'
            else:
                b1['text'] = 'ON'
                b1['fg'] = 'green'
                l1['text'] = 'The device is OFF'
                l1['fg'] = 'red'

        def insert_pass():
            print("inside insert pass")
            print(res)
            print(res[0][0])
            ans = decrypt(masterpass, username, res[0][0])
            print(ans)
            e2.insert(END, ans)

        # on/off button
        b1 = Button(root7, text='ON', fg='green', bg='white', width=20, command=color_change)
        b1.grid(row=3, column=1)

        l1 = Label(root7, text='The device is off', fg='red')
        l1.grid(row=3, column=3)

        # label for accepting device id
        # Label(root7, text="Device Id: ", fg="black", font=('arial', 12, 'bold')).grid(row=1, column=0)
        # e1 = Entry(root7, width=20)
        # e1.grid(row=1, column=3)
        # e1.insert(str(username))
        # e1 = Entry(root7, textvariable=pass_e2).grid(row=3, column=1)

        e2 = Entry(root7, width=20)
        e2.grid(row=5, column=3)

        b2 = Button(root7, text="Get Password", fg="blue", bg="white", width=20, command=insert_pass)
        b2.grid(row=5, column=1)

        b3 = Button(root7, text="EXIT", fg="blue", bg="white", command=root7.destroy)
        b3.grid(row=7, column=1)

    else:
        access_pass_error()


# changed version
def access():
    cn = connector()
    cur = cn.cursor()
    query = "SELECT acc_id, device_name FROM tbl_cryptostore WHERE id = \'" + str(id) + "\'"
    cur.execute(query)
    res = cur.fetchall()
    cn.close()

    if res:
        global root4
        root4 = Toplevel(root2)
        root4.title("My devices")
        root4.geometry("450x300")
        root4.config(bg="white")
        '''
        def color_change(x):
            if b1[x].cget('text') == 'ON':
                b1[x].configure(text='OFF', fg='red')
            else:
                b1[x].configure(text='ON', fg='green')
        '''
        global device_tobe_access
        device_tobe_access = StringVar()
        print("\nAvailable devices:")
        Label(root4, text="Device Id: ", fg="black", font=('arial', 12, 'bold')).grid(row=0, column=0)
        Entry(root4, textvariable=device_tobe_access).grid(row=0, column=1)
        Button(root4, text="Access", fg="green", bg="white", command=access_my_device).grid(row=0, column=3)
        Button(root4, text="Back", fg="green", bg="white", command=root4.destroy).grid(row=0, column=4)
        # b2=Button(root4, text="Password", fg="blue", bg="white", command=cryptocheck)
        i = 1
        print(res)
        for p in res:
            for q in range(len(res)):
                e = Entry(root4, width=20, fg='blue')
                e.grid(row=i, column=0)
                e.insert(END, p)

            i = i + 1

        '''
        print_tuple = ''
        for x in res:
            print_tuple += str(x) + "\n"
    '''
    else:
        failed_access()


# main driver
def main():
    print("hello")
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Login System")
    root.geometry("500x500")

    background_img = PhotoImage(file='homepic.png')
    background_label = Label(root, image=background_img)
    background_label.place(relheight=2, relwidth=1)

    Label(root, text='Welcome to SmartHome systems', bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",
          bg="blue", width=300).pack()
    Label(root, text="").pack()
    Button(root, text='Log In', height="1", width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
           bg="blue", command=login).pack()
    Label(root, text="").pack()
    Button(root, text='Register', height="1", width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
           bg="blue", command=register).pack()
    Label(root, text="").pack()
    Button(root, text='Exit', height="1", width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
           bg="blue", command=Exit).pack()
    Label(root, text="").pack()

    print("hello")


main()
root.mainloop()
