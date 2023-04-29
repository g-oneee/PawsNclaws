from django.contrib import admin

# Register your models here.
from .models import product_Category,ServiceResponses,Services,product_Sub_Category,Product,pet_Category,breed_Category,Adopt,Order,Responses,contact_us


admin.site.register(product_Category)
admin.site.register(product_Sub_Category)
admin.site.register(pet_Category)
admin.site.register(breed_Category)
admin.site.register(Adopt)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Responses)
admin.site.register(contact_us)
admin.site.register(ServiceResponses)
admin.site.register(Services)