import requests
import sys
r=requests.get(sys.argv[1])
f=open('1.jpeg','wb')
f.write(r.content)
