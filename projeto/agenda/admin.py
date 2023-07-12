from django.contrib import admin
from django.contrib.auth.models import User,Permission
from django.contrib.auth.admin import UserAdmin
# from django.utils.html import format_html, format_html_join
from agenda.models import Compromisso, Local, Convidado, Anotacao_Compromisso, User_profile


# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = User_profile
    can_delete = False
    verbose_name_plural = 'Perfil'


class CompormissoConvidadosInline(admin.TabularInline):
    model = Compromisso.Convidados.through
    verbose_name_plural = ' Compromissos'


class ConvidadosCompromissosInline(admin.TabularInline):
    model = Compromisso.Convidados.through
    verbose_name_plural = 'Convidados '


class Anotacao_CompromissoInline(admin.TabularInline):
    model = Anotacao_Compromisso
    extra = 1
    verbose_name_plural = 'Anotacao Compromisso'


class ConvidadoAdmin(admin.ModelAdmin):
    inlines = [CompormissoConvidadosInline,]
    extra = 1


class CompromissoAdmin(admin.ModelAdmin):
    exclude = ['Convidados']
    inlines = [ConvidadosCompromissosInline, Anotacao_CompromissoInline]


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

def traduzir_permissoes(modeladmin, request, queryset):
    
  words = ["Can", "add", "change", "delete", "view","group","entry","permission","user","content","type","session","Pode_"]
  # Um dicionário com as palavras em inglês e suas traduções em português
  translations = {
  "Can": "Pode",
  "add": "adicionar",
  "change": "alterar",
  "delete": "excluir",
  "view": "visualizar",
  "group": "grupo",
  "entry": "entrada",
  "permission": "permissao",
  "user": "usuario",
  "content": "conteudo",
  "type": "tipo",
  "session": "sessao",
  "Pode_":"Pode"
  }
  
    # Obtém todas as permissões do banco de dados
  permissions = Permission.objects.all()

    # Para cada permissão, separa o nome em palavras
  for perm in permissions:
    permission_words = perm.name.split()

    # Para cada palavra da permissão, verifica se ela está no array de palavras
    for word in permission_words:
      if word in words:
    # Se estiver, substitui pela tradução correspondente no dicionário
        index = permission_words.index(word)
        permission_words[index] = translations[word]

    # Junta as palavras traduzidas em uma string
    translated_name = " ".join(permission_words)

    # Atribui o nome traduzido à permissão
    perm.name = translated_name

    # Salva a permissão traduzida no banco de dados
    perm.save()
  
traduzir_permissoes.short_description = "Traduzir Permissões"
class Permission_Admin(admin.ModelAdmin):
    actions = [traduzir_permissoes]
    
admin.site.register(Compromisso, CompromissoAdmin)
admin.site.register(Local)
admin.site.register(Convidado, ConvidadoAdmin)
admin.site.register(Anotacao_Compromisso, Anotacao_CompromissoAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
# admin.site.unregister(Permission)
admin.site.register(Permission,Permission_Admin)
