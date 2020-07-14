from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Nome", widget=forms.TextInput(attrs={'placeholder': 'Digite o seu nome'}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'Digite o seu endereço de email'}))
    content_message = forms.CharField(label="Mensagem", widget=forms.Textarea(attrs={'placeholder': 'Digite sua mensagem'}))
