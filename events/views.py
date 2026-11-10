from django.http import HttpResponse


def event_list(request):
    return HttpResponse("Listado de eventos de EventLen")