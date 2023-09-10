
# Create your views here.
from django.shortcuts import render
import datetime

def main(request):
    current_server_time = datetime.datetime.now()
    return render(request, 'main.html', {'current_time': current_server_time})
