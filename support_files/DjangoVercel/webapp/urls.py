from . import views

from django.urls import path
urlpatterns = [
    path('', views.home, name='home'),
   # path('show_result/', views.show_result, name="show_result")
]
