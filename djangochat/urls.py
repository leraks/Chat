from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name="home"),
    path('<str:pk>/', views.room, name="room"),
    path('checkview', views.checkview, name="checkview"),
    path('send', views.send, name="send"),
    path('getMessages/<str:pk>/', views.getMessages, name="getMessages"),
    path('delete_html/<int:id>/', views.delete_html, name="delete_html"),

]