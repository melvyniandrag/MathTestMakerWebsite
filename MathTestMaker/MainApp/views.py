from django.shortcuts import render

def index( request ):
    context = {}
    return render( request, 'MainApp/index.html', context )
