from django.test import TestCase
import requests
from json import dumps
import time
from datetime import datetime

print(str(datetime.today().timestamp()) + ' - время начала')
d1 = [
        "https://ya.ru",
        "https://ya.ru?q=123",
        "funbox.ru",
        "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
        ]
re = requests.post('http://127.0.0.1:8000/api/visited_links/', data = {'links':dumps(d1)})
# time.sleep(1)

d2 = [
    'https://python-scripts.com/import-collections',
    'https://trello.com/b/Ny50pyFq/visitrecord',
]
re = requests.post('http://127.0.0.1:8000/api/visited_links/', data = {'links':dumps(d2)})
# time.sleep(1)

d3 = [
    'http://qaru.site/questions/589159/django-dynamic-urls'
]
re = requests.post('http://127.0.0.1:8000/api/visited_links/', data = {'links':dumps(d3)})
print(str(datetime.today().timestamp())+ ' - время окончания')

