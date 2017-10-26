from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    organizations = Organization.objects.all()
    return render(request, 'index.html', {'organizations': organizations})


def detail(request, organization_id):
    organization = get_object_or_404(Organization, pk=organization_id)
    return render(request, 'rso.html', {'organization': organization})

