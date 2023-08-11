from django.contrib import admin
from .models import *
# Register your models here.

# class orderAdmin(admin.ModelAdmin):
#     def formfield_for_foreignkey2(self, db_field, request, **kwargs):
#         if db_field.name == 'POR':
#             filtered_queryset = ports.objects.filter(type='dry')
#             print(filtered_queryset)  # Debugging print statement
#             kwargs['queryset'] = filtered_queryset
#             # Repeat the above for other fields
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)


#     def formfield_for_foreignkey1(self, db_field, request, **kwargs):
#         formfield = super().formfield_for_foreignkey(db_field, request, **kwargs)
#         if db_field.name == 'POR':
#             if not formfield.queryset.exists():
#                 filtered_queryset = ports.objects.filter(type='dry')
#                 print(filtered_queryset)  # Debugging print statement
#                 formfield.queryset = filtered_queryset
#         return formfield
    
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         formfield = super().formfield_for_foreignkey(db_field, request, **kwargs)
#         print(" This  ========")
#         if db_field.name == 'POR':
#             print("this IS ++++++++++++")
#             if not formfield.queryset.exists():
#                 print(" this b ***********")
#                 filtered_queryset = ports.objects.filter(type='dry')
#                 formfield.queryset = filtered_queryset
#         # Repeat the above for other fields if needed
#         return formfield
    
admin.site.register(country)
admin.site.register(supplier)
admin.site.register(buyer)
admin.site.register(ports)
admin.site.register(item)
admin.site.register(itemType)
admin.site.register(order)
admin.site.register(orderDetail)
admin.site.register(shipment)
admin.site.register(shippingline)
admin.site.register(shipmentDetail)

