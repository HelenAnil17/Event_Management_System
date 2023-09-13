from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from .forms import EventappForm
# Create your views here.

def index(request):
    events = Event.objects.all()
    context = {
        'events' : events
    }
    return render(request,'eventapps/index.html',context)

def eventdetail(request,pk):
   

    event_single= Event.objects.get(pk=pk)
    form = EventappForm()
    if request.method == 'POST':
        form = EventappForm(request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.event = event_single
            applicant.save()
    context = {
        'events' : event_single,
        'form' : form
    }
    return render(request,'eventapps/event.html',context)
