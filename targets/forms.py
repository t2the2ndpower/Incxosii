from django import forms

from .models import Target, Target_Assignment


class Create_Target_Form(forms.ModelForm):
    target_title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={"placeholder": "Target Title"}
        )
    )
    target_description = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
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
            'target_ownerID',
            'target_image'
        ]


class Create_Assignment_Form(forms.ModelForm):
    assignment_name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={"placeholder": "Assignment Name"}
        )
    )
    assignment_description = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                "placeholder": "Assignment Description",
                "rows": 20,
                "cols": 75
            }
        )
    )

    class Meta:
        model = Target_Assignment
        fields = [
            'assignment_name',
            'assignment_description',
            'assignment_due_date',
            'assignment_number',
            'target_assignmentID',
            'assignment_created_by',
            'related_targetID'
        ]
    #assignment_duration = forms.DurationField()
