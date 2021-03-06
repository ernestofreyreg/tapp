from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from aut.views import add_default_data


@login_required(login_url='/')
def view(request):
    datos = add_default_data(request)
    datos['section'] = 'definitions'
    return render_to_response("definitions/definitions.html", datos, context_instance=RequestContext(request))