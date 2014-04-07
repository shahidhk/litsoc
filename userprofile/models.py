from django.db import models
from django.contrib.auth.models import User
from litsoc.settings import MEDIA_ROOT

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    nick = models.CharField(max_length=100,blank=True)
    contact_number = models.CharField(max_length=10,blank=True)
    USER_TYPE = (('Admin','Admin'),('Core','Core'),('Convener','Convener'),('Coordinator','Coordinator'),('Photograpy Coordinator','Photograpy Coordinator'))
    typ = models.CharField(max_length=20,choices=USER_TYPE)
    assigned = models.BooleanField(default = False)
    HOSTEL = [('Alakananda',"Alakananda"),('Brahmaputra',"Brahmaputra"),('Cauvery',"Cauvery"),('Ganga',"Ganga"),('Godavari',"Godavari"),('Jamuna',"Jamuna"),('Krishna',"Krishna"),('Mahanadhi',"Mahanadhi"),('Mandakini',"Mandakini"),('Narmada',"Narmada"),('Pampa',"Pampa"),('Saraswathi',"Saraswathi"),('Sarayu',"Sarayu"),('Sharavati',"Sharavati"),('Sindhu',"Sindhu"),('Tamiraparani',"Tamiraparani"),('Tapti',"Tapti")]
    hostel = models.CharField(max_length=50,choices=HOSTEL)
    avatar = models.ImageField(upload_to='avatar',default=MEDIA_ROOT[0]+'/avatar/default.jpg')

    def __unicode__(self):
        ret=(self.user.first_name + ' ' + self.user.last_name)
        if not ret.isspace():
            return ret
        else:
            return self.user.username

