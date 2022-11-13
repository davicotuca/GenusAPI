"""
    Views for  the simulations
"""
# from app.core.models import User
from simulations import derivaService
from simulations import gargaloService
from simulations import selecaoService
from simulations import derivaSelecaoService
from simulations import selecaoMutacaoService

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import (
    viewsets,
    mixins,
)
from core.models import (
    Grupo,
    GrupoSimulacao
)
from simulations import serializers

listaParamGeral = ['population_size', 'generations', 'initial_p', 'populations', 'generation_bottleneck', 'pop_bottleneck', 'WAA', 'WAa', 'Waa', 'h', 'u', 's']


def extrai_valida(query_params, listaParams):
    result = []
    for x in listaParams:
        valor = query_params.pop(x)
        param_result = {'nome': x, 'valor': valor[0]}
        result.append(param_result)

    return extrai(result)


def extrai(listaParametros):
    result = {}
    for param in listaParametros:
        try:
            if(not param['valor'].upper() == 'NULL'):
                if(param['nome'] == 'population_size' or param['nome'] == 'generations' or param['nome'] == 'populations' or param['nome'] == 'generation_bottleneck' or param['nome'] == 'pop_bottleneck'):
                    valor = int(param['valor'])
                else:
                    valor = float(param['valor'])
                    param['valor'] = valor
                result[param['nome']] = valor
        except ValueError:
            return Response({"message": "Parameters don't follow the expected"})
    return result


def deriva(extractedParams):

    result = {}
    for x in range(0, extractedParams.get('populations')):
        result[x] = derivaService.rodaNGeracoes_deriva(
            extractedParams.get('generations'),
            extractedParams.get('initial_p'),
            extractedParams.get('population_size'))

    return Response(result)


def derivaGargalo(extractedParams):

    result = {}
    for x in range(0, extractedParams.get('populations')):
        result[x] = gargaloService.derivaComGargalo(
            extractedParams.get('generations'),
            extractedParams.get('initial_p'),
            extractedParams.get('population_size'),
            extractedParams.get('generation_bottleneck'),
            extractedParams.get('pop_bottleneck'))

    return Response(result)


def selecao(extractedParams):

    return Response(selecaoService.selecao(
        extractedParams.get('initial_p'),
        extractedParams.get('WAA'),
        extractedParams.get('WAa'),
        extractedParams.get('Waa'),
        extractedParams.get('generations')))


def selecaoDeriva(extractedParams):

    return Response(derivaSelecaoService.selecaoDeriva(
        extractedParams.get('initial_p'),
        extractedParams.get('WAA'),
        extractedParams.get('WAa'),
        extractedParams.get('Waa'),
        extractedParams.get('generations'),
        extractedParams.get('population_size')))


def selecaoMutacao(extractedParams):

    return Response(selecaoMutacaoService.selecaoComMutacao(
        extractedParams.get('initial_p'),
        extractedParams.get('s'),
        extractedParams.get('h'),
        extractedParams.get('u'),
        extractedParams.get('generations')))


@api_view(['GET'])
def simulacaoGeral(request):

    extractedParams = extrai_valida(request.query_params.copy(), listaParamGeral)

    if "generations" in extractedParams and "initial_p" in extractedParams:
        if "population_size" in extractedParams and "populations" in extractedParams:
            if "generation_bottleneck" in extractedParams and "pop_bottleneck" in extractedParams:
                print("deriva gargado")
                return derivaGargalo(extractedParams)
            else:
                print("deriva")
                return deriva(extractedParams)
        if "WAA" in extractedParams and "WAa" in extractedParams and "Waa" in extractedParams:
            if "population_size" in extractedParams:
                print("selecaoDeriva")
                return selecaoDeriva(extractedParams)
            else:
                print("selecao")
                return selecao(extractedParams)
        if 's' in extractedParams and 'h' in extractedParams and 'u' in extractedParams:
            print("selecaoMutacao")
            return selecaoMutacao(extractedParams)

    return Response({"message": "Error, given parameters don't match any simulation available"})


class GrupoViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    """Manage Grupo in the database."""
    serializer_class = serializers.GrupoSerializer
    queryset = Grupo.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter queryset to authenticated user."""
        return self.queryset.filter(user=self.request.user)


class GrupoSimulacaoViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    """Manage Grupo in the database."""
    serializer_class = serializers.GrupoSimulacaoSerializer
    queryset = GrupoSimulacao.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        originalQuerySet = self.queryset
        gruposID = Grupo.objects.all().filter(user=self.request.user).values('id')
        """Filter queryset to authenticated user."""
        filteredGrupoSimulacao = originalQuerySet.filter(grupo_id__in=gruposID)
        return filteredGrupoSimulacao
