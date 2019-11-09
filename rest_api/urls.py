
from django.contrib import admin
from django.urls import path
from updates.views import json_example_view , JsonCBV, JsonCBV2 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', json_example_view ),
    path('cbv/', JsonCBV.as_view() ),
    path('cbv2/', JsonCBV2.as_view() )


]
