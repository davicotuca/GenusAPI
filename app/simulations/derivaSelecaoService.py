
from simulations import derivaService

from simulations import selecaoService


def selecaoDeriva(p, WAA, WAa, Waa, geracoes, popSize, populations):
    result = {}

    for j in range(0, populations):
        pop = []
        pop.append(p)

        for i in range(0, geracoes):
            currentP = pop[i]
            currentP = selecaoService.selecao(currentP, WAA, WAa, Waa, 1)
            currentP = derivaService.proximaGeracaoP(popSize, currentP['0'][1])
            pop.append(currentP)
        result[j] = pop

    return result
