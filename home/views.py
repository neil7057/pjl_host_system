from django.shortcuts import render
from host.models import Host
from members.models import Members
from category.models import Category
from timeperiod.models import Timeperiod
from pupil.models import Pupil
from organisation.models import Organisation
from teamlead.models import Teamlead
from django.db.models import Q

# Create your views here.


def index(request):
    """ view to return index page """

    return render(request, 'home/index.html')


def search(request):
    """ view to return search results page """
    hosts = ""
    categories = ""
    members = ""
    pupils = ""
    timeperiods = ""
    organisations = ""
    teamleaders = ""
    if 'q' in request.GET:
        q = request.GET['q']
        # hosts = Host.objects.filter(hostname__icontains=q)
        multiple_q = Q(Q(hostname__icontains=q) | Q(county__icontains=q) |
                       Q(categories__friendly_name__icontains=q))
        hosts = Host.objects.filter(multiple_q)

        multiple_q = Q(Q(orgname__icontains=q) | Q(county__icontains=q))
        organisations = Organisation.objects.filter(multiple_q)

        multiple_q = Q(Q(name__icontains=q) | Q(friendly_name__icontains=q))
        categories = Category.objects.filter(multiple_q)

        multiple_q = Q(Q(first_name__icontains=q) |
                       Q(preferred_name__icontains=q) |
                       Q(last_name__icontains=q) |
                       Q(team__first_name__icontains=q))
        pupils = Pupil.objects.filter(multiple_q)

        multiple_q = Q(Q(first_name__icontains=q) |
                       Q(last_name__icontains=q) |
                       Q(host__hostname__icontains=q))
        members = Members.objects.filter(multiple_q)

        multiple_q = Q(Q(first_name__icontains=q) |
                       Q(last_name__icontains=q) |
                       Q(org__orgname__icontains=q))
        teamleaders = Teamlead.objects.filter(multiple_q)

        multiple_q = Q(Q(title__icontains=q) |
                       Q(date_from__icontains=q) |
                       Q(date_to__icontains=q))
        timeperiods = Timeperiod.objects.filter(multiple_q)

    context = {
        'hosts': hosts,
        'categories': categories,
        'members': members,
        'pupils': pupils,
        'timeperiods': timeperiods,
        'organisations': organisations,
        'teamleaders': teamleaders,
        'search_term': q
    }

    return render(request, 'home/search_results.html', context)
