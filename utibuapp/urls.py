from django.urls import path
from . import views, api

urlpatterns = [
    # Views URLs
    path('place_order/', views.place_order, name='place_order'),
    path('order_history/', views.order_history, name='order_history'),
    path('statement/', views.statement, name='statement'),

    # API URLs
    path('api/medications/', api.MedicationListCreateAPIView.as_view(), name='medication-list-create'),
    path('api/orders/', api.OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('api/statements/', api.StatementListAPIView.as_view(), name='statement-list'),
]