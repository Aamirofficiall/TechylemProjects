
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.conf.urls import url 
from .views import *
router = DefaultRouter()
router.register('',ImageView)


urlpatterns = [
     path('',include(router.urls)),
    # path('', views.ImageView.as_view()),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)