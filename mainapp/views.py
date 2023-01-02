from django.shortcuts import redirect, render
from django.views import View
from.models import *


# Create your views here.

class Home2View(View):
    def get(self, request):
        data = {
            'sections': MainSection.objects.order_by('name')
        }
        return render(request, 'page-index-2.html', data)

class HomeView(View):
    def get(self, request):
        context = {
            'mainsections': MainSection.objects.all()[:6],
            'rest': MainSection.objects.all()[6:]
        }
        return render(request, 'page-index.html', context)

class SectionsView(View):
    def get(self, request, s):
        s = s.capitalize()
        context = {
            'sections': Section.objects.filter(mainsection__name=s),
        }
        return render(request, 'page-category.html', context)

class InnersView(View):
    def get(self, request, d):
        d = d.capitalize()
        context = {
            'inners': Inner.objects.filter(section__name=d),
        }
        return render(request, 'ichki.html', context)

class ProductsView(View):
    def get(self, request, j):
        data = {
            'products': Product.objects.filter(inner__name=j)
        }
        return render(request, 'page-listing-grid.html', data)

class ProductDetailsView(View):
    def get(self, request, pk):
        data = {
            'product': Product.objects.get(id=pk)
        }
        return render(request, 'page-detail-product.html', data)

