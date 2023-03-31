from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from . import models
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView,DeleteView

class CatList(LoginRequiredMixin,View):
    def get(self,request):
        bc = models.Breed.objects.all().count()
        cl = models.Cat.objects.all()

        ctx = {'breed_count':bc,'cat_list':cl}
        return render(request,'cats/cat_list.html',ctx)
    
class CatCreate(LoginRequiredMixin, CreateView):
    model = models.Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:index')
class CatDelete(LoginRequiredMixin, DeleteView):
    model = models.Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:index')
class CatUpdate(LoginRequiredMixin, UpdateView):
    model = models.Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:index')

class BreedList(LoginRequiredMixin,View):
    def get(self,request):
        bl = models.Breed.objects.all()
        ctx = {'breed_list':bl}
        return render(request,'cats/breed_list.html',ctx)
    
class BreedCreate(LoginRequiredMixin, CreateView):
    model = models.Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:index')
class BreedDelete(LoginRequiredMixin, DeleteView):
    model = models.Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:index')
class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = models.Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:index')