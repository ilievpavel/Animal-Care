from django.contrib import admin

from animal.models import Animal


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_cured')
    list_filter = ('priority', 'is_cured')


admin.site.register(Animal, AnimalAdmin)
