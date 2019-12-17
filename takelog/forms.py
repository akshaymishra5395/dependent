from django import forms
from .models import BuidingAccessRole

class BuildAccessRoleAdminForm(forms.ModelForm):
    MY_CHOICES = (
        ('-----', '-------'),
    )
    floor=forms.ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        # receive a tupple/list for custom choices
        super(BuildAccessRoleAdminForm, self).__init__(*args, **kwargs)
        if hasattr(self.instance,'building') :
            tt=((str(x),str(x))for x in range(1, self.instance.building.floors + 1))
            print((tt))
            self.fields['floor'].choices = tt


    def save(self, commit=True):
        m = super(BuildAccessRoleAdminForm, self).save(commit=False)
        # do custom stuff
        data1 = self.cleaned_data.get('building','')
        data2 = self.cleaned_data.get('floor','')
        if commit:
            m.save()
        return m

     
    
    # class Meta:
    #     model = BuidingAccessRole
    #     fields= ('name','building','fl')