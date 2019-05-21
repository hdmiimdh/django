from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index1(request):
    comment = request.POST.get('comment')
    name = request.POST.get('name')
    lastname = request.POST.get('lastname')
    # slem = comment.split(' ')
    # for i in range(len(slem)):
    #     slem[i] += ' (c) ' + str(name) + ' ' + str(lastname)
    # string = '<br>'.join(slem)
    glas = 'auoieoy'
    sogl = 'qwrtpsdfghjklmnzxcvbnm'
    counter_1 = 0
    counter_2 = 0
    for letter in comment:
        if letter in glas:
            counter_1 += 1
        if letter in sogl:
            counter_2 += 1
    sum = str(counter_1) + '   ' + str(counter_2)
    return HttpResponse(sum)