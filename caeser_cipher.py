a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def encryption():
    p=input("Enter the text to cipher in capital: ")
    k=int(input("Enter the key: "))
    cip=""
    l=len(p)
    a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if(k<26):
        for i in range(0,l):
            if(p[i]==" "):
                cip+=" "
                continue
            c=int(search(p[i]))
            ci=(c+k)%26
            cip=cip+a[ci]
        print(cip,"\n")
    else:
        print("Invalid key\n")


def search(c):
    g=0;
    index=0
    while(g<26):
        if(a[g]==c):
            index=g
            return index
        g+=1
def decryption():
    c=input("Enter the code to deciphered in CAPITAL letters: ")
    k=int(input("Enter the key: "))
    de=""
    if(k<26):
        for i in range(0,len(c)):
            if(c[i]==" "):
                de+=" "
                continue
            decipher_index=search(c[i])
            d=(decipher_index-k)
            if d>0:
                di=d%26
                de+=a[di]
            elif(d<0):
                di=(26+d)%26
                de+=a[di]
        print(de,"\n")
    else:
        print("Invalid Key\n")

def main():
    print("Choose what to do from the below list: ")
    print("1.Encrypt Data")
    print("2.Decrypt Data")
    print("Enter any value less than 0 to exit the program\n")
    b=0
    while(b!=-1):
        b=int(input("Enter the choice from the list: "))
        if b==1:
            print("")
            encryption()
        elif b==2:
            print("")
            decryption()
        elif(b<0):
            return
        else:
            print("Invalid Choice......Enter again")
            print("")
main()
