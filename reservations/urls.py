from django.urls import path

from . import views

app_name = "reservations"

urlpatterns = [
    path(
        "event/<int:event_id>/reserve/",
        views.reserve_event,
        name="reserve_event",
    ),
    path(
        "event/<int:event_id>/cancel/",
        views.cancel_reservation,
        name="cancel_reservation",
    ),
]
