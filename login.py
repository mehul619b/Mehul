def login():
    print("\t\t\tLogin")
    a=input("Username: ")
    password="abcd"
    c=0
    while(True and c<10):
        p=input("Password: ")
        if(password==p):
            print("Access Granted")
            return
        else:
            print("Invalid password!!Enter the password again..")
        c+=1
    print("You have tried the maximum number of times.Goodbye!")
    _=input("Press enter to exit")
login()

