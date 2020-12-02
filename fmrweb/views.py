from django.shortcuts import render


def index(request):
    return render(request, 'fmrweb/index.html')

def faq(request):
    return render(request, 'fmrweb/faq.html')


def about_integrator_chains(request):
    return render(request, 'fmrweb/integrator_chains.html')


def event_icra2016(request):
    return render(request, 'fmrweb/events/challenge-icra2016.html')

def event_icra2015(request):
    return render(request, 'fmrweb/events/workshop-icra2015.html')
