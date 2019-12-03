from django.shortcuts import render, redirect
from .forms import TimelineForm, VoicenoteForm
from .models import Episode, Timeline
import json
import os
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


# Create your views here.

# def timeline_view(request):

#     return render(request, 'submit')

def colors(request):
    return render(request, 'colors.html')

def contact(request):
    if request.method == 'POST':
        return render(request, 'cn_success.html')


    return render(request, 'contact.html')

def home(request):
    tl = Timeline.objects.all()
    print(tl)
    file_path = os.path.join(settings.BASE_DIR, 'media/t.json')
    with open(file_path, 'r', errors='ignore', encoding="utf8") as roar:
        new = json.load(roar)
        for event in tl:
            print(event.endDate)
            if event.approved:
                new['events'].append({
                "start_date": {
                    "month": str(event.startDate.month), 
                    "day": str(event.startDate.day), 
                    "year": str(event.startDate.year)
                },
                "text": {
                    "headline": event.title, 
                    "text": "<p style=\"color: #DC5600\">Submitted by: " + event.name + "</p>" + event.story
                }
                })
                if event.media_url:
                    print("nooooooo")
                    new['events'][len(new['events'])-1]["media"]= {
                        "url": str(event.media_url),
                        "caption": "",
                        "credit": ""
                        }
                    if event.caption:
                        new['events'][len(new['events'])-1]["media"]["caption"] = event.caption
                    if event.credit:
                        new['events'][len(new['events'])-1]["media"]["credit"] = event.credit
                if event.endDate:
                    new['events'][len(new['events'])-1]["end_date"]= {
                    "month": str(event.endDate.month), 
                    "day": str(event.endDate.day), 
                    "year": str(event.endDate.year)
                    }
        gen_path = os.path.join(settings.BASE_DIR, 'media/2.json')
        with open(gen_path, 'w', errors='ignore', encoding="utf8") as hehe:
            json.dump(new, hehe)
    return render(request, 'home.html')

def submit_story(request):
    if request.method == 'POST':
        form = TimelineForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'tl_success.html', {'name' : form.data["name"]})
    else:
        form = TimelineForm()  
        
    return render(request, 'submit_story.html', {'form' : form})  
    
def playlists(request):
    return render(request, 'playlists.html')

def episodes(request):
    episodes_list = Episode.objects.order_by('-pub_date')
    context = {'episodes_list' : episodes_list}
    return render(request, 'episodes.html', context)  

@csrf_exempt
def vn_success(request):
    if request.method == 'POST':
        print(request.body)
        form = VoicenoteForm(request.POST, request.FILES)
        print(form)
        # email = EmailMessage(
        # subject = 'Your Voicenote from KRCL',
        # body = 'Hello, ' + request.POST['name'] + "\n\nAttached is your Voicenote!\n\nThank you for taking the time to test this feature!",
        # from_email = 'face151@windowslive.com',
        # to = [request.POST['email']]
        # )
        # upload_file = request.FILES['audio']
        # content = upload_file.read()
        # email.attach(request.POST['name'] + ".mp3", content, 'audio/mp3')
        # email.send(fail_silently=False)
        # return JsonResponse({
        #     'success': True,
        #     'url': 'success',
        # })
        return render(request, 'vn_success.html', {'name' : form.data["name"]})

    return render(request, 'vn_success.html')

@csrf_exempt
def voicenote(request):
    return render(request, 'voicenote.html')  