
from django import forms
from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple
from .models import Need, HelpCenter


class HelpCenterForm(ModelForm):
    class Meta:
        model = HelpCenter
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HelpCenterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        

        # Also, making 'needs' (which is M2M field) a choicefield
        self.fields['needs'].widget=CheckboxSelectMultiple()
        self.fields['needs'].queryset=Need.objects.all()