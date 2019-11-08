from django.shortcuts import render
from rest_framework import generics
from .models import *
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from json import *
from django.core.cache import cache
from datetime import datetime
from collections import *
import time


@api_view(['POST'])
def VisitedLinks(request):
    data = request.data['links']  # type string(json)
    data = loads(data)
    temp_date = str(datetime.today().timestamp())
    cache.add(temp_date, dumps(data))
    print(temp_date, cache.get(temp_date))
    answer = {
        "status": "ok"

    }
    answer = dumps(answer)
    return Response(answer,status=status.HTTP_200_OK)


@api_view(['GET'])
def GetStatisticTimeIntervar(requests):
    from_date = int(requests.GET.get('from'))
    to_date = int(requests.GET.get('to'))
    #предусмотреть ситуацию, когда эти два числа одинаковые.
    #Вернуть status: time interval error
    #и его описание

    #так же посмотреть ситуацию когда начао и конец интерваа перепутаны.

    response_list = []
    for i in range(to_date, from_date):
        time_dict = dict(cache.get_many(cache.keys(str(i) + '.*')))
        for key in time_dict.keys():
            list_links = time_dict[key]
            for link in loads(list_links):
                print(link)
                print('link')
                temp1 = link.split('/')
                if temp1[0] == 'https:' or temp1[0] == 'http:':
                    if '?' in temp1[2]:
                        temp1 = temp1[2].split('?')[0]
                    else:
                        temp1 = temp1[2]
                    print(temp1 + 'добавлю')
                    response_list.append(temp1)
                else:
                    if '?' in temp1[0]:
                        temp1 = temp1[0].split('?')[0]
                    else:
                        temp1 = temp1[0]
                    print(temp1 + 'добавлю')
                    response_list.append(link)

    response_dict = {'domains':response_list,
                     'status':'ok'}
    return Response(dumps(response_dict))




