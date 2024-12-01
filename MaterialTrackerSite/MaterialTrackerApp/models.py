from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()

    def __str__(self):
        return self.user.email
    
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class ProjectUser(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} is in {self.project.name}"

class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Material(models.Model):
    ref = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    capacity = models.FloatField()
    
    # Attributes for faster fetching
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    main_img = models.ImageField(default="{% static 'img/MaterialTrackerApp/generic_user.png' %}", blank=True)
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    quality_exp_date = models.DateTimeField()
    cost = models.FloatField()
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ref

class MaterialImg(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    img = models.ImageField(default="{% static 'img/MaterialTrackerApp/generic_user.png' %}", blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.item.name


class MaterialInspection(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quality_exp_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.item.name} expires on {self.quality_exp_date}"


class MaterialTransaction(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    origin_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='origin_transactions')
    destination_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='destination_transactions')
    status = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def clean(self):
        if self.origin_project == self.destination_project:
            raise ValidationError("Origin and destination projects cannot be the same.")

    def __str__(self):
        return f"{self.user.username} booked {self.item.name}"

class MaterialLocation(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.item.name} is in {self.location.name}"

class MaterialMovements(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    origin_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='origin_location')
    destination_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='destination_location')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def clean(self):
        if self.origin_location == self.destination_location:
            raise ValidationError("Origin and destination locations cannot be the same.")
    
    def __str__(self):
        return f"{self.user.username} moved {self.item.name} from {self.origin_location.name} to {self.destination_location.name}"

class Currency(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    dolar_value = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class MTCars(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(db_column='NAME') # Field name made lowercase.
    mpg = models.FloatField(db_column='MPG') # Field name made lowercase.
    cyl = models.IntegerField(db_column='CYL') # Field name made lowercase.
    disp = models.FloatField(db_column='DISP') # Field name made lowercase.
    hp = models.IntegerField(db_column='HP') # Field name made lowercase.
    wt = models.FloatField(db_column='WT') # Field name made lowercase.
    qsec = models.FloatField(db_column='QSEC') # Field name made lowercase.
    vs = models.IntegerField(db_column='VS') # Field name made lowercase.
    am = models.IntegerField(db_column='AM') # Field name made lowercase.
    gear = models.IntegerField(db_column='GEAR') # Field name made lowercase.
class Meta:
    managed = True
    db_table = 'MTCars'
    ordering = ['id']
    def __str__(self):
        return self.name

# # DBMaterials models
# class MTMaterials(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.TextField(db_column='NAME') # Field name made lowercase.
#     mpg = models.FloatField(db_column='MPG') # Field name made lowercase.
#     cyl = models.IntegerField(db_column='CYL') # Field name made lowercase.
#     disp = models.FloatField(db_column='DISP') # Field name made lowercase.
#     hp = models.IntegerField(db_column='HP') # Field name made lowercase.
#     wt = models.FloatField(db_column='WT') # Field name made lowercase.
#     qsec = models.FloatField(db_column='QSEC') # Field name made lowercase.
#     vs = models.IntegerField(db_column='VS') # Field name made lowercase.
#     am = models.IntegerField(db_column='AM') # Field name made lowercase.
#     gear = models.IntegerField(db_column='GEAR') # Field name made lowercase.

# class Meta:
#     managed = True
#     db_table = 'MTCars'
#     ordering = ['id']
#     def __str__(self):
#         return self.name