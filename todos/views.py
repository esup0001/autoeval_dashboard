from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': 'eko',
    }
    return render(request, 'index.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')


def table(request):
    return render(request, 'table.html')
