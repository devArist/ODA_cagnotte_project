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
        "matricule",
        "date_add",
        "date_update",
        "status",
    ]

    def image_view(self, obj):

        return mark_safe(
            f'<img src="{obj.photo.url}" style="width:100px; height:100px" >'
        )


@admin.register(models.Caisse)
class CaisseAdmin(admin.ModelAdmin):
    list_display = ["motif", "montant", "date_paiement", "status", "date_add"]
