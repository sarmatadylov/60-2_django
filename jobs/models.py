from django.db import models

# Create your models here.
"""
create table jobs (
    id integer primary key,
    name sting 
)
"""

class Category(models.Model): 
    name = models.CharField(max_length=128)  
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True) 

    def __str__(self):
        return f"{self.name}"


class Jobs(models.Model):
    photo = models.ImageField(blank=True, null=True, upload_to='jobs/')
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    category  = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}"