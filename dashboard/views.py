from django.shortcuts import render
from django.views.generic import ListView
from .models import BugTracker


# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')



class BugListView(ListView):
    model = BugTracker