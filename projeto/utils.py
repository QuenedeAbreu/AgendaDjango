
from django.contrib.auth.models import Permission

def translate_permission_words():
  
  words = ["Can", "add", "change", "delete", "view"]
  # Um dicionário com as palavras em inglês e suas traduções em português
  translations = {
  "Can": "Pode",
  "add": "adicionar",
  "change": "alterar",
  "delete": "excluir",
  "view": "visualizar"
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