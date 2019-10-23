from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def submit_story(request):
    return render(request, 'submit_story.html')  
    
def playlists(request):
    return render(request, 'playlists.html')

def episodes(request):
    return render(request, 'episodes.html')  

def voicenote(request):
    return render(request, 'voicenote.html')  