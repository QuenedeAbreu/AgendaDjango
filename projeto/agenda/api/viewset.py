from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from agenda.models import Local, Convidado, Compromisso, Anotacao_Compromisso
from agenda.api.serializers import UserSerializer, GroupSerializer, LocalSerializer, CompromissoSerializer, ConvidadoSerializer, Anotacao_CompromissoSerializer


def index_view_app(request):
    return render(request, 'index.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViweSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocalViweSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
    permission_classes = [permissions.IsAuthenticated]


class ConvidadoViweSet(viewsets.ModelViewSet):
    queryset = Convidado.objects.all()
    serializer_class = ConvidadoSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompromissoViweSet(viewsets.ModelViewSet):
    # queryset = Compromisso.objects.get_queryset()
    queryset = Compromisso.objects.all()
    serializer_class = CompromissoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields= ['descricao','data_inicio']
    
    def get_queryset(self):
        desc = self.request.query_params.get('descricao')
        queryset = Compromisso.objects.all()
        if desc is not None:
            queryset = queryset.filter(descricao=desc)
        return queryset   
    
    # def get_queryset(self):
    #     usuario = self.request.user
    #     convidado = Convidado.objects.filter(user = usuario)
    #     return Compromisso.objects.filter(Convidados = convidado[0])


class Anotacao_CompromissoViweSet(viewsets.ModelViewSet):
    queryset = Anotacao_Compromisso.objects.all()
    serializer_class = Anotacao_CompromissoSerializer
    permission_classes = [permissions.IsAuthenticated]

