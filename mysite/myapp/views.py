import datetime

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import datetime


def hello(request):
    today = datetime.datetime.now().date()

    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "hello.html", {"today": today, "days_of_week": daysOfWeek})
