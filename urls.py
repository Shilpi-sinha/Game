from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('quest', views.quest, name='quest'),
    path('quest2', views.quest2, name='quest2'),
    path('summ', views.summ, name='summ'),
    path('index', views.index, name='index')
 

]
