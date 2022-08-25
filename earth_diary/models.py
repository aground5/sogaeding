from django.db import models

# Create your models here.
class Diary(models.Model) :
    date = models.DateField()					# 날짜
    state = models.CharField(max_length=100)	# 나라
    content = models.TextField()				# 요약내용
    keyword = models.CharField(max_length=100, default="")  # 키워드
    def __str__(self) :
        return self.state
    
class Image(models.Model) :
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    url = models.TextField()            # 이미지 URL 

class News(models.Model) :
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)    # 뉴스 제목
    url = models.TextField()                    # 뉴스 URL

class Heart(models.Model) :
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    userid = models.IntegerField()