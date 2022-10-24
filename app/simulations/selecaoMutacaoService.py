def selecaoComMutacao(p, s, h, u, geracoes):
    result = []
    result.append(p)
    WAA = 1
    WAa = 1-h*s
    Waa = 1 - s
    for i in range(0, geracoes):
        currentP = result[i]
        nextP = (currentP*WAA + (1-currentP)*WAa)*(1-u)/(Waa)*currentP
        result.append(nextP)

    return result
