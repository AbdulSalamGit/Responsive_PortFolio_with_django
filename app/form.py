from django import forms


class ContactForm(forms.Form):
    your_name = forms.CharField(max_length=100, label="Your Name", required=True)
    your_email = forms.EmailField(label="Your Email", required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
