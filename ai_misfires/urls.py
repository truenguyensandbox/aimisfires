from django.urls import path, include

urlpatterns = [
    path('', include('debugger.urls')),  # Send everything to your app
]
 