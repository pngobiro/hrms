from django.shortcuts import render

# Create your views here.
def list_employees(request):
    return render(request,"list.html")