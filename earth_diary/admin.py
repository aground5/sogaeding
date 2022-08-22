from django.contrib import admin
from earth_diary.models import News, Image, Diary

# Register your models here.
admin.site.register(Diary)
admin.site.register(Image)
admin.site.register(News)