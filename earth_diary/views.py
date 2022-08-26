from datetime import date as module_date, timedelta
from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Diary, Heart

# Create your views here.
def index(request) :
    diary_list = Diary.objects.filter(date=module_date.today())
    context = {
        'diary_list': diary_list,
        'prev_date': module_date.strftime(module_date.today() - timedelta(days=1), '%Y-%m-%d'),
        'next_date': module_date.strftime(module_date.today() + timedelta(days=1), '%Y-%m-%d'),
        'userid': request.user.id,
    }
    context['today'] = "오늘"
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
        'next_date': module_date.strftime(date + timedelta(days=1), '%Y-%m-%d'),
        'userid': request.user.id,
    }
    if (date == module_date.today()) :
        context['today'] = "오늘"
    else :
        context['today'] = date
    return render(request, 'earth_diary/diary_list_2.html', context)

def detail(request, diary_id) :
    diary = get_object_or_404(Diary, pk=diary_id)
    
    context = {
        'diary': diary,
    }
    return render(request, 'earth_diary/diary_detail.html', context)

def api_heart(request, diary_id, userid) :
    diary = get_object_or_404(Diary, pk=diary_id)
    if (userid != request.user.id) :
        raise Http404("login first")
    else :
        filterargs = {
            "diary__exact": diary_id,
            "userid__exact": request.user.id,
        }
        heart = Heart.objects.filter(**filterargs)
        if (heart.count() == 0) :
            diary.heart_set.create(userid=request.user.id)
            data = {
                "status": "hearted"
            }
            return JsonResponse(data=data)
        else :
            heart.delete()
            data = {
                "status": "dehearted"
            }
            return JsonResponse(data=data)

def api_screenshot(request):
    if request.method == "POST":
        print(request.POST)
    return JsonResponse("")
        
def test(request) :
    return render(request, 'test.html', {})