from django.contrib.auth.models import User
from django.db import models

class Group(models.Model):
    owner = models.ForeignKey(User, related_name='owned_groups', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='group_members')
    name = models.CharField(max_length=100)  
    
class Expense(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    paid_by = models.ForeignKey(User, related_name='expenses_paid', on_delete=models.CASCADE)
    involved_members = models.ManyToManyField(User, related_name='expenses_involved')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

# Ensure you handle the Balance updates within your application logic
