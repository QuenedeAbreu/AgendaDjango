from django.contrib import admin
from django.contrib.auth.models import User
from agenda.models import Compromisso, Local, Convidado, Anotacao_Compromisso


# Register your models here.


class ConvidadosInline(admin.TabularInline):
    model = Compromisso.Convidados.through


class ConvidadoAdmin(admin.ModelAdmin):
    inlines = [ConvidadosInline,]


class CompromissoAdmin(admin.ModelAdmin):
    exclude = ['Convidados']
    inlines = [ConvidadosInline]


class Anotacao_CompromissoAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(user=request.user)
        return queryset

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'compromisso':
            if not request.user.is_superuser:
                Usuario = Convidado.objects.filter(user=request.user)
                kwargs['queryset'] = Compromisso.objects.filter(
                    Convidados=Usuario[0])

        if db_field.name == 'user':
            if not request.user.is_superuser:
                kwargs['queryset'] = User.objects.filter(id=request.user.id)
                kwargs['initial'] = request.user.id
                kwargs['disabled'] = 'disabled'

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Compromisso, CompromissoAdmin)
admin.site.register(Local)
admin.site.register(Convidado, ConvidadoAdmin)
admin.site.register(Anotacao_Compromisso, Anotacao_CompromissoAdmin)
