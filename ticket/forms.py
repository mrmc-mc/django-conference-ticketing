from django import forms
from . import models


class TicketForm(forms.ModelForm):
    fullname = forms.CharField(label='نام و نام خانوادگی',required=True,widget=forms.TextInput(attrs={'placeholder': '...', 'id':'name',
                                                                        "aria-describedby":"validationTooltipUsernamePrepend",
                                                                        'id':'validationTooltipUsername', "type":"text",
                                                                        'class':'form-control text-center'}),min_length=2,
                                                                        max_length=150)
                                                    
    mobile = forms.CharField(label='شماره همراه',required=True,widget=forms.TextInput(attrs={'placeholder': '...', 'id':'mobile',
                                                                        "aria-describedby":"validationTooltipUsernamePrepend", "type":"text",
                                                                        'class':'form-control text-center'}),min_length=2,
                                                                        max_length=50)
                                                    
    uniid = forms.CharField(label='شماره دانشجویی',required=True,widget=forms.TextInput(attrs={'placeholder': '...', 'id':'uniid',
                                                                        "aria-describedby":"validationTooltipUsernamePrepend", "type":"text",
                                                                        'class':'form-control text-center'}),min_length=2,
                                                                        max_length=50)

    entered = forms.CharField(label='سال ورود',required=True,widget=forms.TextInput(attrs={'placeholder': '...', 'id':'entered',
                                                                        "aria-describedby":"validationTooltipUsernamePrepend", "type":"text",
                                                                        'class':'form-control text-center'}),min_length=2,
                                                                        max_length=50)                                                        

    course = forms.CharField(label='رشته تحصیلی',required=True,widget=forms.TextInput(attrs={'placeholder': '...', 'id':'course',
                                                                        "aria-describedby":"validationTooltipUsernamePrepend", "type":"text",
                                                                        'class':'form-control text-center'}),min_length=2,
                                                                        max_length=50)


    bed = forms.CharField(label='رشته تحصیلی',required=False,widget=forms.TextInput(attrs={'placeholder': '...', 'id':'bed',
                                                                        "aria-describedby":"validationTooltipUsernamePrepend", "type":"text",
                                                                        'class':'form-control text-center'}),min_length=2,
                                                                        max_length=50)
                                                            
    submited = forms.CharField(label='رشته تحصیلی',required=False,widget=forms.TextInput(attrs={'placeholder': '...', 'id':'submited',
                                                                        "aria-describedby":"validationTooltipUsernamePrepend", "type":"text",
                                                                        'class':'form-control text-center'}),min_length=2,
                                                                        max_length=50)

    class Meta:
        model = models.Ticket
        exclude = ('created_at','invitecode',)