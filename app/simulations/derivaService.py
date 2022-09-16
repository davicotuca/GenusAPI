import random


def rodaNGeracoes_deriva(geracoes, p, popSize):
    result = []
    lastPopP = p
    for x in range(0, geracoes):
        lastPopP = proximaGeracaoP(popSize, lastPopP)
        result.append(lastPopP)
    return result


def proximaGeracaoP(popSize, p):
    sum = 0
    randomPop = random.choices([0, 1], weights=(1-p, p), k=popSize)

    for i in range(0, len(randomPop)):
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
