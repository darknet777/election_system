from django.shortcuts import render

def index(request):
    return render(request, 'election_app/index.html')

def about(request):
    return render(request, 'election_app/about.html')

def contact(request):
    return render(request, 'election_app/contact.html')
