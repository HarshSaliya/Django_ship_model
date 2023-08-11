from django.shortcuts import render
from rest_framework import viewsets
from web.models import *
from web.serializers import *


class CountryViewSet(viewsets.ModelViewSet):
    queryset= country.objects.all()
    serializer_class = countrySerializers

class SupplierViewSet(viewsets.ModelViewSet):
    queryset =supplier.objects.all()
    serializer_class = supplierSerializers

class BuyerViewSet(viewsets.ModelViewSet):
    queryset=buyer.objects.all()
    serializer_class = buyerSerializer

class PortsViewSet(viewsets.ModelViewSet):
    queryset=ports.objects.all()
    serializer_class =portsSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset=item.objects.all()
    serializer_class = itemSerializer

class ItemTypeViewSet(viewsets.ModelViewSet):
    queryset=itemType.objects.all()
    serializer_class = itemTypeSerializers

class orderViewSet(viewsets.ModelViewSet):
    queryset=order.objects.all()
    serializer_class = orderSerializers

class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset=orderDetail.objects.all()
    serializer_class = orderDetailSerializers

class ShipmentViewSet(viewsets.ModelViewSet):
    queryset=shipment.objects.all()
    serializer_class = shipmentSerializers

class ShiplineViewSet(viewsets.ModelViewSet):
    queryset=shippingline.objects.all()
    serializer_class =shipinglineSerializers

class ShipmentDetailViewSet(viewsets.ModelViewSet):
    queryset=shipmentDetail.objects.all()
    serializer_class =shipmentDetailSerializers