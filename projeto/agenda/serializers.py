from django.contrib.auth.models import User, Group
from agenda.models import Local, Convidado, Compromisso
from rest_framework import serializers

# Compromisso -----


class LocalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Local
        fields = ['id', 'url', 'nome', 'rua', 'numero']


class ConvidadoSerializer_Compromisso(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Convidado
        fields = ['id', 'url', 'nome', 'email']


class CompromissoSerializer(serializers.HyperlinkedModelSerializer):
    Convidados = ConvidadoSerializer_Compromisso(many=True, read_only=True)
    local = LocalSerializer(many=False, read_only=True)

    class Meta:
        model = Compromisso
        fields = ['id', 'url', 'descricao', 'data_inicio',
                  'data_fim', 'local', 'Convidados']


class ConvidadoSerializer(serializers.HyperlinkedModelSerializer):
    compromisso_set = CompromissoSerializer(many=True, read_only=True)

    class Meta:
        model = Convidado
        fields = ['id', 'url', 'nome', 'email', 'compromisso_set']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    model = Group
    fields = ['url', 'name']
