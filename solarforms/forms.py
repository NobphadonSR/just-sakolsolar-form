from django import forms
from .models import SolarDatas

class SolarDataForms(forms.ModelForm):
    preferred_contact_time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'class': 'form-control',
            'type': 'time'
        }),
        required=False,
        label='เวลาที่สะดวกให้ติดต่อ'
    )
    
    preferred_survey_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        }),
        required=False,
        label='วันที่สะดวกให้สำรวจหน้างาน'
    )

    class Meta:
        model = SolarDatas
        fields = [
            'location_name',
            'contact_name',
            'phone_number',
            'preferred_contact_time',
            'preferred_survey_date',
            'latest_electric_bill',
            'additional_info'
        ]
        widgets = {
            'location_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'latest_electric_bill': forms.NumberInput(attrs={'class': 'form-control'}),
            'additional_info': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }