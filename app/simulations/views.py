"""
    Views for  the simulations
"""
from simulations import derivaService

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
