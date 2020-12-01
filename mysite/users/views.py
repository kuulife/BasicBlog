from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from .forms import SignUpForm, UpdateUserForm
# from django.contrib.auth.forms import UserChangeForm



class UserRegisterView(CreateView):
	form_class = SignUpForm
	template_name = 'registration/registration.html'
	success_url = reverse_lazy('login')

class UserUpdateView(UpdateView):
	form_class = UpdateUserForm
	template_name = 'registration/profile.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user