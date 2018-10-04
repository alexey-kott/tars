from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'panel/index.html', {})


def accounts(request):
    return render(request, 'panel/accounts.html', {})


def views(request):
    return render(request, 'panel/views.html')


def subscribes(request):
    return render(request, 'panel/subscribes.html')
