from compo.models import Trader, Company, TraderForm
from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponse

def join_compo_view(request):
    if request.method == 'POST':
        pass
    else:
        form = TraderForm()
        t = get_template('compo.html')
