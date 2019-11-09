
from django.contrib import admin
from django.urls import path
from updates.views import json_example_view , JsonCBV, JsonCBV2 , SerializeListView, SerializeDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', json_example_view ),
    path('cbv/', JsonCBV.as_view() ),
    path('cbv2/', JsonCBV2.as_view() ),
    path('serializelistview/', SerializeListView.as_view() ),
    path('serializedetailview/', SerializeDetailView.as_view() )


]
