from django.views.generic import TemplateView
from django.template.loader import render_to_string
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

class CreateUsers(TemplateView):
    template_name = 'manta/home.html'

    """as its name suggests, obtains the data from the context. 
    in this case, the ContactForm() form is passed to it."""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()

        return context
    # when a POST request is made, this function is executed
    def post(self, request, *args, **kwargs):

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # A Json is created with the data to be displayed on the screen.
        return JsonResponse(
            {
                'content': {
                    'message': 'Mensaje enviado correctamente',
                },
                'name': name,
                'email': email,
                'message': message
            }
        )
