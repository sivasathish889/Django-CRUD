from django.shortcuts import render,redirect
from CRUDapp.models import Student
from CRUDapp.forms import Stu_Form

# Create your views here.
#  Form
def Student_view(request):
    student_details=Student.objects.all()
    context={"student_details": student_details}
    return render(request,"base.html", context)

# Form Details
def Form_view(request):
    student_forms=Stu_Form()
    context={"student_forms":student_forms}
    if request.method=="POST":
        stu_form=Stu_Form(request.POST)
        if stu_form.is_valid():
            stu_form.save()
            return redirect("/")
    return render(request,"index.html", context)

# Delete Form details
def Delete_view(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect("/")
    
# Update Form
def Update_view(request,id):
    stu=Student.objects.get(id=id)
    form=Stu_Form(request.POST or None, instance=stu)
    context={"form":form}
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request,"update.html", context)