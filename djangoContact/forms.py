from django import forms

class contactForm(forms.Form):
    Name=forms.CharField(label="Your name", max_length=50)
    Email=forms.EmailField(label="Your email", max_length=50)
    Message=forms.CharField(label="Message")
