
# Create your views here.
from django.shortcuts import render
import datetime
from django.http import JsonResponse


def main_view(request):
    current_server_time = datetime.datetime.now()
    return render(request, 'main.html', {'current_server_time': current_server_time})


def get_date_time(request):
    current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # print(f"IN get date time{current_date_time}")
    return JsonResponse({'dateTime': current_date_time})