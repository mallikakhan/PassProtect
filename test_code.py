''' To check mysql connector
import mysql.connector as con

mydb = con.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'info9crypt1'
)

print(mydb)
'''

from des import DesKey
import hashlib

masterkey = "masterkey123"
userid = "shashankh.s22@gmail.com"

#Following for authentication with the hash stored in DB
'''
masterhash = hashlib.sha256(masterkey.encode())
userhash = hashlib.sha256(userid.encode())
print('To be checked with DB:')
print(masterhash.hexdigest())
print(userhash.hexdigest())
'''


'''
# Following for creation of key for the DES encrypt/decrypt
masterpass = hashlib.shake_256(masterkey.encode())
userpass = hashlib.shake_256(userid.encode())

masterpass = DesKey(bytearray.fromhex(masterpass.hexdigest(24)))
userpass = DesKey(bytearray.fromhex(userpass.hexdigest(24)))
'''


'''
# Following for encryption and decryption of password when storing or retrieving from DB
testpass = "info9crypt1"
print('Before encryption')
print(testpass)

cipher = masterpass.encrypt(bytes(testpass, 'utf-8') , padding = True)
cipher = userpass.encrypt(cipher, padding = True)

print('After encryption')
print(cipher)

plain = userpass.decrypt(cipher, padding = True)
plain = masterpass.decrypt(plain, padding = True)

print('After decryption')
print(plain.decode())
'''


