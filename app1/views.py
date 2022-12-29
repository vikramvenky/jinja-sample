from django.shortcuts import render

# Create your views here.
def jinja(request):
    dict={'mobilenumber':[9989132102]}
    return render(request,'jinja.html',dict)

