dependent on other model field


class Building(models.Model):
    name = models.CharField(max_length=10)
    floors= models.IntegerField()

    def __str__(self):
        return self.name

class BuidingAccessRole(models.Model):
    role_name = models.CharField(max_length=10)  #name for the role of accessing a floor of one building
    building = models.ForeignKey(building,on_delete=models.CASCADE)
    floor = models.IntegerField()   Note:#i want this floor to be shown as choicefield with count starting from 1 to (building.floors) and get saved as integer value in database.
    def __str__(self):
       return self.name

  """If we set Building admin page as this object : 
       name='b1'
       floors=3
  then :
  BuidingAccessRole admin page to be shown as 
       name='Access for floor'
       building = b1 or 1 as 'id'
      floor shown as <select>1,2,3 as option </select>""" 
