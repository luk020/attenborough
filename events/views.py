from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Show, Event, EventForm

# Create your views here.
def index(request):
    return render(request, "events/index.html", {
        "shows": Show.objects.all().order_by('-year')
    })

def show(request, show_id):
    show = Show.objects.get(pk=show_id)
    form = EventForm(initial={'show_id': show.id})
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "events/show.html", {
        "show": show,
        "events": show.events.all().order_by('episode'),
        "form": form
    })