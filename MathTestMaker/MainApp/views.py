from django.shortcuts import render
from django.conf import settings

def index( request ):
    context = {
        'key': settings.STRIPE_PUBLISHABLE_KEY,
    }
    print( context )
    return render( request, 'MainApp/index.html', context )
