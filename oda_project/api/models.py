from django.db import models

# Create your models here.


class Base(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Academician(Base):
    last_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=255)
    matricule = models.CharField(max_length=250)
    photo = models.FileField(upload_to="image_academician")

    class Meta:
        verbose_name = "Academicien"
        verbose_name_plural = "Academiciens"

    def __str__(self):
        return self.last_name


class Caisse(Base):
    academician = models.ForeignKey(
        Academician,
        verbose_name="academicien_id",
        related_name="caisse_academicien",
        on_delete=models.CASCADE,
    )
    motif = models.CharField(max_length=50)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Caisse"

    def __unicode__(self):
        return self.academician
