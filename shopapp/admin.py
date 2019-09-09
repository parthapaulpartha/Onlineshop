from django.contrib import admin
from .models import (
    profile, slider_images,
    man_images, woman_images,
    kids_boy_image, kids_girl_image,
    electronics_phone, electronics_desktop,
    electronics_laptop, electronics_head_phone,
    watch_man, watch_woman, watch_kids, gift,
    order, contact
)

# Register your models here.
#---- admin header --------
admin.site.site_header = 'Online Shop'

#-------- profile of admin -------
class ProfileAdmin(admin.ModelAdmin):
    list_display = 'user', 'image',
    list_filter = 'user', 'image',

admin.site.register(profile, ProfileAdmin),

#------ slide image -------
class SliderimageAdmin(admin.ModelAdmin):
    list_display = 'title', 'image'
    list_filter = 'title', 'image'

admin.site.register(slider_images, SliderimageAdmin),

#------ man image -------
class ManAdmin(admin.ModelAdmin):
    list_display = 'title', 'image', 'price'
    list_filter = 'title', 'image', 'price'
    search_fields = ['title', 'price']

admin.site.register(man_images, ManAdmin)

#------ woman image -------
class WomanAdmin(admin.ModelAdmin):
    list_display = 'title', 'image', 'price'
    list_filter = 'title', 'image', 'price'
    search_fields = ['title', 'price']

admin.site.register(woman_images, WomanAdmin)

#------ Kids_boy image -------
class KidsBoyAdmin(admin.ModelAdmin):
    list_display = 'title', 'image', 'price'
    list_filter = 'title', 'image', 'price'
    search_fields = ['title', 'price']

admin.site.register(kids_boy_image, KidsBoyAdmin)

#------ Kids_girl image -------
class KidsGirlAdmin(admin.ModelAdmin):
    list_display = 'title', 'image', 'price'
    list_filter = 'title', 'image', 'price'
    search_fields = ['title', 'price']

admin.site.register(kids_girl_image, KidsGirlAdmin)

#------ Electronic phone -------
class EPhoneAdmin(admin.ModelAdmin):
    list_display = 'title', 'image', 'price'
    list_filter = 'title', 'image', 'price'
    search_fields = ['title', 'price']

admin.site.register(electronics_phone, EPhoneAdmin)

#------ Electronic Desktop -------
class EDesktopAdmin(admin.ModelAdmin):
    list_display = 'title', 'image', 'price'
    list_filter = 'title', 'image', 'price'
    search_fields = ['title', 'price']

admin.site.register(electronics_desktop, EDesktopAdmin)

#------ Electronic Laptop -------
class ELaptopAdmin(admin.ModelAdmin):
    list_display = 'title', 'image', 'price'
    list_filter = 'title', 'image', 'price'
    search_fields = ['title', 'price']

admin.site.register(electronics_laptop, ELaptopAdmin)

#------ Electronic head phone -------
class EHeadPhoneAdmin(admin.ModelAdmin):
    list_display = 'title', 'image', 'price'
    list_filter = 'title', 'image', 'price'
    search_fields = ['title', 'price']

admin.site.register(electronics_head_phone, EHeadPhoneAdmin)

#------ Watch man -------
class WatchManAdmin(admin.ModelAdmin):
    list_display = 'title', 'image', 'price'
    list_filter = 'title', 'image', 'price'
    search_fields = ['title', 'price']

admin.site.register(watch_man, WatchManAdmin)

#------ Watch woman -------
class WatchWomanAdmin(admin.ModelAdmin):
    list_display = 'title', 'image', 'price'
    list_filter = 'title', 'image', 'price'
    search_fields = ['title', 'price']

admin.site.register(watch_woman, WatchWomanAdmin)

#------ Watch kids -------
class WatchKidsAdmin(admin.ModelAdmin):
    list_display = 'title', 'image', 'price'
    list_filter = 'title', 'image', 'price'
    search_fields = ['title', 'price']

admin.site.register(watch_kids, WatchKidsAdmin)

#------ Gift -------
class GiftAdmin(admin.ModelAdmin):
    list_display = 'title', 'image', 'price'
    list_filter = 'title', 'image', 'price'
    search_fields = ['title', 'price']

admin.site.register(gift, GiftAdmin)

#------ order --------
class OrderProductAdmin(admin.ModelAdmin):
    list_display = 'name', 'phone_number', 'product_code', 'quantity', 'order_place', 'order_date', 'delivery_date'
    list_filter = 'name', 'phone_number', 'product_code', 'quantity', 'order_place', 'order_date', 'delivery_date'
    search_fields = ['product_code', 'order_place', 'order_date']

admin.site.register(order, OrderProductAdmin)

#------ Contact -------
class ContactAdmin(admin.ModelAdmin):
    list_display = 'name', 'email', 'message'
    list_filter = 'name', 'email', 'message'

admin.site.register(contact, ContactAdmin)


