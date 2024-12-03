from django.shortcuts import render

def index(request):
    template = 'homepage/index.html'
    context = {
        'title': 'Welcome to the Homepage or hell)))',
        'message': 'This is the homepage of my Django project.',
    }
    return render(request, template, context)