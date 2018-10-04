import stripe
from django.shortcuts import render
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY # new

def index( request ):
    context = {
        'key': settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render( request, 'MainApp/index.html', context )

def quickstartCategories( request ):
    context = {}
    return render( request, 'MainApp/quickstartCategories.html', context )

def quickstartQuestions( request ):
    context = {}
    return render( request, 'MainApp/quickstartQuestions.html', context )

def quickstartGenerate( request ):
    context = {}
    return render( request, 'MainApp/quickstartGenerate.html', context )

def quickstartDownload( request ):
    context = {}
    return render( request, 'MainApp/quickstartDownload.html', context )

def charge( request ):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='Thanks for Your Donation!',
            source=request.POST['stripeToken']
        )
        return render(request, 'MainApp/charge.html')
