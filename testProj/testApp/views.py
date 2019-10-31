from django.shortcuts import render
from .forms import TimelineForm
from .models import Episode, Timeline
import json
import os
from django.conf import settings

# Create your views here.

# def timeline_view(request):

#     return render(request, 'submit')

def home(request):
    return render(request, 'home.html')

def submit_story(request):
    form = TimelineForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TimelineForm()
        file_path = os.path.join(settings.BASE_DIR, 'static/dataTL.json')
        tl = Timeline.objects.last()
        with open(file_path, 'r', errors='ignore', encoding="utf8") as roar:
            new = json.load(roar)
            new['events'].append({
            "media": {
                "url": str(tl.media_url), 
                "caption": "", 
                "credit": ""
            }, 
            "start_date": {
                "month": str(tl.event_date.month), 
                "day": str(tl.event_date.day), 
                "year": str(tl.event_date.year)
            }, 
            "text": {
                "headline": tl.headline, 
                "text": tl.text
            }
            })
            with open(file_path, 'w', errors='ignore', encoding="utf8") as hehe:
                json.dump(new, hehe)
            return render(request, 'tl_success.html')  
        
    context = {'form' : form}
    return render(request, 'submit_story.html', context)  
    
def playlists(request):
    return render(request, 'playlists.html')

def episodes(request):
    episodes_list = Episode.objects.order_by('-pub_date')
    context = {'episodes_list' : episodes_list}
    return render(request, 'episodes.html', context)  

def voicenote(request):
    if(request.POST):
            return render(request, 'vn_success.html')  
    return render(request, 'voicenote.html')  