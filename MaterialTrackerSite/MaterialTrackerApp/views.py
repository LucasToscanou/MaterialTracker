import csv

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views import View
from django.contrib import messages 

from MaterialTrackerApp.models import *
from django.urls import reverse
from random import *

def index(request):
    return render(request, 'MaterialTrackerApp/index.html')

def about(request):
    return render(request, 'MaterialTrackerApp/about.html')

@login_required
def dashboard(request):

    if request.method == 'GET':
        materials = Material.objects.all()
        user_projects_id = ProjectUser.objects.filter(user=request.user).values_list('project', flat=True)
        # other_user_projects = Project.objects.filter(pk__in=user_projects_id).exclude(pk=current_project_pk)

        context = {
            'materials': materials,
            # 'other_user_projects': other_user_projects,
            'columns': ["Ref", "Description", "Capacity", "Project", "Location", "Quality Exp Date", "Cost"]
        }
        return render(request, 'MaterialTrackerApp/project.html', context)

    elif request.method == 'POST':
        form_id = request.POST.get('form_id')
        if form_id == 'project_choice_form':
            return redirect('MaterialTrackerApp:project', current_project_pk=request.POST.get('selected_project'))

class InventoryView(LoginRequiredMixin, View):
    template_name = 'MaterialTrackerApp/inventory.html'


    def get(self, request):
        materials = Material.objects.all()
        context = {
            'materials': materials,
            'columns': ["Ref", "Description", "Capacity", "Project", "Location", "Quality Exp Date", "Cost"]
        }
        return render(request, self.template_name, context)
    
    def post(self, request):

        if request.POST['action'] == 'request':
            return render(request, 'MaterialTrackerApp/new_request_finish.html')
        
        elif request.POST['action'] == 'edit':
            print("Editing")
            material_id = request.POST['id']
            return redirect('MaterialTrackerApp:edit_item', pk=material_id)

        elif  request.POST['action'] == 'delete':
            print("Deleting")
            print(request.POST['id'])
            Material.objects.filter(pk=request.POST['id']).delete()
            return redirect('MaterialTrackerApp:inventory')
        
        elif request.POST['action'] == 'restart_db':
            from django.contrib import admin
            import os

            projs = Project.objects.all()
            locations = Location.objects.all()
            capacities = [20, 30, 40, 50, 60, 70, 80, 90, 100]
            print("curr_dir = " + os.getcwd())
            imgs = os.listdir("./MaterialTrackerApp/static/img/MaterialTrackerApp/material")
            currencies = Currency.objects.all()

            upper_bound = 100
            Material.objects.all().delete()
            for i in range(0, upper_bound):
                Material.objects.create(
                    ref=f"ABC_{i}",
                    description=f"Description {i}",
                    capacity=choice(capacities),
                    
                    project=choice(projs),
                    main_img=choice(imgs),
                    current_location=choice(locations),
                    quality_exp_date=timezone.now(),
                    cost=randrange(100, 10000),
                    currency=choice(currencies),

                    created_at=timezone.now(),
                    updated_at=timezone.now()
                )

            return redirect('MaterialTrackerApp:inventory')


@login_required
def add_item(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        locations = Location.objects.all()
        currency = Currency.objects.all()

        context = {
            'projects': projects,
            'locations': locations,
            'currencies': currency,
            'capacities': [20, 30, 40, 50, 60, 70, 80, 90, 100],
        }
        return render(request, 'MaterialTrackerApp/add_item.html', context)
    elif request.method == 'POST':
        if request.POST.get('action') == 'cancel':
            return redirect('MaterialTrackerApp:inventory')
        elif request.POST.get('action') == 'save':
            # Get data from the POST request
            reference = request.POST.get('reference')
            description = request.POST.get('description')
            capacity = request.POST.get('capacity')
            project = Project.objects.get(id=request.POST.get('project'))
            location = Location.objects.get(id=request.POST.get('current_location'))
            cost = request.POST.get('cost')
            currency = Currency.objects.get(id=request.POST.get('currency'))
            quality_exp_date = request.POST.get('quality_exp_date')
            photo = request.FILES.get('photo')  # Assuming photo is uploaded as a file

            print("reference = " + str(reference))
            print("description = " + str(description))
            print("capacity = " + str(capacity))
            print("project = " + str(project))
            print("location = " + str(location))
            print("cost = " + str(cost))
            print("currency = " + str(currency))
            print("quality_exp_date = " + str(quality_exp_date))
            print("photo = " + str(photo))

            # Validate the required fields
            if not reference or not description or not capacity or not project:
                messages.error(request, "Please fill out all required fields.", extra_tags='latest')
                return  render(request, 'MaterialTrackerApp/add_item.html')
            
            # Create a new Item instance and save it to the database
            material = Material(
                ref=reference,
                description=description,
                capacity=capacity,
                project=project,
                current_location=location,
                cost=cost,
                currency=currency,
                quality_exp_date=quality_exp_date,
                main_img=photo
            )
            material.save()

            messages.success(request, "Item created successfully!", extra_tags='latest')
            return redirect('MaterialTrackerApp:inventory')
        else:
            print("POST error")

    else:
        print("erro")

@login_required
def edit_item(request, pk):

    if request.method == 'GET':
        material =get_object_or_404(Material, pk=pk)
        projects = Project.objects.all()
        locations = Location.objects.all()
        currencies = Currency.objects.all()
        context = {
            'material': material,
            'projects': projects,
            'locations': locations,
            'currencies': currencies,
            'capacities': [20, 30, 40, 50, 60, 70, 80, 90, 100],
        }

        return render(request, 'MaterialTrackerApp/edit_item.html', context)
    elif request.method == 'POST':
        if request.POST.get('action') == 'cancel':
            return redirect('MaterialTrackerApp:inventory')
        elif request.POST.get('action') == 'save':
            fields_to_update = {
                'ref': request.POST.get('ref'),
                'description': request.POST.get('description'),
                'capacity': request.POST.get('capacity'),
                'project': request.POST.get('project'),
                'current_location': request.POST.get('current_location'),
                'cost': request.POST.get('cost'),
                'currency': request.POST.get('currency'),
                'quality_exp_date': request.POST.get('quality_exp_date'),
                'main_img': request.FILES.get('main_img'),
                'updated_at': timezone.now()
            }

            # Filter out fields with None values
            fields_to_update = {k: v for k, v in fields_to_update.items() if v is not None}

            Material.objects.filter(pk=pk).update(**fields_to_update)


            messages.success(request, "Item changed successfully!", extra_tags='latest')
            return redirect('MaterialTrackerApp:inventory')

@login_required
def add_item_success(request):
    return render(request, 'MaterialTrackerApp/add_item_success.html')

def add_item_fail(request):
    return render(request, 'MaterialTrackerApp/add_item_fail.html')


class NewOrderView(LoginRequiredMixin, View):
    template_name = 'MaterialTrackerApp/new_request_finish.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass
