from django.shortcuts import render
from django.views.decorators.http import require_safe, require_POST


def index(request):
    return render(request, 'fmrweb/index.html')

def faq(request):
    return render(request, 'fmrweb/faq.html')


def norm_index(request):
    return render(request, 'fmrweb/norm-index.html')


def about_integrator_chains(request):
    return render(request, 'fmrweb/integrator_chains.html')

def about_dubins_traffic(request):
    return render(request, 'fmrweb/dubins_traffic.html')


def event_icra2016(request):
    return render(request, 'fmrweb/events/challenge-icra2016.html')

def event_icra2015(request):
    return render(request, 'fmrweb/events/workshop-icra2015.html')


def submit(request):
    return render(request, 'fmrweb/submit.html')
