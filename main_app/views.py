from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Wish

# Home view 
def home(request):
    wishes = Wish.objects.all()
    return render(request, 'index.html', {'wishes': wishes})

class Add_Wish(CreateView):
  model = Wish
  fields = ['description']

class Delete_Wish(DeleteView):
  model = Wish
  success_url = '/'
