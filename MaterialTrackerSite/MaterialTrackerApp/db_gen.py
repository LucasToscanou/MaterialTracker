from django.contrib import admin
from MaterialTrackerApp.models import *
from random import *

projs = Project.objects.all()
items = []

counter = 0
for proj in projs:
    for i in range(counter, counter + 10):
        items.append(Item(name=f"Item {i}", description=f"Description {i}", project=proj))
    counter = counter + 10
    print(counter)

# Bulk create all items in a single query
Item.objects.bulk_create(items)
