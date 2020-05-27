from django.db import models
import uuid

class HumedadAire(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Tipo', max_length=20)
    latitude = models.FloatField(verbose_name='Latitud')
    longitude =  models.FloatField(verbose_name='Longitud')
    terrain =  models.CharField(verbose_name='Tipo de Terreno', max_length=20)
    value = models.IntegerField(verbose_name='Valor')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)