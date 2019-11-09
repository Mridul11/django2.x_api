import json 
from django.http import JsonResponse, HttpResponse 
from django.shortcuts import render
from django.views.generic import View   
from rest_api.mixins import JsonResponseMixin
from .models import Update 

# def detail_view(request, response):
#     return render() 

def json_example_view(request):
    data = {  
        "count" : 11,
        "content" : "some new content"
    }
    # json_data = json.dumps(data)
    return JsonResponse(data)
    # return HttpResponse(json_data)

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {  
            "count" : 11,
            "content" : "some new content"
            }
        # json_data = json.dumps(data)
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count" : 11,
            "content" : "some new content"
        }
        return self.render_to_json_response(data)

