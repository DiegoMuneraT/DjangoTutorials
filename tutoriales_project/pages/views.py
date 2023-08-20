from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django import forms

# Create your views here.
class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'About us - Online Store',
            'subtitle': 'This is the about page of our online store',
            'description': 'This is the about page of our online store',
            'author': 'Developed by: Diego Munera',
        })

        return context
    
class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV", "price": 110},
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price": 50},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price": 45},
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price": 23},
    ]

class ProductIndexView(View):        
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] =  "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'


    def get(self, request, id):
        viewData = {}
        
        if int(id) > len(Product.products):
            return render(request, 'pages/home.html')
        
        product = Product.products[int(id)-1]
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] =  product["name"] + " - Product information"
        viewData["product"] = product

        return render(request, self.template_name, viewData)
    
class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] =  form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid:
            return redirect(form)
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] =  form
            return render(request, self.template_name, viewData)

