from django.contrib.auth.models import User, Group
from agenda.models import Local, Convidado, Compromisso, Anotacao_Compromisso
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


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class ConvidadoSerializer(serializers.HyperlinkedModelSerializer):
    compromisso_set = CompromissoSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Convidado
        fields = ['id', 'url', 'nome', 'email', 'compromisso_set', 'user']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UserAnotacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email']


class CompromissoAnotacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Compromisso
        fields = ['id', 'url', 'descricao', 'data_inicio',
                  'data_fim']


class Anotacao_CompromissoSerializer(serializers.HyperlinkedModelSerializer):
    compromisso = CompromissoAnotacaoSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Anotacao_Compromisso
        fields = ['id', 'url', 'compromisso', 'descricao', 'data', 'user']
