from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from . import models


def IndexView(request):
    return render(request,'index.html')


class SchoolListView(ListView):
    context_object_name='Schools'
    model=models.School
    template_name='school_list.html'

class SchoolDetailView(DetailView):
    context_object_name='schooldet'
    model=models.School
    template_name='school_detail.html'

class SchoolCreateView(CreateView):
    fields=('name','principal','location')
    model=models.School
    template_name='school_form.html'

class SchoolUpdateView(UpdateView):
    fields=('name','principal')
    model=models.School
    template_name='school_form.html'





# Create your views here.
