from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from .forms import SignUpForm, UpdateUserForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangeForm
	success_url = reverse_lazy('password-success')

class UserRegisterView(CreateView):
	form_class = SignUpForm
	template_name = 'users/registration.html'
	success_url = reverse_lazy('login')

class UserUpdateView(UpdateView):
	form_class = UpdateUserForm
	template_name = 'users/profile.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user

def password_success(request):
	return render(request, 'users/password_success.html')