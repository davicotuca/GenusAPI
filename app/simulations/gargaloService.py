from simulations import derivaService


def derivaComGargalo(geracoes, p, popSize, geracaoGargalo, popGargalo):
    firstPart = geracoes - geracaoGargalo
    secondPart = geracoes - firstPart
    result = derivaService.rodaNGeracoes_deriva(firstPart, p, popSize)
    result = result + derivaService.rodaNGeracoes_deriva(
        secondPart, result[geracaoGargalo-1], popGargalo)
    return result
