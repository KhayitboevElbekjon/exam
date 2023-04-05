
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
   openapi.Info(
      title="exam drf API",
      default_version='v1',
      description="exam drf API",
      contact=openapi.Contact("Xayitboeyev Elbekjon <backenddevolpment@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
from rest_framework.routers import DefaultRouter

from rest_framework import routers
from django.contrib import admin
from django.urls import path,include
from asosiy.views import *
router=DefaultRouter()
router.register('suv',SuvAPIView)
router.register('mijoz',MijozAPIView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('buyurtma/',BuyurtmaAPIView.as_view()),
    path('admin/',AdminAPIView.as_view()),
    path('haydovchilar/',HaydovchiAPIView.as_view()),
    path('haydovchi/<int:son>',HaydovchiDetailView.as_view()),
    path('get_token/', TokenObtainPairView.as_view()),
    path('token_yangilash/', TokenRefreshView.as_view()),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0))

]
