import pprint
import stripe
from django.shortcuts import render
from django.conf import settings
from mathtestmaker import MathTestMaker as TestMaker

stripe.api_key = settings.STRIPE_SECRET_KEY # new

def index( request ):
    context = {
        'key': settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render( request, 'MainApp/index.html', context )

def quickstartCategories( request ):
    testmaker = TestMaker()
    categories = testmaker.getQuestionCategories()
    context = {
        "categories": categories,
    }
    return render( request, 'MainApp/quickstartCategories.html', context )

def quickstartQuestions( request ):
    if request.method == "POST":
        testmaker = TestMaker()
        selectedCategories = request.POST.getlist( "selectedCategory" )
        context = {}
        for category in selectedCategories:
            generator = testmaker.questionGenerators[category]
            questions = generator.getQuestionNames()
            context[category] = questions
        return render( request, 'MainApp/quickstartQuestions.html', context )
    else:
        return index( request )

def quickstartGenerate( request ):
    return index( request )

def getQuestions( category, questionNames ):
    # TBD Error Handling
    # TBD Accept params for numChoices and points
    testmaker = TestMaker()
    generator = testmaker.questionGenerators[ category ]
    defaultNumChoices = 4
    defaultPoints = 1
    ret = []
    for name in questionNames:
        ret.append( generator.getQuestion( name, defaultNumChoices, defaultPoints ) )
    return ret

def quickstartDownload( request ):
    if request.method == "POST":
        linearQuestionNames = request.POST.getlist("linear_equations")
        #quadraticQuestions = ...
        #derivativeQuestions = ... 
        #etc...
        generatedQuestions = []
        generatedQuestions += getQuestions( "linear_equations", linearQuestionNames )
        #generatedQuestions += getQuestions( "quadratic_equations", quadraticQuestionNames )
        #generatedQuestions += getQuestions( "derivatives", derivativeQuestionNames )
        #etc.
        context = {
            "generatedQuestions": [ str( question ) for question in generatedQuestions ]
        }
        return render( request, 'MainApp/quickstartDownload.html', context )
    else:
        return index( request )

def charge( request ):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='Thanks for Your Donation!',
            source=request.POST['stripeToken']
        )
        return render(request, 'MainApp/charge.html')

def donate( request ):
    return render( request, 'MainApp/donate.html')
