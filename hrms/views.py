from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect

# Create your views here.


def home(request):
     context = {}
     return render(request,"home.html",context)
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


