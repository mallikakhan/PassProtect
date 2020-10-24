from start import *

def main():
    print("Are you a new user? (Yes/No)")
    choice = input()
    if(choice.lower() == 'yes'):
        register()
    else:
        login()

main()
