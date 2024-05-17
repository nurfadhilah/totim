from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name="index"),
path('newmentor', views.newmentor, name="newmentor"),
path('newstudent', views.newstudent, name="newstudent"),

path('update/<str:stuid>', views.update, name="update"),
path('update/updatedata/<str:stuid>', views.updatedata, name="updatedata"),

path('delete/<str:stuid>', views.delete, name="delete"),
path('delete/deletedata/<str:stuid>', views.deletedata, name="deletedata"),

path('searchpage', views.searchpage, name="searchpage"),
]
