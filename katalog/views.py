from django.shortcuts import render
from .models import *
from django.views.generic import DetailView

# Create your views here.


def index(request):
    nav_kategorie = Kategorie.objects.all()
    nav_kolekce = Kolekce.objects.all()
    nejnovejsi = Kolekce.objects.order_by('-datum_vydani')[:1]
    nejnovejsi_kolekce = Produkt.objects.filter(kolekce=nejnovejsi)
    context = {
        'nadpis': 'Katalog nábytku',
        'nav_kategorie': nav_kategorie,
        'nav_kolekce': nav_kolekce,
        'nejnovejsi_kolekce': nejnovejsi_kolekce,
    }

    return render(request, template_name='index.html', context=context)


def produkty(request):
    nav_kategorie = Kategorie.objects.all()
    nav_kolekce = Kolekce.objects.all()
    produkty = Produkt.objects.all()
    context = {
        'nav_kategorie': nav_kategorie,
        'nav_kolekce': nav_kolekce,
        'produkty': produkty
    }

    return render(request, template_name='produkty.html', context=context)


def kategorie(request):
    nav_kategorie = Kategorie.objects.all()
    nav_kolekce = Kolekce.objects.all()
    produkty = Produkt.objects.all()
    context = {
        'nav_kategorie': nav_kategorie,
        'nav_kolekce': nav_kolekce,
        'produkty': produkty
    }

    return render(request, template_name='kategorie.html', context=context)


def kolekce(request):
    nav_kategorie = Kategorie.objects.all()
    nav_kolekce = Kolekce.objects.all()
    produkty = Produkt.objects.all()
    context = {
        'nav_kategorie': nav_kategorie,
        'nav_kolekce': nav_kolekce,
        'produkty': produkty
    }

    return render(request, template_name='kolekce.html', context=context)


def kategorieDetail(request, pk):
    nav_kategorie = Kategorie.objects.all()
    nav_kolekce = Kolekce.objects.all()
    produkty = Produkt.objects.filter(kategorie=pk)
    nadpis = Kategorie.objects.filter(pk=pk)[0]
    context = {
        'nadpis': nadpis,
        'nav_kategorie': nav_kategorie,
        'nav_kolekce': nav_kolekce,
        'produkty': produkty
    }

    return render(request, template_name='kategorie-detail.html', context=context)


def kolekceDetail(request, pk):
    nav_kategorie = Kategorie.objects.all()
    nav_kolekce = Kolekce.objects.all()
    produkty = Produkt.objects.filter(kolekce=pk)
    nadpis = Kolekce.objects.filter(pk=pk)[0]
    context = {
        'nadpis': nadpis,
        'nav_kategorie': nav_kategorie,
        'nav_kolekce': nav_kolekce,
        'produkty': produkty
    }

    return render(request, template_name='kolekce-detail.html', context=context)


class ProduktDetail(DetailView):
    model = Produkt

    context_object_name = 'produkt'
    template_name = 'produkt-detail.html'
