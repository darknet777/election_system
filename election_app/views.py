from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template import loader
from .models import Candidate, Voter

def index(request):
    return render(request, 'election_app/index.html')

def validation(request):
    if request.method == 'POST':
        dpt = request.POST['no_dpt']
        object = Voter.objects.filter(no_dpt=dpt, vote='1').exists()
        if object == True:
            return redirect('election-voting')
        else:
            messages.error(request, 'Nomor DPT tidak terdaftar! Silakan coba lagi.')
            return redirect('election-home')

def voting(request):
    candidate = Candidate.objects.all().values()
    if request.method == 'POST':
        x = request.POST['name']
        y = Candidate.objects.filter(id=x)
        if y == True:
            update = Candidate()

    context = {
        'candidate': candidate,
    }
    return render(request, 'election_app/voting.html', context)

def voterecord(request, id):
    x = Candidate.objects.get(id=id)
    votes = 1
    x.votes += votes
    x.save()
    return HttpResponseRedirect(reverse('election-statistic'))

def statistic(request):
    candidate = Candidate.objects.all().values()
    template = loader.get_template('election_app/statistic.html')
    context = {
        'candidate': candidate,
    }
    return HttpResponse(template.render(context, request))

def about(request):
    return render(request, 'election_app/about.html')
