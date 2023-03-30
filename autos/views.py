from django.urls import reverse_lazy
from django.views import View
from . import models,forms
from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# make crud with simple View class 
class MainView(LoginRequiredMixin,View):
    def get(self,request):
        mc = models.Make.objects.all().count()
        al = models.Autos.objects.all()

        ctx = {'make_count':mc,'autos_list':al}
        return render(request,'autos/autos_list.html',ctx)

class MakeView(LoginRequiredMixin,View):
    def get(self,request):
        ml = models.Make.objects.all()

        return render(request,'autos/make_list.html',{'make_list':ml})
    
class MakeCreate(LoginRequiredMixin,View):
    template = 'autos/make_form.html'
    success_url = reverse_lazy('autos:index')
    
    def get(self,request):
        form = forms.MakeForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)
    
    def post(self,request):
        form = forms.MakeForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)
        
        make = form.save()
        return redirect(self.success_url)\
    
class MakeUpdate(LoginRequiredMixin,View):
    model = models.Make
    success_url = reverse_lazy('autos:index')
    template = 'autos/make_form.html'

    def get(self,request,pk):
        make = get_object_or_404(self.model, id=pk)
        form = forms.MakeForm(instance=make)
        ctx = {'form': form}
        return render(request,self.template,ctx)
    
    def post(self,request,pk):
        make = get_object_or_404(self.model, pk=pk)
        form = forms.MakeForm(request.POST,instance=make)

        if not form.is_valid():
            ctx = {'form':form}
            return render(request,self.template,ctx)
        form.save()
        return redirect(self.success_url)

class MakeDelete(LoginRequiredMixin,View):
    model = models.Make 
    success_url = reverse_lazy('autos:index')
    template = 'autos/make_confirm_delete.html'

    def get(self,request,pk):
        make = get_object_or_404(self.model, pk=pk)
        return render(request,self.template,{'make':make})
    
    def post(self,request,pk):
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(self.success_url)

# crud of Autos with genreric templates
class AutosCreateView(LoginRequiredMixin,CreateView):
    model = models.Autos
    fields = '__all__'
    success_url = reverse_lazy('autos:index')

class AutosDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Autos
    fields = '__all__'
    success_url = reverse_lazy('autos:index')

class AutosUpdateView(LoginRequiredMixin,UpdateView):
    model = models.Autos
    fields = '__all__'
    success_url = reverse_lazy('autos:index')

