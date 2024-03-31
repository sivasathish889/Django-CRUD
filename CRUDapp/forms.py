from CRUDapp.models import Student
from django.forms import ModelForm
class Stu_Form(ModelForm):
    
    class Meta:
        model = Student
        fields = "__all__"
