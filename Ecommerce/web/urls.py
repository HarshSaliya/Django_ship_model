from django.urls import path ,include
from rest_framework import routers
from web.views import *

router=routers.DefaultRouter()
router.register(r'country' ,CountryViewSet)
router.register(r'supplier',SupplierViewSet)
router.register(r'buyer', BuyerViewSet)
router.register(r'ports',PortsViewSet)
router.register(r'item' ,ItemViewSet)
router.register(r'itemtype' , ItemTypeViewSet)
router.register(r'order' , orderViewSet)
router.register(r'orderdetail' ,OrderDetailViewSet)
router.register(r'shipment' ,ShipmentDetailViewSet)
router.register(r'shipline',ShiplineViewSet)
router.register(r'shipmentdetails',ShipmentDetailViewSet)




urlpatterns = [
    path('', include(router.urls)),
]