from django.db import models
from clubs.models import Club
from litsoc.models import PhotoModel,LinkModel
from userprofile.models import UserProfile

class Venue(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Event(models.Model):
    club = models.ForeignKey(Club,related_name='events',blank = True,null = True)
    name = models.CharField(max_length=200)
    time = models.DateTimeField(blank=True,null=True)
    oneliner = models.CharField(max_length=200,blank=True)
    venue = models.ManyToManyField(Venue,related_name='event_venue',blank = True,null=True)
    typ = models.CharField(choices=(('team','Inter Hostel Team Event'),('hostel','Hostel Event')), max_length = 50)
    description = models.CharField(max_length=40000,blank = True)
    coords = models.ManyToManyField(UserProfile,related_name='coord',blank = True) 
    photo_coord = models.ManyToManyField(UserProfile,related_name='ph_coord',blank = True,null=True)
    created_by = models.ForeignKey(UserProfile,related_name='edited_by')
    images = models.ManyToManyField(PhotoModel,related_name="image_event",blank=True,null=True)
    cover = models.ForeignKey(PhotoModel,related_name='cover_event',blank=True,null=True)
    approved = models.BooleanField(default = False)
    links = models.ManyToManyField(LinkModel,related_name='event_links',blank=True,null=True)

    def __unicode__(self):
        return self.name
