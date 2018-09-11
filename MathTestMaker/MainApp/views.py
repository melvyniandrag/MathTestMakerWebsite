import stripe
from django.shortcuts import render
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY # new

def index( request ):
    context = {
        'key': settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render( request, 'MainApp/index.html', context )

def charge( request ):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'MainApp/charge.html')
