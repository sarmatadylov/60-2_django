from django.contrib import admin 

from jobs.models import Jobs, Category, Comment, Tag 

admin.site.register(Jobs) 
admin.site.register(Category) 
admin.site.register(Tag) 
admin.site.register(Comment)
# Register your models here.


