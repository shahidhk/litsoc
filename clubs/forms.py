from django import forms
from models import Club,MusicRoomTeam,MusicRoomSlot
from litsoc.models import PhotoModel
from userprofile.models import UserProfile
from django.forms.widgets import SelectMultiple
from django_summernote.widgets import SummernoteWidget
from form_utils.widgets import ImageWidget
from django_select2 import *
from fields import SelfMultiChoices

CONVENERS = UserProfile.objects.filter(typ="convener").filter(assigned=False)

class CreateClubForm(forms.ModelForm):
    cover = forms.ImageField(required=False)
    CONVENERS = UserProfile.objects.filter(typ="convener").filter(assigned=False)
    convener = ModelSelect2MultipleField(queryset=CONVENERS,required=False,label='Conveners')
    class Meta:
        model = Club
        fields = ['name','oneliner','about']
        widgets = {
            'about':SummernoteWidget(),
        }

    def __init__(self,*args,**kwargs):
        super(CreateClubForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            if field not in ['convener','cover','about']:
                self.fields[field].widget.attrs.update({'class':'form-control',})

class EditClubForm(forms.ModelForm):
    cover = forms.ImageField(required=False,help_text='Click only to change the present picture.')

    class Meta:
        model = Club
        fields = ['name','oneliner','about','convener']
        widgets = {
            'about':SummernoteWidget(),
            'convener':widgets.Select2MultipleWidget(),
        }

    def __init__(self,*args,**kwargs):
        super(EditClubForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            if field not in ['convener','cover','about']:
                self.fields[field].widget.attrs.update({'class':'form-control',})
        # self.fields['convener'].queryset = self.fields['convener'].queryset.filter(typ='Convener',assigned=False)

class MusicClubForm(forms.ModelForm):
    members = SelfMultiChoices(required=False)
    date = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    slot = forms.ChoiceField(choices = MusicRoomSlot.SLOT_CHOICES,widget=forms.Select(attrs={'disabled':'disabled'}),required=False)
    slot1 = forms.ChoiceField(choices = MusicRoomSlot.SLOT_CHOICES,widget=forms.HiddenInput())
    class Meta:
        model = MusicRoomTeam
        fields = ['leader_name','leader_rollno','musiccardid','members','hostel','date','slot','slot1']
    def __init__(self,*args,**kwargs):
        super(MusicClubForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            if field not in ['members']:
                self.fields[field].widget.attrs.update({'class':'form-control',})
