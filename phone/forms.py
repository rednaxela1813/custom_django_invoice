from django import forms
from .models import Phone


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = "__all__"
        widgets = {
            "phone": forms.TextInput(attrs={"placeholder": "Enter phone number"}),
            "type": forms.Select(attrs={"placeholder": "Enter phone type"}),
            "owner_privat": forms.Select(attrs={"placeholder": "Enter owner privat"}),
            "owner_legal": forms.Select(attrs={"placeholder": "Enter owner legal"}),
            "old_number": forms.CheckboxInput(attrs={"placeholder": "Enter old number"}),
        }