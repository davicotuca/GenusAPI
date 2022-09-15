"""
    Views for  the simulations
"""
import random

from rest_framework.response import Response
from rest_framework.decorators import api_view

def rodaNGeracoes(n, p, popSize):
    result = []
    for x in range(0, n):
        p = proximaGeracaoP(popSize, p)
        result.append(p)
    return result

def proximaGeracaoP(popSize, p):
    sum = 0
    randomPop = random.choices([0,1], weights=(p,1-p), k=popSize)

    for i in range (0, len(randomPop)):
        sum = sum + randomPop[i]

    return sum/popSize
        
# def proximaGeracao(popAtual):
#     proxPop =[]
#     for x in range(0, len(popAtual)):
#         randomInd = random.choice(popAtual)
#         proxPop.append(randomInd)
#     return proxPop

# def montaVetor(popSize, popProportion):
#     p = int(popSize*popProportion)
#     q = popSize - p
#     result = []
#     for x in range(0, p):
#         result.append(1)
#     for x in range(0, q):
#         result.append(0)
#     return result


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
    except:
        return Response({"message": "Parameters don't follow the expects format! population_size, generations, initial_p, populations"})
    
    result = {}

    for x in range(0, pops):
         result[x] = rodaNGeracoes(generations, initialPop, popSize)
    return Response(result)

