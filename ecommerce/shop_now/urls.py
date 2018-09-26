from django.conf.urls import url
from shop_now import views as shop_now_views

from . import views

urlpatterns = [
    url(r"^shop/$", shop_now_views.shop_now, name="shop_now"),
]