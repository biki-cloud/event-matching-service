from django.urls import path

from . import views

urlpatterns = [
    path('detail/<int:pk>', views.VendorDetailView.as_view(), name="vendor_detail"),
    path('update/<int:pk>', views.VendorUpdateView.as_view(), name='vendor_update'),
]