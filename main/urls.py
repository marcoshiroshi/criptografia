from django.urls import path
from main.views import MainView, cripto, descripto

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('ajax/cripto/', cripto, name='ajax_cripto'),
    path('ajax/descripto/', descripto, name='ajax_descripto')
    ]
