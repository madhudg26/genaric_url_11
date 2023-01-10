from django.shortcuts import render

# Create your views here.
def mallareddy(request):
    return render(request,'gen1.html')

def slogan(request):
    return render(request,'gen2.html')