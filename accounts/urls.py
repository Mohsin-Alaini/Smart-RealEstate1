from django.urls import path
from accounts import views
from .views import view , view2, view3,view4, AccountTypeView, CurrencyView

urlpatterns = [
    path('view1/',view),
    path('accounttype/', AccountTypeView.as_view(), name='account_type'),
    path('currencyview/', CurrencyView.as_view(), name='currencyview'),
    path('view1/<int:id>/',view2),
    path('view1/<path:path>/',view4),
    path('view1/<int:id>/<str:name>/',views.view3)
]
