from django.shortcuts import render
from django.shortcuts import redirect
from .models import Students

# Create your views here.


def student_form(request):
    message = ""
    if request.method == 'POST':
        Students.objects.create(
            name = request.POST['name'],
            roll_number = request.POST['roll'],
            student_class = request.POST['class'],
            age = request.POST['age'],
            parent_contact = request.POST['contact'],
            
        )
        message = 'student added sucessfully'
    return render(request,'student_form.html',{'message':message}) 
def student_list(request):
    student = student.object.all()
    return render(request,'student_list.html',{'student':student})   

def student_update(request,id):
    student = student.object.get(id = id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.roll_number = request.POST['roll']
        student.student_class = request.POST['class']
        student.age = request.POST['age']
        student.parent_contact = request.POST['contact']
        student.save()
        return redirect('/modelsapp/list/')