from django import forms
from .models import *

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = '__'
#         widgets = {
#             'Password': forms.PasswordInput(),  # Use PasswordInput widget for password
#         }
class PointageForm(forms.Form):
    CHOICES = [
        ('T', 'T'),
        ('R', 'R'),
        ('1', '1'),
        ('I', 'I'),
        ('2', '2'),
        ('M', 'M'),
        ('A', 'A'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('C', 'C'),
        ('Cr', 'Cr'),
        
    ]

    dropdown_menu = forms.ChoiceField(choices=CHOICES)

class partnerForm(forms.ModelForm):
    class Meta:
        model=Partner
        exclude=['id_employe']
        
    def __init__(self, *args, **kwargs):
        super(partnerForm,self).__init__(*args, **kwargs)
        for field_names,field in self.fields.items():
            field.required=False
    

class EmployeForm(forms.ModelForm):
    class Meta:
        model=Employe
        exclude = ['id','unite','active','refund_total','refund_by_month']
    
    def __init__(self, *args, **kwargs):
        super(EmployeForm,self).__init__(*args, **kwargs)
        for field_names,field in self.fields.items():
            field.required=False
        self.fields['name'].required = True
        self.fields['last_name'].required = True
        '''self.fields['date_of_birth'].requried = True
        self.fields['place_of_birth'].required = True
        self.fields['phone'].required = True
        self.fields['father_name'].required = True
        self.fields['mother_name'].required = True
        self.fields['function'].required = True
        self.fields['position'].required = True'''
        


class EmployeFormForDg(forms.ModelForm):
    class Meta:
        model=Employe
        exclude = ['id','refund_total','refund_by_month']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','required':True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','required':True}),
            #'adresse': forms.TextInput(attrs={'class': 'form-control','required':True}),
            #'recruitment_date': forms.DateInput(attrs={'class': 'form-control','required':True}),
            #'familiy_situation': forms.TextInput(attrs={'class': 'form-control','required':True}),
            #'Nbr_Enfants': forms.NumberInput(attrs={'class': 'form-control','required':True}),
        }
    
    def __init__(self, *args, **kwargs):
        super(EmployeFormForDg,self).__init__(*args, **kwargs)
        for field_names,field in self.fields.items():
            field.required=False
        self.fields['name'].required = True
        self.fields['last_name'].required = True
        '''self.fields['date_of_birth'].requried = True
        self.fields['place_of_birth'].required = True
        self.fields['phone'].required = True
        self.fields['father_name'].required = True
        self.fields['mother_name'].required = True
        self.fields['function'].required = True
        self.fields['position'].required = True
        self.fields['unite'].required = True'''
        

class remboursementForm(forms.ModelForm):
    class Meta:
        model=Employe
        fields=['refund_total']
        widgets = {
            'refund_total': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
class diplomesForm(forms.ModelForm):
    class Meta:
        model=Diplome
        exclude=['id_employe']

class childForm(forms.ModelForm):
    class Meta:
        model=Child
        exclude=['id_employe']
        
    def __init__(self, *args, **kwargs):
        super(childForm,self).__init__(*args, **kwargs)
        for field_names,field in self.fields.items():
            field.required=False


