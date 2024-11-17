from django.contrib import admin
from models import *
from random import *
import os

projs = Project.objects.all()
locations = Location.objects.all()
capacities = [20, 30, 40, 50, 60, 70, 80, 90, 100] 
imgs = os.listdir("./static/img/MaterialTrackerApp/material")
currencies = Currency.objects.all()

upper_bound = 100
for i in range(0, upper_bound):
    Material.objects.create(
        ref=f"ABC_{randint(1, upper_bound)}",
        descritpion=f"Description {i}",
        capacity=choice(capacities),
        
        project=choice(projs),
        main_img=choice(imgs),
        current_location=choice(locations),
        quality_exp_date=timezone.now(),
        cost=random(100, 10000),
        currency=choice(currencies),

        created_at=timezone.now(),
        updated_at=timezone.now()
    )