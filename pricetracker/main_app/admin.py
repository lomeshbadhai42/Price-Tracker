from django.contrib import admin
from .models import Item
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ('product_name','username')  # Specify the columns you want to display

    def username(self, obj):
        return obj.user.username

    username.short_description = 'Username'  # Set a custom header for the column



admin.site.register(Item, ItemAdmin)




class ItemInline(admin.TabularInline):
    model = Item
    extra = 1
    fields = ('product_name', 'product_price', 'max_price', 'status') 

class CustomUserAdmin(UserAdmin):
    inlines = [ItemInline]
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
       
    )
   


# Unregister default User admin and register with custom UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
