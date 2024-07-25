
from django.urls import path
from blog_App import views



urlpatterns = [
   path('', views.index, name="index"),
   #path('insert', views.insertData, name="insertData"),
   #path('update', views.updateData, name="updateData"),
   #path('insert', views.deleteData, name="deleteData"),

   
]
