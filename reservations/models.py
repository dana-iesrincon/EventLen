from django.conf import settings
from django.db import models

from events.models import Event


class Reservation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reservations",
        verbose_name="Usuario",
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="reservations",
        verbose_name="Evento",
    )

    created_at = models.DateTimeField(
        "Fecha de reserva",
        auto_now_add=True,
    )

    active = models.BooleanField(
        "Activa",
        default=True,
    )

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "event"],
                name="unique_user_event_reservation",
            ),
        ]

    def __str__(self):
        return f"{self.user} - {self.event}"
