from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def ADM_LOGIN(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return HttpResponse("Welcome, Admin!") 
            else:
                return HttpResponse("Invalid username or password.")
        else: 
            return HttpResponse("Invalid username or password.")
    
  
    return render(request, 'Login.html')  
    
