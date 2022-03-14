from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('apis',views.ApiView)

urlpatterns = [
    path('',include(router.urls)),
    path('media/',views.main),
]
