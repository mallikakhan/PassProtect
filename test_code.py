import mysql.connector as con

mydb = con.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'info9crypt1'
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

plain = masterpass.decrypt(cipher, padding = True)
plain = userpass.decrypt(plain, padding = True)
plain = masterpass.decrypt(plain, padding = True)

print('After decryption')
print(plain.decode())
