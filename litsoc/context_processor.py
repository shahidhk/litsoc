from clubs.models import MusicRoomSlot
from home.views import get_date_list,get_book_array

def litsoc_context(request):
    response = {'book_list':'',}        
    date_array = get_date_list()
    book_list = get_book_array(date_array)
    response['book_list'] = zip(date_array,book_list)
    return response