from django.shortcuts import render

# Create your views here.

def testmodule(request):
    return render(request,'hello.html')