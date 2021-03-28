import io
from api.models import Student
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
import json
from django.forms.models import model_to_dict


def get_view_old(request):
    if request.method == "GET":
        json_data = request.body
        # stream json dt
        stream = io.BytesIO(json_data)
        # parse to py
        py_data = JSONParser().parse(stream)
        # get required item from py dict
        id = py_data.get('id', None)
        if id is not None:
            # get complex querySet
            complex_obj = Student.objects.get(id=id)
            # serializer complex -> native py
            serializer = StudentSerializer(complex_obj)
            # render py -> json
            json_data = JSONRenderer().render(serializer.data)
            # return json
            return HttpResponse(json_data, content_type="application/json")
        # get complex querySets
        stu = Student.objects.all().order_by('-id')
        # serializer complex -> native py
        serializer = StudentSerializer(stu, many=True)
        # render py -> json
        json_data = JSONRenderer().render(serializer.data)
        # return json
        return HttpResponse(json_data, content_type="application/json")


def get_view(request):
    """
    REST API Response, for sending data back in the json format.
    """
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id', None)
        if id is not None:
            complex_obj = Student.objects.get(id=id)
            serializer = StudentSerializer(complex_obj)
            return JsonResponse(data=serializer.data, safe=False)
        stu = Student.objects.all().order_by('-id')
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(data=serializer.data, safe=False)
