from django.shortcuts import render

def index(request):
    return render(request, 'election_app/index.html')

def statistic(request):
    return render(request, 'election_app/statistic.html')

def contact(request):
    return render(request, 'election_app/contact.html')
