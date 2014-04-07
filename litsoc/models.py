from django.db import models
from userprofile.models import UserProfile

class Comment(models.Model):
    comment = models.TextField(max_length=40000)
    by = models.ForeignKey(UserProfile,related_name='comment_by',blank=True,null=True)
    anonymous = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.comment

class PhotoModel(models.Model):
    image = models.ImageField(upload_to="%Y/%m/%d/")
    name = models.CharField(max_length=100,default="")
    desc = models.CharField(max_length=3000,blank=True)
    by = models.ForeignKey(UserProfile,related_name="photo_by",blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(Comment,related_name='photo_comments',blank=True,null=True)

    def __unicode__(self):
        return self.image

class LinkModel(models.Model):
    link = models.URLField(max_length=300)

    def __unicode__(self):
        return self.link

