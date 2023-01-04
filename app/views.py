from django.shortcuts import render

# Create your views here.
def specificfile(request):
    return render(request,'specificfile.html')