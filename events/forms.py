from django import forms
from models import Event,Venue
from django_summernote.widgets import SummernoteWidget
from userprofile.models import UserProfile
from clubs.models import Club
from django_select2 import *
from fields import *
VENUE = Venue.objects.all()

class CreateEventForm(forms.ModelForm):
    cover = forms.ImageField(required=False)
    venue = ModelSelect2MultipleField(queryset=VENUE,required=False)
    coords = widgets.Select2MultipleWidget(),
    print coords
    coords[0].choices = UserProfile.objects.filter(typ='Coordinator')

    class Meta:
        model = Event
        fields = ['name','oneliner','venue','club','typ','description','coords'] 
        widgets = {
            'description':SummernoteWidget(),
            # 'venue':widgets.Select2MultipleWidget(),
            'club':widgets.Select2Widget(),
        }


    def __init__(self,*args,**kwargs):
        super(CreateEventForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            if field not in ['cover','coords','club','venue','description']:
                self.fields[field].widget.attrs.update({'class':'form-control'})

class EditEventForm(forms.ModelForm):
    cover = forms.ImageField(required=False)
    venue = ModelSelect2MultipleField(queryset=VENUE,required=False)
    class Meta:
        model = Event
        fields = ['name','oneliner','venue','club','typ','description','coords'] 
        widgets = {
            'description':SummernoteWidget(),
            # 'venue':widgets.Select2MultipleWidget(),
            'club':widgets.Select2Widget(),
            'coords':widgets.Select2MultipleWidget(),
        }

    def __init__(self,*args,**kwargs):
        super(EditEventForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            if field not in ['cover','coords','club','venue','description']:
                self.fields[field].widget.attrs.update({'class':'form-control'})

class AddVenueForm(forms.Form):
    name = SelfMultiChoices()
