from django.shortcuts import render

from .models import Event


def event_list(request):
    events = Event.objects.filter(active=True).order_by("date", "time")

    return render(
        request,
        "events/event_list.html",
        {"events": events},
    )
    