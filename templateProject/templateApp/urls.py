
from django.urls import path
from templateApp.views  import home_view

urlpatterns = [ 
    path('demo/',home_view)
]
