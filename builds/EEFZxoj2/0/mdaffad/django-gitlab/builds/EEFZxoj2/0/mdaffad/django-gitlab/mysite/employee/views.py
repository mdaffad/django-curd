from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from mysite.settings import STATIC_URL


# Create your views here.
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/employee/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'employee/index.html', {'STATIC_URL': STATIC_URL,'form': form})


def show(request):
    employees = Employee.objects.all()
    return render(request, "employee/show.html", {'STATIC_URL': STATIC_URL, 'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'employee/edit.html', {'STATIC_URL': STATIC_URL,'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/employee/show")
    return render(request, 'employee/edit.html', {'STATIC_URL': STATIC_URL, 'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/employee/show")
