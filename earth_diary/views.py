from datetime import date as module_date, timedelta
from django.shortcuts import render, get_object_or_404

from .models import Diary

# Create your views here.
def index(request) :
    diary_list = Diary.objects.filter(date=module_date.today())
    context = {
        'diary_list': diary_list,
        'prev_date': module_date.strftime(module_date.today() - timedelta(days=1), '%Y-%m-%d'),
        'next_date': module_date.strftime(module_date.today() + timedelta(days=1), '%Y-%m-%d')
    }
    context['today'] = "Today"
    return render(request, 'earth_diary/diary_list_2.html', context)

def index2(request) :
    diary_list = Diary.objects.filter(date=module_date.today())
    context = {'diary_list': diary_list}
    context = {
        'diary_list': diary_list,
        'prev_date': module_date.strftime(module_date.today() - timedelta(days=1), '%Y-%m-%d'),
        'next_date': module_date.strftime(module_date.today() + timedelta(days=1), '%Y-%m-%d')
    }
    return render(request, 'earth_diary/question_list.html', context)

def bydate(request, date) :
    diary_list = Diary.objects.filter(date=date)
    context = {
        'diary_list': diary_list,
        'prev_date': module_date.strftime(date - timedelta(days=1), '%Y-%m-%d'),
        'next_date': module_date.strftime(date + timedelta(days=1), '%Y-%m-%d')
    }
    if (date == module_date.today()) :
        context['today'] = "Today"
    else :
        context['today'] = module_date.strftime(date, '%Y-%m-%d')
    return render(request, 'earth_diary/diary_list_2.html', context)

def detail(request, diary_id) :
    diary = get_object_or_404(Diary, pk=diary_id)
    
    context = {
        'diary': diary,
    }
    return render(request, 'earth_diary/diary_detail.html', context)

def test(request) :
    return render(request, 'test.html', {})