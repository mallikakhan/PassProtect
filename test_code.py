
'''
import mysql.connector as con

mydb = con.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'mumu2000'
)

print(mydb)
print()
print()



from des import DesKey
import hashlib

masterkey = "demo4master8key1"
userid = "shashankh.s22@gmail.com"


masterhash = hashlib.sha256(masterkey.encode())
userhash = hashlib.sha256(userid.encode())
print('To be checked with DB:')
print(masterhash.hexdigest())
print(userhash.hexdigest())
print()
print()


masterpass = hashlib.shake_256(masterkey.encode())
userpass = hashlib.shake_256(userid.encode())

masterpass = masterpass.hexdigest(24)
userpass = userpass.hexdigest(24)

masterpass = bytearray.fromhex(masterpass)
userpass = bytearray.fromhex(userpass)

masterpass = DesKey(masterpass)
userpass = DesKey(userpass)


testpass = "info9crypt1"
print('Before encryption')
print(testpass)
print()

cipher = masterpass.encrypt(bytes(testpass, 'utf-8') , padding = True)
cipher = userpass.encrypt(cipher, padding = True)
cipher = masterpass.encrypt(cipher, padding = True)

print('After encryption')
print(cipher)
print()

cipher1 = ''
for i in cipher:
	cipher1 = cipher1 + format(i, '02x')
print("Store in DB as:")
print(cipher1)
print()

cipher2 = bytes.fromhex(cipher1)
print("Use for decrypt as: ")
print(cipher2)
print()


plain = masterpass.decrypt(cipher2, padding = True)
plain = userpass.decrypt(plain, padding = True)
plain = masterpass.decrypt(plain, padding = True)

print('After decryption')
print(plain)
print(plain.decode())



import string
import random


def passGen(size):
	sample = string.ascii_letters + string.digits + '!@#$%^&*-_+=?><'
	passwd = ''.join((random.choice(sample) for i in range(size)))
	print(passwd)


passGen(14)

'''

a = input('Enter: ')
print("Done")