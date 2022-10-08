from user.forms import RegisterForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUp(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
