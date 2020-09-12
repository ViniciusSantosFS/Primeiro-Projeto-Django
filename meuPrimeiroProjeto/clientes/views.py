from django.shortcuts import render
from .models import Person

def persons_list(request):
    persons = Person.objects.all()
    return render(request,'person.html', {'persons'}: persons)
# Create your views here.
