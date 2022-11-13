from simulations import derivaService


def derivaComGargalo(geracoes, p, popSize, geracaoGargalo, popGargalo):
    result = derivaService.rodaNGeracoes_deriva(geracaoGargalo-1, p, popSize)
    result = result + derivaService.rodaNGeracoes_deriva(
        geracoes - geracaoGargalo + 1, result[geracaoGargalo-2], popGargalo)
    return result
