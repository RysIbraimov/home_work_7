from django.shortcuts import render
import json
from  django.http import HttpResponse
# Create your views here.
from .models import Employee,JobTitle


def job_title_list(request):
    job = JobTitle.objects.all()
    job_data = []

    for data in job:
        obj = {'job title' : data.job_t, 'department' : data.department}
        job_data.append(obj)

    return HttpResponse(json.dumps(job_data))

def add_job_title(request):
    new_job_title = request.GET.get('job_t')
    new_department = request.GET.get('department')
    create_job_t = JobTitle.objects.create(job_t=new_job_title,department=new_department)
    obj = {'job title' : create_job_t.job_t, 'department' : create_job_t.department}

    return HttpResponse(json.dumps(obj))

def get_employee(request):
    emps = Employee.objects.all()
    data = []

    for emp in emps:
        obj = {'position': emp.job_title_id.job_t, 'salary': emp.salary,
               'name': emp.name, 'birth_date': str(emp.birth_date)}
        data.append(obj)

    return  HttpResponse(json.dumps(data))

def add_employee(request):
    name = request.GET.get('name')
    salary = request.GET.get('salary')
    position = request.GET.get('job_title_id')
    birth_date = request.GET.get('birth_date')
    employee = Employee.objects.create(name=name, salary=salary, job_title_id=position,birth_date=birth_date)
    obj = {'salary': salary, 'birth_date':employee.birth_date}
    return HttpResponse(json.dumps(obj))


