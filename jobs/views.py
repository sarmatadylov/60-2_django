from django.shortcuts import render 
from .models import Jobs
# Create your views here. 


"""
select * form jobs;
"""

"""
select * from jobs ILIKE where = "%phone%"
"""



def home(request):
    return render(request, "base.html")


def jobs_list(request):
    jobs = Jobs.objects.all()
    return render(request, "jobs/jobs_list.html", context={"jobs": jobs})


def jobs_detail(request, jobs_id):
    jobs = Jobs.objects.filter(id=jobs_id).first()
    return render(request, "jobs/jobs_detail.html", context={"jobs": jobs})


