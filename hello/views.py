from django.http import HttpResponse

def hello_world(request):
    return HttpResponse(b"Hello, World!")
