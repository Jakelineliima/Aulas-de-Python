from django.http import JsonResponse
from rest_framework import viewsets

from escola.models import Aluno, Curso
from escola.serializer import AlunoSerializer


def alunos(request):
    if request.method == 'GET':
        aluno = {'id': 1, 'nome': 'Eder'}
        return JsonResponse(aluno)


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursoSerializer(object):
    pass


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
