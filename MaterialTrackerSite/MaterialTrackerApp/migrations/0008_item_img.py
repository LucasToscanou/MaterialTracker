# Generated by Django 5.1.3 on 2024-11-10 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaterialTrackerApp', '0007_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='img',
            field=models.ImageField(blank=True, default="{% static 'img/MaterialTrackerApp/generic_user.png' %}", upload_to=''),
        ),
    ]
