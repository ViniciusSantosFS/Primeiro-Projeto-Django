from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.forms import ModelForm

class personForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name','last_name','age','salary','bio']


def person_list(request):
    persons = Person.objects.all()
    person = {'list' : persons}
    return render(request,'list.html', person)

def person_create(request,template_name='create.html'):
    form = personForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request,template_name,{'form':form})



def person_edit(request,pk,template_name = 'create.html'):
    persons = get_object_or_404(Person,pk=pk)
    if request.method == "POST":
        form = personForm(request.POST, instance = persons)
        if form.is_valid():
            persons = form.save()
            return redirect('person_list')

    else:
        form = personForm(instance = persons)

    return render(request,template_name,{'form': form})


def person_remove(request,pk,template_name='remove.html'):
    persons = Person.objects.get(pk=pk)
    if request.method == "POST":
        persons.delete()
        return redirect('person_list')
    return render(request,template_name,{'persons':persons})




# Create your views here.
