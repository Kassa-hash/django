from django.shortcuts import render
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def create_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        position = request.POST.get('position')
        department = request.POST.get('department')
        salary = request.POST.get('salary')

        Employee.objects.create(
            name=name,
            email=email,
            position=position,
            department=department,
            salary=salary
        )
    return render(request, 'create_employee.html')

def update_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.position = request.POST.get('position')
        employee.department = request.POST.get('department')
        employee.salary = request.POST.get('salary')
        employee.save()
    return render(request, 'update_employee.html', {'employee': employee})

def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        employee.delete()
    return render(request, 'delete_employee.html', {'employee': employee})
