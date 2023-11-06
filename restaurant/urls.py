from django.urls import path
from .views import Dashboard, OrderDetails
# na wa 0 




urlpatterns = [ 
    path("dashboard/", Dashboard.as_view(), name='dashboard'),
    path("orders/<int:pk>/", OrderDetails.as_view(), name='order-details'),
] 
