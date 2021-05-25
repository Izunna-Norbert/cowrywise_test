from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Uuuid
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import UuuidSerializer
import uuid
from django.utils import timezone
from rest_framework.response import Response
# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'GET':
        data ={
            'pub_date': timezone.now(),
            'uuid_char': uuid.uuid4()
        }
        serializer1 = UuuidSerializer(data=data)
        if serializer1.is_valid():
            serializer1.save()
            snippets = Uuuid.objects.order_by('-pub_date')[:5]
            serializer = UuuidSerializer(snippets, many=True)
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'POST':
        return JsonResponse(serializer.errors, status=400)