from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_xml
from wishlist.views import show_json
from wishlist.views import show_xml_by_id
from wishlist.views import show_json_by_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'), # http://localhost:8000/wishlist/
    path('xml/', show_xml, name='show_xml'), # http://localhost:8000/wishlist/xml/
    path('json/', show_json, name='show_json'), # http://localhost:8000/wishlist/json/
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'), # http://localhost:8000/wishlist/xml/<pk:id>
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), # http://localhost:8000/wishlist/json/<pk:id>
]