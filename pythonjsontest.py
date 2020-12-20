#!/usr/bin/python3
import requests
import json
url = "http://openlibrary.org/search.json?q=9780684867625"
res = requests.get(url)
scone = res.json()
for key, value in scone.items():
    print("---------------->")
    print(value, key)
