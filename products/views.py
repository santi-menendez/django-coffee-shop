from django.urls import reverse_lazy
from django.views import generic
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import ProductForm
from .models import Product
from .serializer import ProductSerializer

# Create your views here.


class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy(
        "add_product"
    )  # Redirige a la misma página después de enviar el formulario

    def form_valid(self, form):
        form.save()  # Guarda el producto en la base de datos
        return super().form_valid(form)


class ProductListView(generic.ListView):
    template_name = "products/list_product.html"
    model = Product
    context_object_name = "products"


class ProductListAPI(APIView):
    authentication_classes = []  # Deshabilita la autenticación para esta vista
    permission_classes = []  # Deshabilita los permisos para esta vista

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
