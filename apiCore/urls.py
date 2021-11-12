from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('payment',views.paymentViewSet)
router.register('order',views.orderViewSet)
router.register('paymentType',views.paymentTypeViewSet)
#router.register(r'messages', views.messageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]