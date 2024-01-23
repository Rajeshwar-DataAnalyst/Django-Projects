from django.shortcuts import render

# Create your views here.

def aktu_form(request):
  return render(request,'form/index.html')