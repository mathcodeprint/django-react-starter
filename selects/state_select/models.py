from django.db import models

# Create your models here.
class StateTable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    abbr = models.CharField(max_length=2, unique=True, null=False)
    
    def __str__(self):
        return self.name

class Counties(models.Model):
    id = models.AutoField(primary_key=True)
    state_table = models.ForeignKey(StateTable, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return f"{self.name} ({self.state_table})"

class Towns(models.Model):
    id = models.AutoField(primary_key=True)
    counties = models.ForeignKey(Counties, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return f"{self.name}, {self.counties}"