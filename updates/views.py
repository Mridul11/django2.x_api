import json 
from django.http import JsonResponse, HttpResponse 
from django.shortcuts import render
from django.views.generic import View   
from django.core.serializers import serialize 
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


class SerializeDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        # data = {
        #     "user" : obj.user.name ,
        #     "content" : obj.user.content 
        # }
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')


class SerializeListView(View):
    def get(self, request, *args, **kwargs):
        # qs = Update.objects.all()
        # data = serialize("json", qs, fields=('user', 'content'))
        # print(data)
        # json_data = data
        # data = {
        #     "user" : obj.user.name ,
        #     "content" : obj.user.content 
        # }
        # json_data = json.dumps(data)
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')

