from django.shortcuts import render


def index(request):
    context_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'BasicApp/index.html', context_dict)


def other(request):
    return render(request, 'BasicApp/other.html')


def relative(request):
    return render(request, 'BasicApp/relative_url_templates.html')
