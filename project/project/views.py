from django.shortcuts import render, redirect
from posts.models import Car, Brand
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from posts import forms,models


def home(request):
    data = Car.objects.all()
    return render(request, 'home2.html', {'data': data})

@login_required
def car(request):
    data = Car.objects.all()
    return render(request, 'home.html', {'data': data})



@login_required
def mercede(request):
    brand_instance = Brand.objects.get(name='Marcedes')  
    data = Car.objects.filter(brands=brand_instance)
    return render(request, 'mar.html', {'data': data})

@login_required
def bmw(request):
    brand_instance = Brand.objects.get(name='BMW')  
    data = Car.objects.filter(brands=brand_instance)
    return render(request, 'bmw.html', {'data': data})

@login_required
def tata(request):
    brand_instance = Brand.objects.get(name='TATA') 
    data = Car.objects.filter(brands=brand_instance)
    return render(request, 'tata.html', {'data': data})

@login_required
def all(request):
    data = Car.objects.all()
    return render(request, 'all.html', {'data': data})
  
@login_required
def add_car(request, id):
    post = models.Car.objects.get(pk=id) 
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST': 
        post_form = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid(): 
            post_form.instance.author = request.user
            post_form.save() 
            return redirect('profile') 
    
    return render(request, 'add_post.html', {'form' : post_form})
