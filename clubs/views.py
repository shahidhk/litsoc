from django.shortcuts import *
from forms import CreateClubForm, EditClubForm, MusicClubForm
from django.core.urlresolvers import reverse
from django.contrib import auth,messages
from models import Club,MusicRoomSlot,MusicRoomTeam
from userprofile.models import UserProfile
from litsoc.models import PhotoModel
import datetime
from home.views import get_date_list

def club_main(request):
    club_list = Club.objects.all()
    to_return = {
        'club_list' : club_list,
    }
    return render_to_response("clubs/club_main.html",to_return,context_instance=RequestContext(request))

def create_club(request):
    createclubForm = CreateClubForm(request.POST or None,request.FILES or None)
    if createclubForm.is_valid():
        club = createclubForm.save(commit=False)
        photo = PhotoModel()
        photo.image = createclubForm.cleaned_data['cover']
        photo.name = createclubForm.cleaned_data['name']
        desc = '%s cover photo' %(createclubForm.cleaned_data['name'])
        photo.desc = desc
        photo.save()
        club.cover = photo
        club.save()
        for convener in createclubForm.cleaned_data['convener']:
            club.convener.add(convener)
            convener.assigned=True
            convener.save()
        club.save()
        messages.success(request,'Club successfully created')
        return HttpResponseRedirect(reverse('club_main'))
    title = "Create Club"
    return_url = reverse('create_club')
    to_return={
        'form' : createclubForm,
        'title' : title,
        'return_url' : return_url,
        'button' : 'Create' ,
        'tags' : [],
    }
    return render(request,'form1.html',to_return,context_instance=RequestContext(request))

def edit_club(request,club_id):
    club = Club.objects.get(id=int(club_id))
    conveners = [user.id for user in club.convener.all()]
    if request.POST:
        editclubForm = EditClubForm(request.POST,request.FILES,instance=club)
        if editclubForm.is_valid():
            club = editclubForm.save()
            if editclubForm.cleaned_data['cover']:
                club.images.add(club.cover)
                photo = PhotoModel()
                photo.image = editclubForm.cleaned_data['cover']
                photo.name = editclubForm.cleaned_data['name']
                desc = '%s cover photo' %(editclubForm.cleaned_data['name'])
                photo.desc = desc
                photo.save()
                club.cover = photo
                club.save()
            messages.success(request,'Details successfully saved')
            return HttpResponseRedirect(reverse('club_main'))
    else:
        editclubForm = EditClubForm(instance=club)
        title = "Edit Club"
        return_url = reverse('edit_club',args={int(club_id)},)
        to_return={
            'form' : editclubForm,
            'title' : title,
            'return_url' : return_url,
            'button' : 'Update' ,
        }
        return render(request,'form1.html',to_return,context_instance=RequestContext(request))

def delete_club(request,club_id):
    club = Club.objects.get(id=int(club_id))
    for convener in club.convener.all():
        convener.assigned = False
        convener.save()
    club.delete()
    messages.success(request,'Club removed successfully')
    return HttpResponseRedirect(reverse('club_main'))

def musicroom1(request):
    if request.method == 'POST':
        request.session['_old_post'] = request.POST
        return HttpResponseRedirect(reverse('musicroom2'))
    else:
        # date_array = get_date_list()
        # book_list = get_book_array(date_array)
        to_return={
            # 'book_list':zip(date_array,book_list),
            'title':'Musicroom',
        }
        return render(request,'clubs/musicroom.html',to_return,context_instance=RequestContext(request))

def musicroom2(request):
    old_post = request.session['_old_post']
    date = old_post['date']
    slot = old_post['slot']
    form = MusicClubForm(request.POST or None,initial={'date':date,'slot':int(slot),'slot1':int(slot)})
    if form.is_valid():
        team = form.save(commit=False)
        team.save()
        for member in form.cleaned_data['members']:
            team.members+=member
        team.save()
        date = form.cleaned_data['date']
        slot = form.cleaned_data['slot1']
        try:
            slot = MusicRoomSlot.objects.get(date=date,slot=int(slot))
        except:
            slot = MusicRoomSlot.objects.create(date=date,slot=int(slot))
        slot.teams.add(team)
        messages.success(request,'Request successful')
        request.session['_old_post'] = ''
        return HttpResponseRedirect(reverse('home'))
    return_url = reverse('musicroom2')
    to_return={
        'form' : form,
        'return_url' : return_url,
        'title' : 'Musicclub Reservation-2',
        'button' : 'Book',
    }
    return render_to_response("form1.html",to_return,context_instance=RequestContext(request))

def approval(request):
    date_array = get_date_list()
    if request.method == 'POST':
        for item in request.POST:
            if "date" in item:
                item = item.replace('date','')
                date = item[0]
                item = item[1:]
                item = item.replace('slot','')
                slot = item[0]
                item = item[1:]
                item = item.replace('team','')
                team = item
                item = "date"+date+"slot"+slot
                team = int(request.POST[item]) 
                date=date_array[int(date)-1]
                team = MusicRoomTeam.objects.get(id=int(team))
                slot = MusicRoomSlot.objects.get(date=date,slot=int(slot))
                slot.approved_team = team
                slot.save()
                messages.success(request,'All changes saved')
                try:
                    send_mail('Litsoc Portal : Music Room request approved', email_body , 'saarang@gmail.com',[email], fail_silently=False)
                except:
                    pass
    to_return={
        'title':'Musicroom Approval',
    }
    return render_to_response("clubs/musicroomlist.html",to_return,context_instance=RequestContext(request))

def cancel_musicroom_approval(request,slot_id):
    slot = MusicRoomSlot.objects.get(id=int(slot_id))
    slot.approved_team = None
    slot.save()
    try:
        send_mail('Litsoc Portal : Music Room request cancelled', email_body , 'saarang@gmail.com',[email], fail_silently=False)
    except:
        pass
    messages.success(request,'The reservation has been cancelled')
    return HttpResponseRedirect(reverse('approval'))