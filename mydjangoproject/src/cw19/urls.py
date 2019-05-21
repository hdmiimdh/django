from django.urls import path, include
from cw19.views import comment_add

urlpatterns = [
    path('add/', comment_add),
]
