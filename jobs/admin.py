from django.contrib import admin 

from jobs.models import Jobs, Category, Tag

admin.site.register(Jobs) 
admin.site.register(Category) 
admin.site.register(Tag)
# Register your models here.


