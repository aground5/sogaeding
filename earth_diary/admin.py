from django.contrib import admin
from earth_diary.models import Heart, News, Image, Diary

# Register your models here.
admin.site.register(Diary)
admin.site.register(Image)
admin.site.register(News)
admin.site.register(Heart)