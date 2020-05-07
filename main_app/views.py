from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pokemon, Toy

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def pokemon_index(request):
    pokemon_list = Pokemon.objects.filter(user=request.user)
    return render(request, 'pokemon/index.html', { 'pokemon_list': pokemon_list })

@login_required
def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    toys_pokemon_doesnt_have = Toy.objects.exclude(id__in = pokemon.toys.all().values_list('id'))
    return render(request, 'pokemon/detail.html', { 'pokemon': pokemon, 'toys': toys_pokemon_doesnt_have })

class PokemonCreate(LoginRequiredMixin, CreateView):
    model = Pokemon
    fields = ['name', 'pkmntype', 'description', 'level']
    success_url = '/pokemon/'
    
    def form_valid(self, form):
      form.instance.user = self.request.user  # form.instance is the cat
      return super().form_valid(form)

class PokemonUpdate(LoginRequiredMixin, UpdateView):
    model = Pokemon
    fields = ['name', 'pkmntype', 'description', 'level']

class PokemonDelete(LoginRequiredMixin, DeleteView):
    model = Pokemon
    success_url = '/pokemon/'

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

@login_required
def assoc_toy(request, pokemon_id, toy_id):
  Pokemon.objects.get(id=pokemon_id).toys.add(toy_id)
  return redirect('detail', pokemon_id=pokemon_id)

@login_required
def unassoc_toy(request, pokemon_id, toy_id):
  Pokemon.objects.get(id=pokemon_id).toys.remove(toy_id)
  return redirect('detail', pokemon_id=pokemon_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)