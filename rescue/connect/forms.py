
from django import forms
from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple
from .models import Need, HelpCenter, SomeoneNeedsHelp, Help


class HelpCenterForm(ModelForm):
    name = forms.CharField(label='Name of foodbank/help center', widget=forms.TextInput(attrs={'placeholder': 'Example: Shanti Chowk Food Bank'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Example: Shanti Chowk, Biratnagar'}))
    class Meta:
        model = HelpCenter
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HelpCenterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self.fields['needs'].widget=CheckboxSelectMultiple()
        self.fields['needs'].queryset=Need.objects.all()


class NeedHelpForm(ModelForm):
    name = forms.CharField(label='Your name')
    address = forms.CharField(label='Address where help is needed', widget=forms.TextInput(attrs={'placeholder': 'Example: Bhimsengola, Baneshwor'}))
    contact = forms.CharField(label='Your contact')
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Example: A family of 5 members needs help with food.'}))
    number_of_people = forms.CharField(label='Number of people who needs help')
    class Meta:
        model = SomeoneNeedsHelp
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NeedHelpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self.fields['needs'].widget=CheckboxSelectMultiple()
        self.fields['needs'].queryset=Need.objects.all()
    

class HelpForm(ModelForm):
    name = forms.CharField(label='Your name')
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Example: Shanti Chowk, Biratnagar'}))
    class Meta:
        model = Help
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HelpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self.fields['needs'].widget=CheckboxSelectMultiple()
        self.fields['needs'].queryset=Need.objects.all()