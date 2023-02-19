import imp
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request,'index.html')

def all_emp(request):
    emp = Employe.objects.all()
    print(emp)
    return render(request,'all_emp.html',context={"data":emp})


def add_emp(request):
    form = EmployeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(index)
    return render(request,'add_emp.html',context={'form':form})


def filter_emp(request):
    
    #form = EmployeForm(request.POST or None)
    if request.method == 'POST':
        dept = request.POST.get("department")
        role = request.POST.get("role")
        name = request.POST.get("name")
        location = request.POST.get("location")
        emp = Employe.objects.all()
        if name:
            emp = emp.filter(Q(first_name__icontains = name ) | Q(last_name__icontains = name ))

        if role:
            emp = emp.filter(role__name__icontains = role)
        
        if location:
            emp = emp.filter(department__location__icontains = location)

        if dept: 
            emp = emp.filter(department__name__icontains = dept)  #To filter with foreign key we use __ to access the other model  


        context = {'data':emp}
        return render(request,'all_emp.html',context)
    return render(request,'filter_emp.html')
    

def remove_emp(request,id):
    data = Employe.objects.get(id=id)
    data.delete()
    return redirect(all_emp)
    pass
