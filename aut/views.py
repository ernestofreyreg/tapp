# Create your views here.
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import twython
from aut.models import TwitterProfileCredentials
from tapp.settings import TWITTER_KEY, TWITTER_SECRET


def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/dashboard")
    data = {"request": request}
    return render_to_response("base.html", data, context_instance=RequestContext(request))


def logged(request):
    """User is logged already, so, grab their twitter profile info"""
    tuser = request.user.twitterprofile
    tw = twython.Twython(TWITTER_KEY,TWITTER_SECRET,tuser.oauth_token,tuser.oauth_secret)
    profile = tw.verify_credentials()
    if TwitterProfileCredentials.objects.filter(twitterprofile=tuser).exists():
        credentials = TwitterProfileCredentials.objects.get(twitterprofile=tuser)
    else:
        credentials = TwitterProfileCredentials(twitterprofile=tuser)
    credentials.data = json.dumps(profile)
    credentials.save()

    return render_to_response("login_success.html")


def add_default_data(request):
    data = {'request': request}
    if request.user.is_authenticated():
        tp = request.user.twitterprofile
        tpc = tp.twitterprofilecredentials
        tw = tpc.twython()
        data.update({"twitterprofile": tp, "twitterprofilecredentials": tpc, "twitter": tw})

    return data

@login_required(login_url='/')
def dashboard(request):
    datos = add_default_data(request)
    datos['section'] = 'dashboard'
    return render_to_response("dashboard.html", datos, context_instance=RequestContext(request))
