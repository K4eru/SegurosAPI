from django.db.models import base
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('company',views.companyViewSet,basename='companies')
router.register('order',views.orderViewSet,basename='orders')
router.register('training',views.trainingViewSet,basename='trainings')
router.register('checklist',views.checklistViewSet,basename='checklists')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]