from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Pokemon(models.Model):
  name = models.CharField(max_length=100)
  pkmntype = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  level = models.IntegerField()
  toys = models.ManyToManyField(Toy)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'pokemon_id': self.id})
    
