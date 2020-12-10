from start import *
<<<<<<< HEAD
from tkinter import *
import tkinter.messagebox




=======
import os
from time import sleep

def main():
    while(1):
    	os.system('CLS')
    	print("Are you a new user? (Yes / No / Anything else to exit)")
    	choice = input()
    	if(choice.lower() == 'yes'):
    		os.system('CLS')
    		register()
    	elif(choice.lower() == 'no'):
    		os.system('CLS')
    		login()
    	else:
    		exit()
main()
>>>>>>> 3584a0ec3a744c24353f49d22e5e637bbc0011f5
