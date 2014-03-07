from django.shortcuts import render_to_response
from django.template import RequestContext
from aut.views import add_default_data


def features(request):
    datos = add_default_data(request)
    return render_to_response("pages/features.html", datos, context_instance=RequestContext(request))

def pricing(request):
    datos = add_default_data(request)
    return render_to_response("pages/pricing.html", datos, context_instance=RequestContext(request))

def about(request):
    datos = add_default_data(request)
    return render_to_response("pages/about.html", datos, context_instance=RequestContext(request))