from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
#from django.core.mail import EmailMessage
from email.message import EmailMessage
from django.core.mail import send_mail
import smtplib
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from app.forms import ContactForm

class HomeView(TemplateView):
    template_name = 'manta/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()

        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        body = render_to_string(
            'manta/email_content.html', {
                'name': name,
                'email': email,
                'message': message,
            },
        )

        #email_message = EmailMessage(
        #    subject='Mensaje de usuario',
        #    body=body,
        #    from_email=email,
        #    to=['kevinchocano@gmail.com'],
        #)
        #email_message.content_subtype = 'html'
        #email_message.send()

        #EmailMessage() envia el correo usando las librerias de Python y le indicas el server smtp al que debe conectar
        #message = EmailMessage()
        #message.set_content("test message sent locally")
        #message.set_content(body)
        #message['Subject'] = 'Your subject here'
        #message['From'] = 'kevinchocano@gmail.com'
        #message['To'] = 'kevinchocano@gmail.com'
        # Para activar el servidor de prueba es con el comando // python -m smtpd -n -c DebuggingServer localhost:1025
        #smtp_server = smtplib.SMTP('smtp.server.address:587') // smtp_server = smtplib.SMTP('smtp.server.address:25') // smtp_server = smtplib.SMTP('aspmx.l.google.com:25') 
        #smtp_server = smtplib.SMTP('localhost:1025')
        #smtp_server.send_message(message)
        #smtp_server.quit()
        # send_mail envia el correo usando librerias de Django
        send_mail(
            'Subject here',
            body,
            'kevinchocano@gmail.com',
            ['kevinchocano@gmail.com'],
            fail_silently=False,
        )

        # Se crea un Json que son los datos que enviara por ajax
        return JsonResponse(
            {
                'content': {
                    'message': 'Mensaje enviado correctamente',
                },
                'name': name
            }
        )
