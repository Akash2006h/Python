from django.shortcuts import render,HttpResponse
def index(request):
    return HttpResponse("This is Homepage")
# Create your views here.
