from django.contrib import admin

# Register your models here.

from .models import  District, Circle, Panchayat, SubDiv, User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_staff", "is_superuser")

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):

    list_display = ("dist_name_hn",)

@admin.register(SubDiv)
class SubDivAdmin(admin.ModelAdmin):

    list_display = ("subdiv_id", "subdiv_name_hn")

@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):

    list_display = ("circle_name_hn",)

@admin.register(Panchayat)
class PanchayatAdmin(admin.ModelAdmin):

    list_display = ("id","panchayat_name_hn","circle")