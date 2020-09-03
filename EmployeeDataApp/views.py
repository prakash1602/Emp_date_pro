from django.shortcuts import render, redirect
from .models import EmployeeData


def displaying_data(request):
    employees = EmployeeData.objects.all()
    return render(request, 'displaying_data.html', {'employees': employees})


def add_employee(request):
    return render(request, 'add_employee.html')


def save_data(request):
    fname1 = request.POST.get('fname')
    lname1 = request.POST.get('lname')
    mobile1 = request.POST.get('mobile')
    email1 = request.POST.get('email')
    salary1 = request.POST.get('salary')
    exp1 = request.POST.get('exp')
    loc1 = request.POST.get('loc')
    company1 = request.POST.get('company')

    data1 = EmployeeData(
        first_name=fname1,
        last_name=lname1,
        mobile=mobile1,
        email=email1,
        salary=salary1,
        exp=exp1,
        location=loc1,
        company=company1
    )
    data1.save()
    return redirect('/')


def update_employee(request, pk):
    employee = EmployeeData.objects.get(id=pk)
    return render(request, 'update_employee.html', {'employee': employee})


def save_update_data(request,pk):
    employee = EmployeeData.objects.get(id=pk)

    employee.first_name = request.POST.get('fname')
    employee.last_name = request.POST.get('lname')
    employee.mobile = request.POST.get('mobile')
    employee.email = request.POST.get('email')
    employee.salary = request.POST.get('salary')
    employee.exp = request.POST.get('exp')
    employee.location = request.POST.get('loc')
    employee.company = request.POST.get('company')
    employee.save()
    return redirect('/')


def delete_employee(request, pk):
    employee = EmployeeData.objects.get(id=pk)
    employee.delete()
    return redirect('/')
