import pyshorteners

from allmodules import *
def shorten_url(url):
    s=pyshorteners.Shortener()
    f=s.tinyurl.short(url)
    return f

#read url from txt file

with open('url.txt','r') as file:
    c=file.readlines()

su={}
for i in c:
    i=i.strip()
    f=shorten_url(i)
    su[i]=f


filename = "data.json"

with open(filename, "w") as file:
    json.dump(su,file,indent=4)

