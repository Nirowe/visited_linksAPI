from django.test import TestCase
import requests
from json import dumps

d1 = [
        "https://ya.ru",
        "https://ya.ru?q=123",
        "funbox.ru",
        "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
        ]
#
# print(d1)
# print(dumps(d1))
# # Create your tests here.
# re = requests.post('http://127.0.0.1:8000/api/visited_links/', data = {'links':dumps(d1)})


re = requests.get('http://127.0.0.1:8000/api/visited_domains?from=1573252088&to=1573252087')
print(re.text)