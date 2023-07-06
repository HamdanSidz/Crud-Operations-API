from django import forms
from .models import employees

class employee_reg(forms.ModelForm):
    class Meta:
        model = employees
        fields = ["name","department","position","salary"]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "department":forms.TextInput(attrs={"class":"form-control"}),
            "position":forms.TextInput( attrs={"class":"form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"})
        }





    


