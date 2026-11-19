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

    return render(
        request,
        "events/event_detail.html",
        {"event": event},
    )
