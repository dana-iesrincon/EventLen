from django.db import models


class Event(models.Model):
    CATEGORY_CHOICES = [
        ("sport", "Deporte"),
        ("leisure", "Ocio"),
        ("culture", "Cultura"),
        ("music", "Música"),
        ("family", "Familiar"),
        ("other", "Otros"),
    ]

    title = models.CharField("Título", max_length=150)
    description = models.TextField("Descripción")

    category = models.CharField(
        "Categoría",
        max_length=20,
        choices=CATEGORY_CHOICES,
    )

    date = models.DateField("Fecha")
    time = models.TimeField("Hora")
    location = models.CharField("Ubicación", max_length=200)
    capacity = models.PositiveIntegerField("Capacidad")

    minimum_age = models.PositiveIntegerField(
        "Edad mínima",
        null=True,
        blank=True,
    )

    image = models.ImageField(
        "Imagen",
        upload_to="events/",
        null=True,
        blank=True,
    )

    active = models.BooleanField("Activo", default=True)
    created_at = models.DateTimeField(
        "Fecha de creación",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.title
    