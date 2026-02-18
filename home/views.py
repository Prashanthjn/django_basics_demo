from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import random


def index(request):
    lucky_number=random.randint(100,999)
    vegetables=['tomato','potato','chilli']
    for vegetable in vegetables:
        print(vegetable)

    context={"lucky_number" : lucky_number,"vegetables": vegetable}
    return render (request, 'index.html',context)


def about(request):
    return render (request,'about.html')

def contact(request):
    return render(request,'contact.html')
  
def dynamic_url(request,id):
    print(f"this is the id which we got--> {id} ")
    return render(request,'dynamic_url.html',context={"id":id,"name":"prashanth"}) 