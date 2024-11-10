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

