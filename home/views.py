from django.shortcuts import *
from django.template import RequestContext
import datetime
from clubs.models import MusicRoomSlot

def get_date_list():
    base = datetime.date.today()
    return [ base + datetime.timedelta(days=x) for x in range(1,8) ]

def get_book_array(date_array):
    slot_array = []
    for date in date_array:
        temp_slot_array=[]
        booked = MusicRoomSlot.objects.filter(date = date)
        for slot in range(1,5):
            try:
                temp_slot_array.append(booked.get(slot=slot))
            except:
                temp_slot_array.append(False)
        slot_array.append(temp_slot_array)
    return slot_array    

def home(request):
    to_return={
    
    }
    return render_to_response("home/home.html",to_return,context_instance=RequestContext(request))
