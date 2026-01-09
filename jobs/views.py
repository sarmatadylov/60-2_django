from django.http import HttpResponse
from django.shortcuts import render 

from .form import JobsFrom
from .models import Jobs 

# Create your views here.  



"""
select * form jobs;
"""

"""
select * from jobs ILIKE where = "%phone%"
"""

"""
insert into jobs (name, description, price) values ('name','description','price')
"""

# GET - для просмотра данных 
# POST - для отправки данных 
# PUT - для обновления данных 
# PATCH - для обновления частичных данных 
# DELETE - для удаления 

def home(request): 
    if request.method == "GET":
       return render(request, "base.html")


def jobs_list(request): 
    if request.method == "GET":
       jobs = Jobs.objects.all()
       return render(request, "jobs/jobs_list.html", context={"jobs": jobs})


def jobs_detail(request, jobs_id): 
    if request.method == "GET":
       jobs = Jobs.objects.filter(id=jobs_id).first()
       return render(request, "jobs/jobs_detail.html", context={"jobs": jobs}) 
    
def jobs_create_view(request): 
    if request.method == "GET":  
        form = JobsFrom()
        return render(request, "jobs/jobs_create.html", context={"form": form}) 
    elif request.method == "POST":  
        form = JobsFrom(request.POST, request.FILES) 
        if form.is_valid(): 
            print(form.cleaned_data)
        Jobs.objects.create(
            name=form.cleaned_data["name"],
            description=form.cleaned_data["description"], 
            price=form.cleaned_data["price"],
            photo=form.cleaned_data["photo"], 
        ) 
        return HttpResponse("Jobs created")

        
       


