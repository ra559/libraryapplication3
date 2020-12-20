#!/usr/bin/python3
import requests
url = "http://openlibrary.org/search.json?q="+ request.form.get['isbn']
res = requests.get(url)
print(res.json())
