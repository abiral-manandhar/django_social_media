from django.urls import path
from .views import AddPost, CreateComment

urlpatterns = [

    path('add/', AddPost, name='post'),
    path('create/<int:pk>', CreateComment, name='comment'),

]