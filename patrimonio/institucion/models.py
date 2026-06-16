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
        costo_total = 0
        for guia in self.guias.all():
            for exhibicion in guia.exhibiciones.all():
                if exhibicion.costo_produccion:
                    costo_total += exhibicion.costo_produccion
        return costo_total
    calcular_costo_total_produccion.short_description = "Costo total de producción"

    def guia_mas_experiencia(self):
        guias = self.guias.all()
        if not guias.exists():
            return "No registrado"
        max_exp = -1
        for guia in guias:
            if guia.anios_experiencia_guia is not None and guia.anios_experiencia_guia > max_exp:
                max_exp = guia.anios_experiencia_guia
                
        if max_exp == -1:
            return "No registrado"
        nombres_guias = []
        for guia in guias:
            if guia.anios_experiencia_guia == max_exp:
                nombres_guias.append(guia.nombre_completo)
                
        return ", ".join(nombres_guias)
        
    guia_mas_experiencia.short_description = "Guía(s) con más experiencia"

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
    def __str__(self):
        return self.titulo_exhibicion
