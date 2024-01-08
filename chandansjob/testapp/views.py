from django.shortcuts import render
from testapp.models import Hydjobs

# Create your views here.
def homepage_view(request):
    return render(request,'testapp/index.html')

def hydjobs_view(request):
    jobs_list = Hydjobs.objects.all()
    my_dict = {'jobs_list': jobs_list}
    return render(request,'testapp/hydjobs.html',my_dict)

def punejobs_view(request):
    jobs_list = Punejobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',my_dict)


def Bangjobs_view(request):
    jobs_list = Bangjobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',my_dict)