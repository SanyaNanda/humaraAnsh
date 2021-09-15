from portal.models import User, Patient,  Doctor
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.contrib.auth.forms import AuthenticationForm

from .models import Patient
from .forms import PatientSignUpForm, DoctorSignUpForm
from .decorators import patient_required

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.user.is_doctor:
                    messages.info(request, f"You are now logged in as {username}")
                    return redirect('doctor_home')
                else:
                    return redirect('patient_home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "registration/login.html",
                    context={"form":form})

class SignUpView(TemplateView):
    template_name = 'portal/index-home.html'

class ContactUsView(TemplateView):
    template_name = 'portal/contact.html'

class TeamView(TemplateView):
    template_name = 'portal/team.html'

class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'portal/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('patient_home')

class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'portal/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('doctor_home')

class PatientHomeView(ListView):
    model = Patient
    template_name = 'portal/patient_home.html'

class DoctorHomeView(ListView):
    model = Doctor
    template_name = 'portal/doctor_home.html'

@login_required
def login_success(request):
    if request.user.is_doctor:
        return HttpResponseRedirect(reverse('doctor_home'))
    else:
        return HttpResponseRedirect(reverse('patient_home'))