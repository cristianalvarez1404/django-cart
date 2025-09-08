from django.contrib import admin
from .models import Store

class StoreAdmin(admin.ModelAdmin):
  list_display = ('product_name','slug','price','stock','category','created_date','modified_date','is_available')
  prepopulated_fields = {'slug':('product_name',)}

admin.site.register(Store,StoreAdmin)