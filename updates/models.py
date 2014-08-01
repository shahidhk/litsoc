from django.db import models
from events.models import Event
from clubs.models import Club
from litsoc.models import PhotoModel,LinkModel
from userprofile.models import UserProfile

class Update(models.Model):
    name = models.TextField(max_length=100)
    oneliner = models.CharField(max_length=200,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True,null=True)
    update_by = models.ForeignKey(UserProfile,related_name='update_by')
    desc = models.TextField(max_length = 40000,blank = True)
    event = models.ForeignKey(Event,related_name='event_update',null=True,blank=True)
    club = models.ForeignKey(Club,related_name='club_update',null=True,blank=True)
    approved = models.BooleanField(default = False)
    cover = models.ForeignKey(PhotoModel,related_name='cover_update',blank=True,null=True)
    images = models.ManyToManyField(PhotoModel,related_name="update_images",blank=True,null=True)
    links = models.ManyToManyField(LinkModel,related_name='links_update',blank=True,null=True)

    class Meta:
        ordering = ['-updated_at']

    def __unicode__(self):
        return self.name

