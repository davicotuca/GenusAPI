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


def deriva(request):

    popSize = request.query_params.get('population_size')
    generations = request.query_params.get('generations')
    initialPop = request.query_params.get('initial_p')
    pops = request.query_params.get('populations')

    try:
        popSize = int(popSize)
        generations = int(generations)
        pops = int(pops)
        initialPop = float(initialPop)
    except ValueError:
        return Response({"message": "Parameters don't follow the expects" +
                         " format! population_size, generations," +
                         " initial_p, populations"})

    result = {}

    for x in range(0, pops):
        result[x] = derivaService.rodaNGeracoes_deriva(
            generations, initialPop, popSize)
    return Response(result)


def derivaGargalo(request):

    popSize = request.query_params.get('population_size')
    generations = request.query_params.get('generations')
    initialPop = request.query_params.get('initial_p')
    pops = request.query_params.get('populations')
    geracaoGargalo = request.query_params.get('geracaoGargalo')
    popGargalo = request.query_params.get('popGargalo')

    try:
        popSize = int(popSize)
        generations = int(generations)
        pops = int(pops)
        initialPop = float(initialPop)
        geracaoGargalo = int(geracaoGargalo)
        popGargalo = int(popGargalo)
    except ValueError:
        return Response({"message": "Parameters don't follow the expected"})

    result = {}

    for x in range(0, pops):
        result[x] = gargaloService.derivaComGargalo(
            generations, initialPop, popSize, geracaoGargalo, popGargalo)
    return Response(result)


def selecao(query_params):
    geracoes = query_params.get('generations')
    initialPop = query_params.get('initial_p')
    WAA = query_params.get('WAA')
    WAa = query_params.get('WAa')
    Waa = query_params.get('Waa')

    try:
        initialPop = float(initialPop)
        geracoes = int(geracoes)
        WAA = float(WAA)
        WAa = float(WAa)
        Waa = float(Waa)
    except ValueError:
        return Response({"message": "Parameters don't follow the expected"})

    result = selecaoService.selecao(initialPop, WAA, WAa, Waa, geracoes)
    return Response(result)


def selecaoDeriva(request):
    geracoes = request.query_params.get('generations')
    initialPop = request.query_params.get('initial_p')
    WAA = request.query_params.get('WAA')
    WAa = request.query_params.get('WAa')
    Waa = request.query_params.get('Waa')
    popSize = request.query_params.get('population_size')

    try:
        initialPop = float(initialPop)
        geracoes = int(geracoes)
        WAA = float(WAA)
        WAa = float(WAa)
        Waa = float(Waa)
        popSize = int(popSize)
    except ValueError:
        return Response({"message": "Parameters don't follow the expected"})

    result = derivaSelecaoService.selecaoDeriva(initialPop, WAA, WAa, Waa, geracoes, popSize)

    return Response(result)


def selecaoMutacao(request):
    geracoes = request.query_params.get('generations')
    p = request.query_params.get('initial_p')
    s = request.query_params.get('s')
    h = request.query_params.get('h')
    u = request.query_params.get('u')

    try:
        p = float(p)
        geracoes = int(geracoes)
        s = float(s)
        h = float(h)
        u = float(u)
    except ValueError:
        return Response({"message": "Parameters don't follow the expected"})

    result = selecaoMutacaoService.selecaoComMutacao(p, s, h, u, geracoes)
    return Response(result)


@api_view(['GET'])
def simulacaoGeral(request):

    if "generations" in request.query_params and "initial_p" in request.query_params:
        if "population_size" in request.query_params and "populations" in request.query_params:
            if "geracaoGargalo" in request.query_params and "popGargalo" in request.query_params:
                return derivaGargalo(request)
            else:
                deriva(request)
        if "WAA" in request.query_params and "WAa" in request.query_params and "Waa" in request.query_params:
            if "population_size" in request.query_params:
                return selecaoDeriva(request)
            else:
                return selecao(request.query_params)
        if 's' in request.query_params and 'h' in request.query_params and 'u' in request.query_params:
            return selecaoMutacao(request)

    return Response({"message": "Error, given parameters don't match any simulation available"})

# @api_view(['POST'])
# def simulacao(request):
#     respJson = json.loads(request.body)

#     resultados = Resultados.objects.create(
#         resultado =  respJson['resultado']
#     )

#     print("olha o resutado  ")
#     print(resultados.resultado)

#     paramJson = respJson['parametros']

#     parametros = Parametros.objects.create(
#         pop_size = paramJson["pop_size"],
#         generations = paramJson["generations"],
#         pop_bottleneck = paramJson["pop_bottleneck"],
#         generation_bottleneck = paramJson["generation_bottleneck"],
#         p_inicial = paramJson["p_inicial"],
#         WAA = paramJson["WAA"],
#         WAa = paramJson["WAa"],
#         Waa = paramJson["Waa"],
#         s = paramJson["s"],
#         h = paramJson["h"],
#         u = paramJson["u"],
#     )

#     simulacao = Simulacao.objects.create(
#         resultado = resultados,
#         parametros = parametros,
#         nome = respJson['simulacao_nome']
#     )

#     grupo = Grupo.objects.get(id=respJson['grupoID'])

#     rGrupoSimulação = GrupoSimulacao.objects.create(
#         grupo = grupo,
#         simulacao = simulacao
#     )

#     print(rGrupoSimulação.simulacao.nome)
#     print(rGrupoSimulação.grupo.nome)
#     print(parametros.pop_size)
#     print(resultados.resultado)
#     print(simulacao.nome)


#     return Response({"message": simulacao.nome})


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
