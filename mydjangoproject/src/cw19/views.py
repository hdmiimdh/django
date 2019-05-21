from django.shortcuts import render
from django.http import HttpResponse
from cw19.forms import PostForm

# Create your views here.

def comment_add(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'comment_add.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.data
            firstname = data.get('firstname')
            lastname = data.get('lastname')
            age = data.get('age')
            comment = data.get('comment')
            result = '{} {} {} {}'.format(firstname, lastname, age, comment)
            context = {'form': PostForm()}
            print(result)
            return render(request, 'comment_add.html',context)
        else:
            errors = form.errors
            return HttpResponse(errors)
    return HttpResponse('Wrong request method')
