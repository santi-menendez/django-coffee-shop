from django import forms

from .models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="Nombre")
    description = forms.CharField(max_length=300, label="Descripción")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    available = forms.BooleanField(initial=True, required=False, label="Disponible")
    photo = forms.ImageField(required=False, label="Foto del producto")

    def save(self):
        # Aquí puedes implementar la lógica para guardar el producto en la base de datos
        # Por ejemplo, podrías crear una instancia del modelo Product y guardarla
        Product.objects.create(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            available=self.cleaned_data["available"],
            photo=self.cleaned_data.get("photo"),
        )
