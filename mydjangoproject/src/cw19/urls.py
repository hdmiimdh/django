from django.urls import path, include
from cw19.views import comment_add

urlpatterns = [
    path('comment_add/', comment_add, name='comment_add'),
]
