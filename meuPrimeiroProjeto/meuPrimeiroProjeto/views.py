from django.http import HttpResponse
def hello (request):
    return HttpResponse ("Ola Mundo");

def numero (request, year):
    return HttpResponse('O ano enviado foi: ' + str(year))