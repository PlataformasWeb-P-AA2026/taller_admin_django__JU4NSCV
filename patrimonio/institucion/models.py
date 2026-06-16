from django.db import models

class Museo(models.Model):
    nombre = models.CharField(
        max_length=150,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Nombre"
    )
    ciudad = models.CharField(
        max_length=100,
        verbose_name="Ciudad"
    )
    anio_fundacion = models.IntegerField(
        verbose_name="Año de fundación"
    )

    def calcular_costo_total_produccion(self):
        resultado = Exhibicion.objects.filter(guia_museo__museo=self).aggregate(
            total=Sum('costo_produccion')
        )
        return resultado['total'] or 0

    def guia_mas_experiencia(self):
        guias = self.guias.all()
        if not guias.exists():
            return "No registrado"
        guias_mas_experiencia = guias.first()
        for guia in guias:
            if guia.anios_experiencia_guia >= guias_mas_experiencia.anios_experiencia_guia:
                guias_mas_experiencia = guia
        return guias_mas_experiencia.nombre_completo

    def __str__(self):
        return self.nombre

class GuiaMuseo(models.Model):
    nombre_completo = models.CharField(
        max_length=150,
        verbose_name="Nombre completo"
    )
    anios_experiencia_guia = models.IntegerField(
        verbose_name="Años de experiencia"
    )
    idiomas_hablados = models.CharField(
        max_length=200,
        verbose_name="Idiomas hablados"
    )
    museo = models.ForeignKey(
        Museo,
        on_delete=models.CASCADE,
        related_name="guias",
        verbose_name="Museo"
    )
    class Meta:
        verbose_name = "Guía de Museo"
        verbose_name_plural = "Guías de Museo"

    def __str__(self):
        return self.nombre_completo
    
class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField(
        max_length=150,
        verbose_name="Título de la exhibición"
    )
    duracion_meses = models.IntegerField(
        verbose_name="Duración (meses)"
    )
    costo_produccion = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Costo de producción"
    )
    tematica = models.CharField(
        max_length=150,
        verbose_name="Temática"
    )
    guia_museo = models.ForeignKey(
        GuiaMuseo,
        on_delete=models.CASCADE,
        related_name="exhibiciones",
        verbose_name="Guía de museo"
    )

    class Meta:
        verbose_name = "Exhibición"
        verbose_name_plural = "Exhibiciones"

    def __str__(self):
        return self.titulo_exhibicion
