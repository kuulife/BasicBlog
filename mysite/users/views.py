from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,UpdateView,DetailView
from django.urls import reverse_lazy
from .forms import SignUpForm, UpdateUserForm, CreateProfile,EditProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from blog.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class CreateProfilePageView(LoginRequiredMixin,CreateView):
	model = Profile
	form_class = CreateProfile
	template_name = 'users/create_profile_page.html'

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class EditProfilePageView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Profile
	form_class = EditProfilePageForm
	template_name = 'users/edit_profile_page.html'
	success_url = reverse_lazy('home')

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.user:
			return True
		else:
			return False

class ShowProfilePageView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
	model = Profile
	template_name = 'users/show_profile.html'

	def get_context_data(self,*args,**kwargs):
		context = super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
		user_page = get_object_or_404(Profile, id = self.kwargs['pk'])
		context['user_page'] = user_page
		return context
		
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.user:
			return True
		else:
			return False

class PasswordsChangeView(LoginRequiredMixin,PasswordChangeView):
	form_class = PasswordChangeForm
	success_url = reverse_lazy('password-success')


class UserRegisterView(CreateView):
	form_class = SignUpForm
	template_name = 'users/registration.html'
	success_url = reverse_lazy('login')


class UserUpdateView(LoginRequiredMixin,UpdateView):
	form_class = UpdateUserForm
	template_name = 'users/edit_profile.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user


def password_success(request):
	return render(request, 'users/password_success.html')