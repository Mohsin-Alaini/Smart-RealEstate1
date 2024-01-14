from django.urls import path
from accounts import views
from .views import view , view2, view3

urlpatterns = [
    path('view1/',view),
    path('view1/<int:id>/',view2),
    path('view1/<int:id>/<str:name>/',views.view3)
]
