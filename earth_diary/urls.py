from django.urls import path
from . import views

app_name = 'earth_diary'

urlpatterns = [
    path('candidate1', views.index, name='index'),
    path('candidate2', views.index2, name='index2'),
    path('<int:diary_id>/', views.detail, name='detail'),
    path('test', views.test, name='test'),
]
