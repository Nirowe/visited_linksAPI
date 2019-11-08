# d1 = [
#         "https://ya.ru",
#         "https://ya.ru?q=123",
#         "funbox.ru",
#         "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
#         ]
# res = []
# for i in range(len(d1)):
#     print(d1[i])
#     temp1 = d1[i].split('/')
#     print(temp1)
#     #print(temp1[2].split('?'))
#
#     if temp1[0] == 'https:' or temp1[0] == 'http:':
#         if '?' in temp1[2]:
#             temp1 = temp1[2].split('?')[0]
#         else:
#             temp1 = temp1[2]
#         res.append(temp1)
#     else:
#         if '?' in temp1[0]:
#             temp1 = temp1[0].split('?')[0]
#         else:
#             temp1 = temp1[0]
#         res.append(temp1)
# print(res)

# from datetime import datetime
# from time import sleep
# print(datetime.today().timestamp())
# sleep(1)
# print(datetime.today().timestamp())


d1 = {'1573251058.650278': '["https://ya.ru", "https://ya.ru?q=123", "funbox.ru", "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"]', '1573251058.661279': '["https://python-scripts.com/import-collections", "https://trello.com/b/Ny50pyFq/visitrecord"]', '1573251058.674279': '["http://qaru.site/questions/589159/django-dynamic-urls"]'}
for key in d1.keys():
    print(d1[key])
