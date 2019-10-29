from django.shortcuts import render
from .forms import TimelineForm
from .models import Episode

# Create your views here.

# def timeline_view(request):

#     return render(request, 'submit')

def home(request):
    return render(request, 'home.html')

def submit_story(request):
    form = TimelineForm(request.POST or None)
    if form.is_valid():
        form.save()
        form.TimelineForm()

    context = {'form' : form}
    return render(request, 'submit_story.html', context)  
    
def playlists(request):
    return render(request, 'playlists.html')

def episodes(request):
    episodes_list = Episode.objects.order_by('-pub_date')
    context = {'episodes_list' : episodes_list}
    return render(request, 'episodes.html', context)  

def voicenote(request):
    return render(request, 'voicenote.html')  