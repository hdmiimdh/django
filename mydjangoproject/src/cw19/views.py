from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def comment_add(request):
    if request.method == 'GET':
        return render(request, 'comment_add.html')
    elif request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        comment = request.POST.get('comment')
        result = '{} {} {} {}'.format(firstname, lastname, age, comment)
        print(result)
        return render(request, 'comment_add.html')
    return HttpResponse('Wrong request method')
