from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import List, Object
from django.contrib import messages

def registrera(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            anvandarnamn = form.cleaned_data.get('username')
            messages.success(request, f'Konto skapades för {anvandarnamn}')
            return redirect('loggain')
    else:
        form=UserRegisterForm()

    return render(request, 'listapp/registrera.html',{'form':form})

class AllaListor(LoginRequiredMixin,ListView):
    model=List
    template_name = 'listapp/hem.html'
    context_object_name = 'listor'
    ordering = ['-cdate']

class EnLista(LoginRequiredMixin,ListView):
    model=Object
    template_name = 'listapp/lista.html'
    context_object_name = 'objects'

    def get_queryset(self):
        return Object.objects.filter(list=self.kwargs['pk'])

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['listan'] = List.objects.filter(id=self.kwargs['pk'])
        return context

class SkapaLista(LoginRequiredMixin,CreateView):
    model=List
    fields=['listname']

    def form_valid(self,form):
        form.instance.cuser=self.request.user
        return super().form_valid(form)

class UppdateraLista(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=List
    fields=['listname']

    def test_func(self):
        lista=self.get_object()
        if self.request.user == lista.cuser:
            return True
        return False

class RaderaLista(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=List
    sucess_url='/'

    def test_func(self):
        lista=self.get_object()
        if self.request.user == lista.cuser:
            return True
        return False