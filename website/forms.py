from django import forms
from website.models import Contact,NewsLetter
from django.forms import ModelForm
from captcha.fields import CaptchaField
# class ContactForm(forms.Form):
#     name = forms.CharField(label="Name", max_length=100)
#     email = forms.EmailField(label="Email", max_length=100)
#     subject = forms.CharField(widget=forms.Textarea,label="subject", max_length=100)
#     message = forms.CharField(widget=forms.Textarea,label="message", max_length=100)
# class ArticleForm(ModelForm):
#      class Meta:
#         model = Contact
#         fields = "__all__"
class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your name',
                'class': 'common-input mb-20 form-control',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Enter your name'",
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email address',
                'class': 'common-input mb-20 form-control',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Enter email address'",
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Enter subject',
                'class': 'common-input mb-20 form-control',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Enter subject'",
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Enter Message',
                'class': 'common-textarea form-control',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Enter Message'",
            }),
        }
class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = "__all__"
