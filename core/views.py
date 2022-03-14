from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import pyrebase



from django.core.files.storage import default_storage
from django.contrib import messages
# import pyrebase
# import os




from .models import Api
from .serializers import ApiSerializer
# Create your views here.

config = {
    "apiKey": "AIzaSyDBdTQBEB4t8eDSUf-8aukOSTxtWZ58e48",
    "authDomain": "test-a8c66.firebaseapp.com",
    "projectId": "test-a8c66",
    "storageBucket": "test-a8c66.appspot.com",
    "messagingSenderId": "523338301684",
    "appId": "1:523338301684:web:e6b96c979dd60001d2dea1",
    "measurementId": "G-8J9040JVSX",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()


class ApiView(viewsets.ModelViewSet):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
    
   

def main(request):
    if request.method == 'POST':
        file = request.FILES['file']
        file_save = default_storage.save(file.name, file)
        storage.child("files/" + file.name).put("media/" + file.name)
        delete = default_storage.delete(file.name)
        messages.success(request, "File upload in Firebase Storage successful")
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')