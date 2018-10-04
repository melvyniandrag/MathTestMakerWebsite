from django.urls import path
from . import views

app_name = 'MainApp'

urlpatterns = [
    path( '', views.index, name='index' ),
    path( 'quickstartCategories/', views.quickstartCategories, name="quickstartCategories" ),
    path( 'quickstartQuestions/', views.quickstartQuestions, name = 'quickstartQuestions' ),
    path( 'quickstartGenerate/', views.quickstartGenerate, name='quickstartGenerate' ),
    path( 'quickstartDownload/', views.quickstartDownload, name='quickstartDownload' ),
    path( 'charge/', views.charge, name='charge' ),
]
