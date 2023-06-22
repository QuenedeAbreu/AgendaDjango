from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from agenda.models import Local, Convidado, Compromisso

from agenda.serializers import UserSerializer, GroupSerializer, LocalSerializer, CompromissoSerializer, ConvidadoSerializer


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
    queryset = Compromisso.objects.all()
    serializer_class = CompromissoSerializer
    permission_classes = [permissions.IsAuthenticated]
