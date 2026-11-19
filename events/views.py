from django.shortcuts import get_object_or_404, render

from .models import Event


def event_list(request):
    events = Event.objects.filter(active=True).order_by("date", "time")

    return render(
        request,
        "events/event_list.html",
        {"events": events},
    )


def event_detail(request, event_id):
    event = get_object_or_404(
        Event,
        id=event_id,
        active=True,
    )

    active_reservations = event.reservations.filter(active=True).count()

    available_places = event.capacity - active_reservations

    user_has_reservation = False

    if request.user.is_authenticated:
        user_has_reservation = event.reservations.filter(
            user=request.user,
            active=True,
        ).exists()

    return render(
        request,
        "events/event_detail.html",
        {
            "event": event,
            "available_places": available_places,
            "user_has_reservation": user_has_reservation,
        },
    )
