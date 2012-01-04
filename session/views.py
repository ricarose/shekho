from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import UserCreationForm

from shekho.session.models import SESSION_STATUS, Session
from shekho.session.forms import SessionForm

def index(request):
    t = loader.get_template('session/index.html')

    c = RequestContext(request, {
    })

    return HttpResponse(t.render(c))

def browse(request):
    sessions = Session.objects.all()
    return render_to_response('session/browse.html', \
        {'sessions' : sessions}, \
        context_instance=RequestContext(request))

def details(request, session_id):
    session =  get_object_or_404(Session, pk=session_id)
    t = loader.get_template('session/details.html')
    c = RequestContext(request, {
        'session' : session,
    })

    return HttpResponse(t.render(c))

@login_required
def submit(request):
    t = loader.get_template('session/submit.html')

    submission_success = False

    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            submission_success = True
    else:
        form = SessionForm()

    c = RequestContext(request, {
        'form': form, 'success' : submission_success})

    c.update(csrf(request))
    return HttpResponse(t.render(c))

def register(request):
    t = loader.get_template('registration/register.html')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/accounts/login")

    form = UserCreationForm()

    c = RequestContext(request, {'form': form})

    c.update(csrf(request))

    return HttpResponse(t.render(c))
