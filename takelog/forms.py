from django import forms
from .models import BuidingAccessRole
from .models import Building
class BuildAccessRoleAdminForm(forms.ModelForm):
    MY_CHOICES = (
        ('-----', '-------'),
    )
    floor=forms.ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        # receive a tupple/list for custom choices
        super(BuildAccessRoleAdminForm, self).__init__(*args, **kwargs)
        if hasattr(self.instance,'building') :
            if hasattr(self,'cleaned_data') :
                self.instance.building=self.cleaned_data.get('building')
            self.fields['floor'].choices = ((str(x),str(x))for x in range(1, self.instance.building.floors + 1))

        if hasattr(self,'data') and self.data != {} :
            try:
                building = Building.objects.get(pk=self.data['building'])
            except e:
                print(e)
            # if hasattr(self,'cleaned_data') :
            #     self.instance.building=self.cleaned_data.get('building')
            #     # self.instance.floor=self.cleaned_data.get('floor')
            self.fields['floor'].choices = ((str(x),str(x))for x in range(1, building.floors + 1))


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