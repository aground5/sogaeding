from datetime import date
from django.shortcuts import render, get_object_or_404

from .models import Diary

# Create your views here.
def index(request) :
    diary_list = Diary.objects.filter(date=date.today())
    context = {'diary_list': diary_list}
    return render(request, 'earth_diary/diary_list.html', context)

def index2(request) :
    diary_list = Diary.objects.filter(date=date.today())
    context = {'diary_list': diary_list}
    return render(request, 'earth_diary/question_list.html', context)

def detail(request, diary_id) :
    diary = get_object_or_404(Diary, pk=diary_id)
    
    context = {
        'diary': diary,
    }
    return render(request, 'earth_diary/diary_detail.html', context)

def test(request) :
    return render(request, 'test.html', {})