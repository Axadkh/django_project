from django.shortcuts import render, render_to_response
from django.http import HttpResponse
# Create your views here.
from django.template import loader

from people.models import People


def people(req):
    employees = People.objects.all()
    return render(req, 'Employee.html', {'employees': employees})


def employee(req):

    return HttpResponse('employe')


