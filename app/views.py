from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
#from django.core.mail import EmailMessage
from email.message import EmailMessage
from django.core.mail import send_mail
import smtplib
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from app.forms import ContactForm, PostForm
from app.models import Post

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

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #posts = Post.objects.all()
    return render(request, 'manta/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'manta/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'manta/post_detail.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'manta/post_edit.html', {'form': form})
