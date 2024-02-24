import time
class Main_Page:
    print('Hello. This program is needed for authorization or registration!')
    time.sleep(2)
    have_unhave = input('You want login or register: ')  
    if have_unhave == 'register':
            while True:
                name = input("Write your name: ")
                if not name.isalpha():
                    print("Please, enter a letter name!")
                else:
                    break
            while True:
                surname = input("Write your surname: ")
                if not surname.isalpha():
                    print("Please, enter a letter surname!")
                else:
                    break
            username = input("Write username: ")
            print ("Your username: ", username)
            while True:
                password = input("Write password: ")
                password2 = input("Confirm password: ")
                if password != password2:
                    print("Passwords didn't match!")
                else:
                    break 
            account = '%s:%s\n'%(username,password)
            with open ('base.txt','a') as file:
                file.write(account)
                print ('Account saved!')   

    elif have_unhave == 'login':
        def login():
            with open('base.txt', 'r') as file:
                login2 = input("Write username: ")
                passw2 = input("Write passwordd: ")
                for line in file:
                    user2, passw = line.split(':')
                    if login2 == user2 and passw2 == passw:
                        print("Logged in")
                        break
                    else:
                        continue

        login()

    else:
        print('Please, write other answer.')
