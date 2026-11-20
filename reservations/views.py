from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from events.models import Event

from .models import Reservation


@login_required
@require_POST
def reserve_event(request, event_id):
    event = get_object_or_404(
        Event,
        id=event_id,
        active=True,
    )

    reservation = Reservation.objects.filter(
        user=request.user,
        event=event,
    ).first()

    if reservation and reservation.active:
        messages.info(
            request,
            "Ya tienes una reserva activa para este evento.",
        )
        return redirect("event_detail", event_id=event.id)

    active_reservations = event.reservations.filter(active=True).count()

    if active_reservations >= event.capacity:
        messages.error(
            request,
            "No quedan plazas disponibles para este evento.",
        )
        return redirect("event_detail", event_id=event.id)

    if reservation:
        reservation.active = True
        reservation.save()
    else:
        Reservation.objects.create(
            user=request.user,
            event=event,
        )

    messages.success(
        request,
        "La reserva se ha realizado correctamente.",
    )

    return redirect("event_detail", event_id=event.id)

@login_required(login_url="/admin/login/")
@require_POST
def cancel_reservation(request, event_id):
    event = get_object_or_404(
        Event,
        id=event_id,
        active=True,
    )

    reservation = Reservation.objects.filter(
        user=request.user,
        event=event,
        active=True,
    ).first()

    if reservation:
        reservation.active = False
        reservation.save()

        messages.success(
            request,
            "La reserva se ha cancelado correctamente.",
        )
    else:
        messages.info(
            request,
            "No tienes una reserva activa para este evento.",
        )

    return redirect("event_detail", event_id=event.id)

@login_required(login_url="/admin/login/")
def reservation_list(request):
    reservations = Reservation.objects.filter(
        user=request.user,
        active=True,
    ).select_related("event").order_by("event__date", "event__time")

    return render(
        request,
        "reservations/reservation_list.html",
        {"reservations": reservations},
    )
