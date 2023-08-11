from django.db import models

# Create your models here.



class country(models.Model):
    cid=models.BigAutoField(primary_key=True)
    cname=models.CharField(max_length=50)

    def __str__(self):
        return self.cname

class supplier(models.Model):
    sid =models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)
    address=models.TextField()
    IECcode=models.CharField(max_length=60)
    country_origin=models.ForeignKey(country , on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class buyer(models.Model):
    bid=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)
    IECcode=models.CharField(max_length=60)
    gstno=models.CharField(max_length=18)
    panno=models.CharField(max_length=18)
    Authsignatory=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
porttype=(
    ("1" , 'dry'),
    ("2" , 'sea'),
)

class ports(models.Model):
    pid=models.BigAutoField(primary_key=True)
    cid=models.ForeignKey(country, on_delete=models.CASCADE)
    portname=models.CharField(max_length=90)
    type=models.CharField(max_length=3,choices=porttype,default=1)

    def __str__(self):
        return self.portname


class item(models.Model):
    igid=models.BigAutoField(primary_key=True)
    igroupname=models.CharField(max_length=50)

    def __str__(self):
        return self.igroupname

class itemType(models.Model):
    iid=models.BigAutoField(primary_key=True)
    item_name=models.ForeignKey(item , on_delete=models.CASCADE)
    HSNcode=models.CharField(max_length=90)

    # def __str__(self):ot
    #     return self.item_name

class order(models.Model):
    oid=models.BigAutoField(primary_key=True)
    salesOrderno=models.CharField(max_length=90)
    ft=models.ForeignKey(supplier , on_delete=models.CASCADE ,related_name='orders_as_ft')
    supplier=models.ForeignKey(supplier  ,on_delete=models.CASCADE ,related_name='orders_as_supplier')
    buyer=models.ForeignKey(buyer , on_delete=models.CASCADE)
    orderdate=models.DateField()
    supplierOrderDate=models.DateField()
    ValidityPeriod=models.IntegerField()
    POR=models.ForeignKey(ports , on_delete=models.CASCADE , related_name='orders_as_por')
    LoadPort=models.ForeignKey(ports , on_delete=models.CASCADE , related_name='orders_as_laod_port')
    POD=models.ForeignKey(ports , on_delete=models.CASCADE , related_name='orders_as_pod')
    FPOD=models.ForeignKey(ports , on_delete=models.CASCADE ,  related_name='orders_as_fpod')

  
    
class orderDetail(models.Model):
    oid=models.BigAutoField(primary_key=True)
    orderid=models.ForeignKey(order , on_delete=models.CASCADE)
    Iid=models.ForeignKey(itemType , on_delete=models.CASCADE)
    Qty=models.DecimalField(max_digits=10, decimal_places=2)
    price=models.DecimalField(max_digits=10, decimal_places=2)

    # def __str__(self):
    #     return self.oid

class shipment(models.Model):
    shipmentid=models.BigAutoField(primary_key=True)
    orderid=models.ForeignKey(order , on_delete=models.CASCADE , related_name='shipment_as_orderid')
    Blno=models.CharField(max_length=90)
    shippingline=models.ForeignKey(order , on_delete=models.CASCADE , related_name='shipment_as_sobdate')
    SOBdate=models.DateTimeField()
    POR=models.ForeignKey(ports , on_delete=models.CASCADE , related_name='shipment_as_por')
    LoadPort=models.ForeignKey(ports , on_delete=models.CASCADE , related_name='shipment_as_load_port')
    Pod=models.ForeignKey(ports , on_delete=models.CASCADE ,  related_name='shipment_as_pod')
    Fpod=models.ForeignKey(ports , on_delete=models.CASCADE ,  related_name='shipment_as_fpod')
    isshipped=models.BooleanField()


    def __str__(self):
        return self.Blno

class shippingline(models.Model):
    slid=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class shipmentDetail(models.Model):
    id=models.BigAutoField(primary_key=True)
    shipmentid=models.ForeignKey(shipment ,   on_delete=models.CASCADE , related_name='shipmentdetail_as_shipmentid')
    item=models.ForeignKey(shipment ,  on_delete=models.CASCADE ,  related_name='shipmentdetail_as_item')
    qty=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.shipmentid


    