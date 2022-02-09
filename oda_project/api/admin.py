from django.contrib import admin
from . import models
from django.utils.html import mark_safe

# Register your models here.


@admin.register(models.Academician)
class AcademicianAdmin(admin.ModelAdmin):
    list_display = [
        "image_view",
        "last_name",
        "first_name",
        "registration_number",
        "date_add",
        "date_update",
        "status",
    ]
    list_display_links = ['last_name']

    def image_view(self, obj):

        return mark_safe(
            f'<img src="{obj.photo.url}" style="width:100px; height:100px" >'
        )


@admin.register(models.Caisse)
class CaisseAdmin(admin.ModelAdmin):
    list_display = ["reason", "amount", "payment_date", "status", "date_add"]
