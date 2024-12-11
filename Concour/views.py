from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *


# Create your views here.

def physique(request):
    query = None
    form_data = {
        'concr': request.POST.get('concr', ''),
        'filie': request.POST.get('filie', ''),
        'epreuve': request.POST.get('epreuve', ''),
        'year1': request.POST.get('year1', ''),
        'year2': request.POST.get('year2', ''),
        'fruits': request.POST.getlist('fruits', []),
    }
    if request.method == 'POST':
        concours = request.POST.get('concr', None)
        file = request.POST.get('filie', None)
        epreuuve = request.POST.get('epreuve', None)
        anee1 = request.POST.get('year1', None)
        anee2 = request.POST.get('year2', None)
        modules = request.POST.getlist('fruits', None)
        query = concourphy.objects.all()
        if concours:
            query = query.filter(nom=concours)
        if file:
            query = query.filter(filier=file)
        if epreuuve:
            query = query.filter(numepreuve=epreuuve)
        if anee1 and anee2:
            query = query.filter(annee__gte=anee1, annee__lte=anee2)
        elif anee1:
            query = query.filter(annee__gte=anee1)
        elif anee2:
            query = query.filter(annee__lte=anee2)
        if modules:  # Si des modules sont sélectionnés

            query = query.filter(
                mecanique='mecanique' in modules,
                electromagnetisme='electromagnetisme' in modules,
                thermodynamique='thermodynamique' in modules,
                optique='optique' in modules,
                quantique='quantique' in modules,
                electronique='electronique' in modules
            )

    return render(request, 'cncphy.html', {'query': query, 'form_data': form_data})


def math(request):
    query = None
    form_data = {
        'concr': request.POST.get('concr', ''),
        'filie': request.POST.get('filie', ''),
        'epreuve': request.POST.get('epreuve', ''),
        'year1': request.POST.get('year1', ''),
        'year2': request.POST.get('year2', ''),
        'fruits': request.POST.getlist('fruits', []),
    }
    if request.method == 'POST':
        concours = request.POST.get('concr', None)
        file = request.POST.get('filie', None)
        epreuuve = request.POST.get('epreuve', None)
        anee1 = request.POST.get('year1', None)
        anee2 = request.POST.get('year2', None)
        modules = request.POST.getlist('fruits', None)
        query = concourmath.objects.all()
        if concours:
            query = query.filter(nom=concours)
        if file:
            query = query.filter(filier=file)
        if epreuuve:
            query = query.filter(numepreuve=epreuuve)
        if anee1 and anee2:
            query = query.filter(annee__gte=anee1, annee__lte=anee2)
        elif anee1:
            query = query.filter(annee__gte=anee1)
        elif anee2:
            query = query.filter(annee__lte=anee2)
        if modules:  # Si des modules sont sélectionnés

            query = query.filter(
                algebre='algebre' in modules,
                analyse='analyse' in modules,
                proba='proba' in modules,
                optique='geom' in modules
            )

    return render(request, "cncmath.html", {'query': query, 'form_data': form_data})


def chimie(request):
    query = None
    form_data = {
        'concr': request.POST.get('concr', ''),
        'filie': request.POST.get('filie', ''),
        'year1': request.POST.get('year1', ''),
        'year2': request.POST.get('year2', ''),
        'fruits': request.POST.getlist('fruits', []),
    }
    if request.method == 'POST':
        concours = request.POST.get('concr', None)
        file = request.POST.get('filie', None)
        anee1 = request.POST.get('year1', None)
        anee2 = request.POST.get('year2', None)
        modules = request.POST.getlist('fruits', None)
        query = concourchimie.objects.all()
        if concours:
            query = query.filter(nom=concours)
        if file:
            query = query.filter(filier=file)
        if anee1 and anee2:
            query = query.filter(annee__gte=anee1, annee__lte=anee2)
        elif anee1:
            query = query.filter(annee__gte=anee1)
        elif anee2:
            query = query.filter(annee__lte=anee2)
        if modules:  # Si des modules sont sélectionnés

            query = query.filter(
                generale='generale' in modules,
                thermochimie='thermo' in modules,
                electrochimie='electro' in modules,
                cinetique='cinetique' in modules,
                diag_bin='bin' in modules,
                solution='solution' in modules,
                organique='organique' in modules
            )

    return render(request, 'cncchim.html', {'query': query, 'form_data': form_data})

def details(request, concours_id):
    concours = get_object_or_404(concourphy, id=concours_id)
    return render(request, 'Detailconcour.html', {'concours': concours})
