from django.db import models
from userprofile.models import UserProfile
from litsoc.models import PhotoModel,LinkModel

class Club(models.Model):
    name = models.CharField(max_length=200)
    oneliner = models.CharField(max_length=200,blank=True)
    about = models.CharField(max_length=20000,blank = True)
    convener = models.ManyToManyField(UserProfile,related_name = "convener",blank=True,null=True)
    cover = models.ForeignKey(PhotoModel,related_name="cover_club",blank=True,null=True,on_delete=models.SET_NULL)
    images = models.ManyToManyField(PhotoModel,related_name="image_club",blank=True,null=True)
    links = models.ManyToManyField(LinkModel,related_name='clubs_links',blank=True,null=True)
    approved = models.BooleanField(default = False)

    def __unicode__(self):
        return self.name 

class MusicRoomTeam(models.Model):
    leader_name = models.CharField(max_length=100)
    leader_rollno = models.CharField(max_length=10)
    musiccardid = models.CharField(max_length=100)
    hostel = models.CharField(choices=UserProfile.HOSTEL,max_length=100)
    members = models.CharField(blank=True,max_length=1000)

    def __unicode__(self):
        return self.leader_name + '|' + self.leader_rollno

class MusicRoomSlot(models.Model):
    date = models.DateField()
    SLOT_CHOICES = ((1,'Slot 1 : 5:00pm - 7:00pm'),(2,'Slot 2 : 7:00pm - 9:00pm'),(3,'Slot 3 : 9:00pm - 11:00pm'),(4,'Slot 4 : 11:00pm - 1:00am'))
    slot = models.IntegerField(choices=SLOT_CHOICES,default=1)
    teams = models.ManyToManyField(MusicRoomTeam,blank=True,null=True,related_name='slot')
    timestamp = models.CharField(max_length=2000,blank=True)
    approved_team = models.ForeignKey(MusicRoomTeam,blank=True,null=True,related_name='slot_name')

    def __unicode__(self):
        ret = ''
        for i in self.teams.all():
            i=i.musiccardid+';'
            ret+=i
        return ret