from users.forms import SignUpForm

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    template_name ='sign_up.html'
    dorm_class = SignUpForm
    success_url = reverse_lazy('home')

class UserLoginView(LoginView):
    template_name = 'login.html'