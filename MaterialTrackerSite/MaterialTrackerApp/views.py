import csv

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views import View

from MaterialTrackerApp.models import *
from django.urls import reverse


def index(request):
    return render(request, 'MaterialTrackerApp/index.html')

def about(request):
    return render(request, 'MaterialTrackerApp/about.html')

@login_required
def project(request):
    return render(request, 'MaterialTrackerApp/project.html')

class InventoryView(LoginRequiredMixin, View):
    template_name = 'MaterialTrackerApp/inventory.html'


    def get(self, request):
        items = Item.objects.all()
        context = {
            'items': items
        }
        for i in items:
            print(i.name)
        return render(request, self.template_name, context)


@login_required
def add_item(request):
    if request.method == 'GET':
        items = Item.objects.all()
        projects = Project.objects.all()
        locations = Location.objects.all()
        
        context = {
            'currencies': Currency.objects.all(),
            'projects': projects,
            'locations': locations,
        }
        return render(request, 'MaterialTrackerApp/add_item.html', context)
    elif request.method == 'POST':
        form = Item(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('inventory')
    else:
        form = Item()
    return render(request, 'MaterialTrackerApp/add_item.html', {'form': form})

@login_required
def new_request_finish(request):
    if request.method == 'GET':
        items = Item.objects.all()

        items_summary = {}
        for p in items.values('project').distinct():
            project = Project.objects.get(pk=p['project'])
            
            items_summary[project.name] = {}
            items_summary[project.name]['items'] = []
            items_summary[project.name]['qty'] = 0
            items_summary[project.name]['cost'] = {
                'item': 0,
                'transport': 0,
                'storage': 0,
                'customs': 0,
                'total_logistics': 0,
            }

            for i in items.filter(project=project):
                items_summary[project.name]['items'].append(i)
                items_summary[project.name]['qty'] += 1
                items_summary[project.name]['cost']['item'] += i.cost
                items_summary[project.name]['cost']['transport'] += i.cost
                items_summary[project.name]['cost']['storage'] += i.cost
                items_summary[project.name]['cost']['transport'] += i.cost
                items_summary[project.name]['cost']['total_logistics'] += items_summary[project.name]['cost']['transport'] + items_summary[project.name]['cost']['storage'] + items_summary[project.name]['cost']['customs']

        total_cost = 0
        for p in items_summary:
            total_cost += items_summary[p]['cost']['item'] + items_summary[p]['cost']['total_logistics']

        projects = Project.objects.all()
        locations = Location.objects.all()
        context = {
            'items_summary': items_summary,
            'projects': projects,
            'locations': locations,
            'total_cost': total_cost,
        }
        return render(request, 'MaterialTrackerApp/new_request_finish.html', context)
    # if request.method == 'POST':
    #     form = TransactionForm(request.POST)
    #     if form.is_valid():
    #         transaction = form.save(commit=False)
    #         transaction.save()
    #         return redirect('inventory')
    # else:
    #     form = TransactionForm()
    # return render(request, 'MaterialTrackerApp/new_transaction.html', {'form': form})

@login_required
def new_request_view(request):
    if request.method == 'GET':
        items = Item.objects.all()[:10]
        context = {
            'items': items
        }
        for i in items:
            print(i.name)
        return render(request, 'MaterialTrackerApp/new_request_view.html', context)
    # if request.method == 'POST':
    #     form = TransactionForm(request.POST)
    #     if form.is_valid():
    #         transaction = form.save(commit=False)
    #         transaction.save()
    #         return redirect('inventory')
    # else:
    #     form = TransactionForm()
    # return render(request, 'MaterialTrackerApp/new_transaction.html', {'form': form})


@login_required
def new_request_result(request):
    if request.method == 'GET':
        items = Item.objects.all()[:10]
        context = {
            'items': items
        }
        for i in items:
            print(i.name)
        return render(request, 'MaterialTrackerApp/new_request_result.html', context)
    # if request.method == 'POST':
    #     form = TransactionForm(request.POST)
    #     if form.is_valid():
    #         transaction = form.save(commit=False)
    #         transaction.save()
    #         return redirect('inventory')
    # else:
    #     form = TransactionForm()
    # return render(request, 'MaterialTrackerApp/new_transaction.html', {'form': form})