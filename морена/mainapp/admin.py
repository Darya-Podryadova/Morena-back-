from django.contrib import admin
from .models import *
from django.forms import ModelChoiceField


class StuffAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='stuff'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Category)
admin.site.register(Stuff, StuffAdmin)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(CartProduct)

