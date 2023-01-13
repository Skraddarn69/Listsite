from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
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