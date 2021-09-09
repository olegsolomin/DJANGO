from django.contrib import admin

from cats.models import Cat, Breed

# models

admin.site.register(Cat)
admin.site.register(Breed)