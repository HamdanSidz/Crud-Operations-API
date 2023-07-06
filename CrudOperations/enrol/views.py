from django.shortcuts import render
from .forms import employee_reg
from .models import employees
from django.http import HttpResponseRedirect
from django.db.models import Q
# Create your views here.


def addshow(request):
    if request.method == "POST":
        form = employee_reg(request.POST)
        if form.is_valid():
            nm = form.cleaned_data["name"]
            dp = form.cleaned_data["department"]
            po = form.cleaned_data["position"]
            sl = form.cleaned_data["salary"]
            emp = employees(name=nm, department=dp, position=po, salary=sl)
            emp.save()
            return HttpResponseRedirect('/')
        else:
            form = employee_reg()
            emp = employees.objects.all()
            return render(request, 'enrol/add&show.html', {"form": form, "message": "Information Enter is not valid", "inst": emp})
    else:
        form = employee_reg()
        emp = employees.objects.all()
        return render(request, 'enrol/add&show.html', {"form": form, "inst": emp})


def delete(request, id):
    if request.method == "POST":
        emp = employees.objects.get(pk=id)
        emp.delete()
        return HttpResponseRedirect('/')


def update(request, id):
    if request.method == "POST":
        emp = employees.objects.get(pk=id)
        form = employee_reg(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, 'enrol/update.html', {"message": "Information Enter is not valid or incomplete"})
    else:
        emp = employees.objects.get(pk=id)
        form = employee_reg(instance=emp)
        return render(request, "enrol/update.html", {"form": form})


def search(request):
    if request.method == "GET":
        query = request.GET["query"]
        if query:
            emp = employees.objects.filter(
                Q(name__icontains=query) or Q(department__icontains=query))
            return render(request, "enrol/searchresult.html", {"emp": emp})
        else:
            return HttpResponseRedirect("/")
