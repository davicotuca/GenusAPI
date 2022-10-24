from simulations import derivaService

from simulations import selecaoService


def selecaoDeriva(p, WAA, WAa, Waa, geracoes, popSize):
    result = []
    result.append(p)

    for i in range(0, geracoes):
        currentP = result[i]
        currentP = selecaoService.selecao(currentP, WAA, WAa, Waa, 1)
        currentP = derivaService.proximaGeracaoP(popSize, currentP[1])
        result.append(currentP)
    return result
