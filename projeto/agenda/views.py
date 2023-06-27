from django.http import HttpResponse
from .models import Local
from django.template import loader
def lista_locais(request):
  locais = Local.objects.all()
  teste = request.user 
  if  request.user == 'AnonymousUser':
    teste = 'Não logado'
    
  context = {
    'locais':locais,
    'usuario':teste 
  }
  template = loader.get_template('locais.html')
  return HttpResponse(template.render(context,request))