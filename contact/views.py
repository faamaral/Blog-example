from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage


def contact(request):
    send = False

    form = ContactForm(request.Post or None)
    if form.is_valid():
        name = request.Post.get('name', '')
        email = request.Post.get('email', '')
        content_message = request.Post.get('content_message', '')
        email = EmailMessage(
            "Mensagem do blog",
            "De: {} <{}> Enviou a seguinte mensagem:\n\n{}".format(name, email, content_message),
            "nao-responder@inbox.mailtrap.io",
            ["eltonriaweb@gmail.com"],
            reply_to=[email]
        )

        try:
            email.send()
            send = True
        except:
            send = False

    context = {
        'form': form,
        'success': send,
    }
    return render(request, 'contact/contact.html', context)



