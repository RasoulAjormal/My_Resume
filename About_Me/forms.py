# from django import forms
#
# from About_Me.models import ContactModel
#
#
# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = ContactModel
#         fields = '__all__'
#         widgets = {
#             'FullName': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'FullName'}),
#             'CompanyName': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'CompanyName'}),
#             'Subject': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Title'}),
#             'EmailAddress': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
#             'Message': forms.Textarea(attrs={'class': "form-control", 'placeholder': 'Message'}),
#         }
