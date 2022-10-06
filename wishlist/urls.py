from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_xml
from wishlist.views import show_json
from wishlist.views import show_xml_by_id
from wishlist.views import show_json_by_id

# Lab 03
from wishlist.views import register
from wishlist.views import login_user 
from wishlist.views import logout_user

# Lab 04
from wishlist.views import wishlist_ajax
from wishlist.views import show_wishlist_ajax


app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'), # http://localhost:8000/wishlist/
    path('xml/', show_xml, name='show_xml'), # http://localhost:8000/wishlist/xml/
    path('json/', show_json, name='show_json'), # http://localhost:8000/wishlist/json/
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'), # http://localhost:8000/wishlist/xml/<pk:id>
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), # 
    # Lab 03
    path('register/', register, name='register'), # http://localhost:8000/wishlist/register/
    path('login/', login_user, name='login'), # http://localhost:8000/wishlist/login/
    path('logout/', logout_user, name='logout'),
    # Lab 04
    path('ajax', wishlist_ajax, name='wishlist_ajax'), # http://localhost:8000/wishlist/ajax/
    path('ajax/submit', show_wishlist_ajax, name='show_wishlist_ajax'), # POST TEMBAK URL
]