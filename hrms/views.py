from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect

# Create your views here.


    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


