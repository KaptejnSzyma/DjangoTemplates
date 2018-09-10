from django.shortcuts import render


def index(request):
    return render(request, 'BasicApp/index.html')


def other(request):
    return render(request, 'BasicApp/index.html')


def relative(request):
    return render(request, 'BasicApp\relative_url_templates.html')
