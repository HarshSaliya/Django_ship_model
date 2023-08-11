from rest_framework import serializers
from web .models import *


class countrySerializers(serializers.ModelSerializer):
    class Meta:
        model = country
        fields= "__all__"

class  supplierSerializers(serializers.ModelSerializer):
    class Meta:
        model = supplier
        fields = "__all__"

class buyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = buyer
        fields = '__all__'

class portsSerializer(serializers.ModelSerializer):
    class Meta:
        model =ports
        fields = '__all__'

class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = '__all__'


class itemTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = itemType
        fields = '__all__'

class orderSerializers(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'

class orderDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = orderDetail
        fields = '__all__'

class shipmentSerializers(serializers.ModelSerializer):
    class Meta:
        model =shipment
        fields = "__all__"

class shipinglineSerializers(serializers.ModelSerializer):
    class Meta:
        model = shippingline
        fields="__all__"

class shipmentDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = shipmentDetail
        fields ="__all__"