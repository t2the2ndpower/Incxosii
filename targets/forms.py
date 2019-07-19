from django import forms

from .models import Target



class Create_Target_Form(forms.ModelForm):
    target_title = forms.CharField(
        label = '',
        widget = forms.TextInput(
            attrs = {"placeholder": "Target Title"}
            )
        )
    target_description = forms.CharField(
        label = '',
        widget = forms.Textarea(
            attrs = {
                "placeholder": "Target Description",
                "rows": 20,
                "cols": 75
                }
            )
        )
    
    class Meta:
        model = Target
        fields = [
            'target_title',
            'target_description',
            'targetID',
            'target_ownerID'
        ]





class Create_Assignment_Form(forms.Form):
    assignment_name = forms.CharField(
        label = '',
        widget = forms.TextInput(
            attrs = {"placeholder": "Assignment Name"}
            )
        )
    assignment_description = forms.CharField(
        label = '',
        widget = forms.Textarea(
            attrs = {
                "placeholder": "Assignment Description",
                "rows": 20,
                "cols": 75
                }
        )
    )
    #assignment_duration = forms.DurationField()