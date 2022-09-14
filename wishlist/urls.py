from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_xml
from wishlist.views import show_json

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'), # http://localhost:8000/wishlist/
    path('xml/', show_xml, name='show_xml'), # http://localhost:8000/wishlist/xml/
    path('json/', show_json, name='show_json'), # http://localhost:8000/wishlist/json/
]