import json
import pyperclip
import sys
def adding_new_account():
    f=open('password.json','w')
    file=json.load(f.read())
    data={}
    count=1
    site=input("Enter the website for storing password:- ")
    if site in file.keys:
        print("Enter the data: ")
        key_name="account"+ str(count)
        data[key_name]=input('Enter the log in id: ')

    else:


def main():
    f=open('password.json','r')
    if(sys.argv[2] not in f):
        print("Account for the website not found.\nWould you like to add it to the database[Y/N]:- ",end="")
        ch=input()
        if(ch=="Y" or ch=='y'):
            print("Adding account to the database..................................................")
            adding_new_account()
