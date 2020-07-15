from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'testapp/index.html')

def register(request):
    return render(request,'testapp/register.html')

# core/views.py


from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
  return render(request, 'login.html')

@login_required
def home(request):
  return render(request, 'home.html')

def details(request):
  return render(request, 'testapp/portfolio-details.html')
