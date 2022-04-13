from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from .models import EVS_Admin, Candidate, Voter

def index(request):
    return render(request, 'election_app/index.html')

def validation(request):
    if request.method == 'POST':
        dpt = request.POST.get('no_dpt')
        obj = Voter.objects.filter(no_dpt=dpt).exists()
        if obj == True:
            return HttpResponse('valid')
        else:
            return redirect('election-voting')

def voting(request):
    candidate = Candidate.objects.all().values()
    template = loader.get_template('election_app/voting.html')
    context = {
        'candidate': candidate,
    }
    return HttpResponse(template.render(context, request))

def statistic(request):
    candidate = Candidate.objects.all().values()
    template = loader.get_template('election_app/statistic.html')
    context = {
        'candidate': candidate,
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    return render(request, 'election_app/contact.html')
