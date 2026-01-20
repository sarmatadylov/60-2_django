from django.http import HttpResponse
from django.shortcuts import redirect, render 
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .form import CommentForm, JobsFrom, SearchForm
from .models import Comment, Jobs 

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
    
lsit = ["123", 12, "asd", True]


@login_required(login_url ="/login/")
def jobs_list(request): 
    jobs = Jobs.objects.all()
    if request.method == "GET":  
        limit = 3
        forms = SearchForm()
        search = request.GET.get("search")  
        category = request.GET.get("category")  
        tags = request.GET.getlist("tags") 
        ordering = request.GET.get("ordering") 
        page = request.GET.get("page") if request.GET.get("page") else 1
        if category:
            jobs = jobs.filter(category=category)
        if search: 
            jobs = jobs.filter( 
                Q(name__icontains=search) | Q(description__icontains=search) 
            ) 
        if tags:
            jobs = jobs.filter(tag__in=tags) 
        
        if ordering:
            jobs = jobs.order_by(ordering)
        max_page = range(jobs.count() // limit + 1)
        jobs = jobs[limit * (int(page) - 1) : limit * int(page)]
        return render(
            request,
            "jobs/jobs_list.html",
            context={"jobs": jobs, "form": forms, "max_page": max_page[1:]},
        )


        

      


@login_required(login_url ="/login/")
def jobs_detail(request, jobs_id): 
    if request.method == "GET":
       jobs = Jobs.objects.filter(id=jobs_id).first()
       return render(request, "jobs/jobs_detail.html", context={"jobs": jobs}) 

@login_required(login_url ="/login/")    
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

        
@login_required(login_url="/login/")
def jobs_update(request, jobs_id):
    if request.method == "GET":
        jobs = Jobs.objects.filter(id=jobs_id).first()
        form = JobsFrom(initial=jobs.__dict__)
        return render(request, "jobs/jobs_update.html", context={"form": form})
    elif request.method == "PUT":
        form = JobsFrom(request.PUT, request.FILES)
        if form.is_valid():
            jobs = Jobs.objects.filter(id=jobs_id).first()
            if request.user == jobs.user:
                jobs.name = form.cleaned_data["name"]
                jobs.description = form.cleaned_data["description"]
                jobs.price = form.cleaned_data["price"]
                jobs.photo = form.cleaned_data["photo"]
                jobs.save()

        return redirect(f"/jobs/{jobs_id}/")       


