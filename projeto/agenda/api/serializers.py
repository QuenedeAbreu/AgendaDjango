from django.contrib.auth.models import User, Group
from agenda.models import Local, Convidado, Compromisso, Anotacao_Compromisso
from rest_framework import serializers

# Compromisso -----


class LocalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Local
        fields = ['id', 'url', 'nome', 'rua', 'numero','foto']


class Convidado_Edit_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Convidado
        fields = ['id', 'url', 'nome', 'email']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class Compromisso_Edit_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Compromisso
        fields = ['id', 'url', 'descricao', 'data_inicio',
                  'data_fim','registro']


class Anotacao_CompromissoSerializer(serializers.HyperlinkedModelSerializer):
    compromisso = Compromisso_Edit_Serializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Anotacao_Compromisso
        fields = ['id', 'url', 'compromisso', 'descricao', 'data', 'user']


class Anotacao_Compromisso_Edit_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anotacao_Compromisso
        fields = ['id', 'url', 'descricao', 'data']


class CompromissoSerializer(serializers.HyperlinkedModelSerializer):
    Convidados = Convidado_Edit_Serializer(many=True, read_only=True)
    local = LocalSerializer(many=False, read_only=True)
    anotacao_compromisso_set = Anotacao_Compromisso_Edit_Serializer(
        many=True, read_only=True)

    class Meta:
        model = Compromisso
        fields = ['id', 'url', 'descricao', 'data_inicio',
                  'data_fim', 'local', 'Convidados', 'anotacao_compromisso_set','registro']


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
