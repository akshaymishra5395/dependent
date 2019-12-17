from django.db import models

# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=10)
    floors= models.IntegerField()

    def __str__(self):
        return self.name

class BuidingAccessRole(models.Model):
    role_name = models.CharField(max_length=10)  #name for the role of accessing a floor of one building
    building = models.ForeignKey(Building,on_delete=models.CASCADE)
    floor = models.IntegerField()   #Note:#i want this floor to be shown as choicefield with count starting from 1 to (building.floors) and get saved as integer value in database.
    
    def __str__(self):
       return self.role_name