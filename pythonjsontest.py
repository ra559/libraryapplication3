#!/usr/bin/python3
import requests
url = "https://robertalberto.com/123.json"
res = requests.get(url)
scone = res.json()
print(type(scone['docs']))
lst = scone['docs']
for item in lst:
    isbn = item['isbn']
    title = item['title']
    author = item['author_name']
    lang = item['language']
    genre = item['subject']
    publisher = item['publisher']
    #test onlu
    print('\n',isbn[0],"\n",title,"\n",author[0],"\n",lang[0],"\n",genre[0],"\n",publisher[0],"\n")
