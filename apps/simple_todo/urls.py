from django.urls import path,include
from .views import (
    TasksModelViewSet,
    TasksAPIViewSet,
    TasksModelGenericView,
    TasksModelGenericView2,
    )
from rest_framework.routers import DefaultRouter
router= DefaultRouter()
router.register(
    'Tasks',TasksModelViewSet,basename='SomethingViewSet'
)
# router.register(
#     'Types',SomethingViewSet2,basename='ViewSet2'
# )

urlpatterns=[
    path('ModelViewSet/',include(router.urls)),
    path('APIViewSet/',TasksAPIViewSet.as_view()),
    path('APIViewSet/<int:id>/',TasksAPIViewSet.as_view()),

    path('GenericView/',TasksModelGenericView.as_view()),
    path('GenericView/<int:pk>/',TasksModelGenericView2.as_view()),
]
#+router.urls