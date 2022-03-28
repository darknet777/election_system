from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import EVS_Admin, Candidate, Voter

def index(request):
    return render(request, 'election_app/index.html')

def statistic(request):
    candidate = Candidate.objects.all().values()
    template = loader.get_template('election_app/statistic.html')
    context = {
        'candidate': candidate,
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    return render(request, 'election_app/contact.html')
