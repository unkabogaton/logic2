
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.postgres.search import SearchVector
from django.db.models import Q

# Create your views here.
def index(request):
    if request.method == 'POST':
        form=ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            items= Item.objects.all().order_by('-created')
            messages.success(request,('You successfully posted your meme!'))
            return render(request,'index.html', context={'items': items, 'form':form})
    items= Item.objects.all().order_by('?')
    return render(request,'index.html', context={'items': items})

def delete(request, item_id):
    item=get_object_or_404(Item, pk=item_id)
    item.delete()
    messages.success(request,('A Note Has Been Successfully Deleted!'))
    return redirect('index')

def cross_off(request, item_id):
    item=get_object_or_404(Item, pk=item_id)
    item.completed=True
    item.save()
    messages.success(request,('Congrats! A Task Has Been Completed!'))
    return redirect('index')

def uncross(request, item_id):
    item=get_object_or_404(Item, pk=item_id)
    item.completed=False
    item.save()
    messages.success(request,('A Task Has Been Set to Ongoing!'))
    return redirect('index')

def edit(request, item_id):
    if request.method == 'POST':
        item=Item.objects.get(pk=item_id)
        form=ItemForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,('A Note Has Been Successfully Updated!'))
            return redirect('index')
    else:
        item=Item.objects.get(pk=item_id)

def search(request):
    query=request.GET.get("q")
    try:
        items=Item.objects.filter(Q(item__icontains=query)|Q(description__icontains=query)|Q(created__icontains=query)).distinct()
        messages.success(request,('Search results ready'))
        return render(request,'index.html', context={'items': items})
    except:
        return render(request,'index.html', context={'items': items})

def completed_task(request):
    items=Item.objects.filter(completed=True)
    messages.success(request,('Showing All Completed Task'))
    return render(request,'index.html', context={'items': items})

def ongoing_task(request):
    items=Item.objects.filter(completed=False)
    messages.success(request,('Showing All Ongoing Task'))
    return render(request,'index.html', context={'items': items})

def all_completed(request):
    items=Item.objects.filter(completed=False)
    for item in items:
        item.completed=True
        item.save()
    messages.success(request,('All Tasks are set to Completed'))
    return redirect('index')

def all_ongoing(request):
    items=Item.objects.filter(completed=True)
    for item in items:
        item.completed=False
        item.save()
    messages.success(request,('All Tasks are set to Ongoing'))
    return redirect('index')


def hominem(request):
    items=Item.objects.filter(type="Argumentum ad hominem").order_by('?')
    messages.success(request,('Argumentum ad Hominem'))
    return render(request,'hominem.html', context={'items': items})

def baculum(request):
    items=Item.objects.filter(type="Argumentum ad baculum").order_by('?')
    messages.success(request,('Argumentum ad Baculum'))
    return render(request,'baculum.html', context={'items': items})

def misericordiam(request):
    items=Item.objects.filter(type="Argumentum ad misericordiam").order_by('?')
    messages.success(request,('Argumentum ad misericordiam'))
    return render(request,'misericordiam.html', context={'items': items})

def populum(request):
    items=Item.objects.filter(type="Argumentum ad populum").order_by('?')
    messages.success(request,('Argumentum ad populum'))
    return render(request,'populum.html', context={'items': items})

def dichotomy(request):
    items=Item.objects.filter(type="False dichotomy").order_by('?')
    messages.success(request,('False dichotomy'))
    return render(request,'dichotomy.html', context={'items': items})

def false_cause(request):
    items=Item.objects.filter(type="False cause").order_by('?')
    messages.success(request,('False cause'))
    return render(request,'false_cause.html', context={'items': items})

def equivocation(request):
    items=Item.objects.filter(type="Equivocation").order_by('?')
    messages.success(request,('Equivocation'))
    return render(request,'equivocation.html', context={'items': items})

def slippery_slope(request):
    items=Item.objects.filter(type="Slippery slope").order_by('?')
    messages.success(request,('Slippery slope'))
    return render(request,'slippery_slope.html', context={'items': items})

def false_analogy(request):
    items=Item.objects.filter(type="False analogy").order_by('?')
    messages.success(request,('False analogy'))
    return render(request,'false_analogy.html', context={'items': items})

def generalization(request):
    items=Item.objects.filter(type="Hasty generalization").order_by('?')
    messages.success(request,('Hasty generalization'))
    return render(request,'generalization.html', context={'items': items})