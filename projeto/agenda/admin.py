from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html, format_html_join
from agenda.models import Compromisso, Local, Convidado, Anotacao_Compromisso, UserProfile


# Register your models here.


class CompormissoConvidadosInline(admin.TabularInline):
    model = Compromisso.Convidados.through
    verbose_name_plural = ' Compromissos'


class ConvidadosCompromissosInline(admin.TabularInline):
    model = Compromisso.Convidados.through
    verbose_name_plural = 'Convidados '


class Anotacao_CompromissoInline(admin.TabularInline):
    model = Anotacao_Compromisso
    extra = 1


class ConvidadoAdmin(admin.ModelAdmin):
    inlines = [CompormissoConvidadosInline,]
    extra = 1


class CompromissoAdmin(admin.ModelAdmin):
    exclude = ['Convidados']
    inlines = [ConvidadosCompromissosInline, Anotacao_CompromissoInline]


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


class Anotacao_CompromissoAdmin(admin.ModelAdmin):
    # Campos a serem exibidos na listagem
    list_display = ['get_descricao', 'data', 'compromisso', 'get_usuario']
    list_filter = ['descricao', 'data', 'compromisso', 'user']  #
    # change_list_template = 'change_list.html'
    search_fields = ['descricao', 'data']

    def get_descricao(self, obj):
        return obj.descricao
    get_descricao.admin_order_field = 'descricao'
    get_descricao.short_description = 'Descrição'

    def get_usuario(self, obj):
        return obj.descricao
    get_usuario.admin_order_field = 'user'
    get_usuario.short_description = 'Usuário'

    # list_display = ['__str__', 'botao_excluir']
    # def botao_excluir(self, obj):
    #     delete_url = f'/admin/agenda/anotacao_compromisso/{obj.id}/delete/'
    #     editar_url = f'/admin/agenda/anotacao_compromisso/{obj.id}/chage/'
    #     return format_html('<a href="{}" class="button-delete ">Excluir</a> <a href="{}" class="button">Editar</a>', delete_url, editar_url)
    # botao_excluir.short_description = 'Ações'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'compromisso':
            if not request.user.is_superuser:
                Usuario = Convidado.objects.get(user=request.user)
                kwargs['queryset'] = Compromisso.objects.filter(
                    Convidados=Usuario)

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
