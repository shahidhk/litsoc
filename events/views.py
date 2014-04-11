from django.shortcuts import *
from forms import CreateEventForm,AddVenueForm,EditEventForm
from django.core.urlresolvers import reverse
from django.contrib import auth,messages
from models import Event,Venue
from userprofile.models import UserProfile
from litsoc.models import PhotoModel
from clubs.models import Club

def event_main(request):
    event_list = Event.objects.all()
    to_return = {
        'event_list' : event_list,
    }
    return render_to_response("events/event_main.html",to_return,context_instance=RequestContext(request))

def create_event(request):
    form = CreateEventForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        event = form.save(commit=False)
        photo = PhotoModel()
        photo.image = form.cleaned_data['cover']
        photo.name = form.cleaned_data['name']
        desc = '%s cover photo' %(form.cleaned_data['name'])
        photo.desc = desc
        photo.save()
        event.cover = photo
        event.created_by = request.user.get_profile()
        try:
            event.club = form.cleaned_data['club']
            event.save()
        except:
            pass
        event=form.save_m2m()
        messages.success(request,'Created event successfully')
        return HttpResponseRedirect(reverse('event_main'))
    title = "Create Event"
    return_url = reverse('create_event')
    to_return={
        'form' : form,
        'title' : title,
        'return_url' : return_url,
        'button' : 'Create' ,
    }
    return render(request,'form1.html',to_return,context_instance=RequestContext(request))

def add_venue(request):
    form = AddVenueForm(request.POST or None)
    if form.is_valid():
        for venue in form.cleaned_data['name']:
            Venue.objects.create(name=venue)
        messages.success(request,'Venues successfully added')
        HttpResponseRedirect(reverse('event_main'))
    title = "Add Venue"
    return_url = reverse('add_venue')
    to_return={
        'form' : form,
        'title' : title,
        'return_url' : return_url,
        'button' : 'Add' ,
    }
    return render(request,'form1.html',to_return,context_instance=RequestContext(request))

def edit_event(request,event_id):
    event = Event.objects.get(id=int(event_id))
    form = EditEventForm(request.POST or None,request.FILES or None,instance=event) 
    if form.is_valid():
        event = form.save(commit=False)
        if form.cleaned_data['cover']:
            photo = PhotoModel()
            photo.image = form.cleaned_data['cover']
            photo.name = form.cleaned_data['name']
            desc = '%s cover photo' %(form.cleaned_data['name'])
            photo.desc = desc
            photo.save()
            event.cover = photo
        try:
            event.club = form.cleaned_data['club']
            event.save()
        except:
            pass
        event=form.save_m2m()
        messages.success(request,'Details successfully updated')
        HttpResponseRedirect(reverse('event_main'))
    title = "Edit Event"
    # return_url = reverse('edit_event',args={int(event_id)},)
    return_url =""
    to_return={
        'form' : form,
        'title' : title,
        'return_url' : return_url,
        'button' : 'Update' ,
    }
    return render(request,'form1.html',to_return,context_instance=RequestContext(request))

def delete_event(request,event_id):
    event = Event.objects.get(id=int(event_id))
    for coord in event.coords.all():
        coord.assigned = False
        coord.save()
    event.delete()
    messages.success(request,'Event removed successfully')
    return HttpResponseRedirect(reverse('event_main'))
