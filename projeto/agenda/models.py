from django.db import models
from django.utils.dateformat import DateFormat
from django.contrib.auth.models import User


def Format_Date(date):
    return DateFormat(date).format('d/m/Y')


class Local(models.Model):
    nome = models.CharField(max_length=255)
    rua = models.CharField(max_length=255, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    foto = models.ImageField(upload_to='ft_locais', null=True, blank=True)

    def __str__(self):
        return f'{self.nome} na rua {self.rua}'

    class Meta:
        verbose_name_plural = "Locais"


class Convidado(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.email}'

    class Meta:
        verbose_name_plural = "Convidados"


class Compromisso(models.Model):
    descricao = models.CharField(max_length=255)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    local = models.ForeignKey(
        Local, related_name="Local", on_delete=models.CASCADE)
    Convidados = models.ManyToManyField(Convidado, related_name="Convidados")
    registro = models.FileField(upload_to='arquivos', null=True, blank=True)

    def __str__(self):
        return f'{self.descricao} começa : {Format_Date(self.data_inicio)} - {Format_Date(self.data_fim)}'

    class Meta:
        verbose_name_plural = "Compromissos"


class Anotacao_Compromisso(models.Model):
    compromisso = models.ForeignKey(Compromisso, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=255)
    data = models.DateField()
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        null=True, blank=True)

    def __str__(self):
        return f'{self.compromisso} - {self.descricao} - {Format_Date(self.data)} - {self.user}'

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(Anotacao_Compromisso, self).save_model(
            request, obj, form, change)

    class Meta:
        verbose_name_plural = "Anotações nos Compromissos"
