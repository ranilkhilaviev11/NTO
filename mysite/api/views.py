from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import PersonInfo
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    return HttpResponse("<h3>Hello world!</h3>")


def GetPersonInfo(request):
    persons = PersonInfo.objects.all()
    str1 = ''
    i = 1
    for per in persons:
        str1 += '<h3>Person' + str(i) + '</h3>'
        str1 += '<p>FirstName: ' + per.FirstName + '</p>'
        str1 += '<p>LastName: ' + per.LastName + '</p>'
        str1 += '<p>MiddleName: ' + per.MiddleName + '</p>'
        str1 += '<p>Phone: ' + str(per.Phone) + '</p>'
        str1 += '<p>Birthday: ' + str(per.Birthday) + '</p>'
        i += 1

    return HttpResponse(str1)


class PersonForm(ModelForm):
    class Meta:
        model = PersonInfo
        fields = ['FirstName', 'LastName', 'MiddleName', 'Description', 'Phone', 'Birthday',
                  'Country', 'City', 'Position', 'HaveChildren']


def person_list(request, template_name='persons/person_list.html'):
    person = PersonInfo.objects.all()
    return render(request, template_name, {'persons': person})


def person_view(request, pk, template_name='persons/person_detail.html'):
    person = get_object_or_404(PersonInfo, pk=pk)
    return render(request, template_name, {'person':person})


def person_edit(requst, pk, template_name='persons/person_form.html'):
    person = get_object_or_404(PersonInfo, pk=pk)
    form = PersonForm(requst.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(requst, template_name, {'form': form})


def person_create(request, template_name='persons/person_form.html'):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return  redirect('person_list')

    return render(request, template_name, {'form': form})


def person_delete(request, pk, temlate_name='persons/person_confirm_delete.html'):
    person= get_object_or_404(PersonInfo, pk=pk)
    if request.method == 'POST':
        person.delete()
        return  redirect('person_list')
    return render(request, temlate_name, {'object': person.LastName})


class PersonList(ListView):
    model = PersonInfo


class PersonView(DetailView):
    model = PersonInfo


class PersonCreate(CreateView):
    model = PersonInfo
    fields = ['FirstName', 'LastName', 'MiddleName', 'Description', 'Phone', 'Birthday']
    success_url = reverse_lazy('person_list')


class PersonUpdate(UpdateView):
    model = PersonInfo
    fields = ['FirstName', 'LastName', 'MiddleName', 'Description', 'Phone', 'Birthday']
    success_url = reverse_lazy('person_list')


class PersonDelete(DetailView):
    model = PersonInfo
    success_url = reverse_lazy('person_list')
