from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, edit
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import Post
from portal.models import Doctor, Patient
from .forms import PostForm

class SelectView(ListView):
	model = Doctor
	template_name = 'reports/selected.html'

def LikeView(request, pk):
	post = get_object_or_404(Doctor, id=request.POST.get('doctor_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
	return HttpResponseRedirect(reverse('post_details', args=[str(pk)]))

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'reports/add_report.html'

def choice(request,pk):
    patient = get_object_or_404(Patient, id=request.user.id)
    patient.choice = pk
    return HttpResponseRedirect(reverse('portal:patient_home'))