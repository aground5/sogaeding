from django.urls import path, register_converter
from datetime import date as module_date
from . import views

app_name = 'earth_diary'

class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return module_date.fromisoformat(value)

    def to_url(self, value):
        return value

register_converter(DateConverter, 'yyyy')

urlpatterns = [
    path('candidate1', views.index, name='index'),
    path('candidate2', views.index2, name='index2'),
    path('date/<yyyy:date>/', views.bydate, name='date'),
    path('<int:diary_id>/', views.detail, name='detail'),
    path('test', views.test, name='test'),
    path('api/heart/<int:diary_id>/<int:userid>', views.api_heart, name="heart")
]
