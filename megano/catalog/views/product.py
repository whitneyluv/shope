from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import DetailView
from catalog.models import Product

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'

    def get(self, request, product_id, *args, **kwargs):
        try:
            product = Product.objects.get(id=product_id)
            context = {'product': product}
            return render(request, self.template_name, context)
        except Product.DoesNotExist:
            return HttpResponse("Product not found", status=404)
