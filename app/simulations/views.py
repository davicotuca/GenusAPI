"""
    Views for  the simulations
"""
from simulations import derivaService
from simulations import gargaloService
from simulations import selecaoService

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
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

@api_view(['GET'])
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

@api_view(['GET'])
def selecao(request):
    geracoes = request.query_params.get('generations')
    initialPop = request.query_params.get('initial_p')
    WAA = request.query_params.get('WAA')
    WAa = request.query_params.get('WAa')
    Waa = request.query_params.get('Waa')

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