from django.http import HttpResponse


# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World!")


def hello_china(request):
    return HttpResponse("Hello China!")
