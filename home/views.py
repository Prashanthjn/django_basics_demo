from django.shortcuts import render
from django. http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render (request,'about.html')

def contact(request):
    return render(request,'contact.html')
  
def dynamic_url(request,id):
    print(f"this is the id which we got--> {id} ")
    return render(request,'dynamic_url.html')