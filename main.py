from start import *

def main():
    print("Are you a new user? (Yes / No / Anything else to exit)")
    choice = input()
    if(choice.lower() == 'yes'):
        register()
    elif(choice.lower() == 'no'):
        login()
    else:
        exit()
    main()

main()
