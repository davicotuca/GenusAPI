def selecao(p, WAA, WAa, Waa, geracoes):
    result = []
    result.append(p)
    for i in range(0, geracoes):
        currentP = result[i]
        nextP = (currentP*WAA+(1-currentP)*WAa)/(currentP**2+2*currentP*(1-currentP)*WAa+(1-currentP)**2*Waa)*currentP
        result.append(nextP)
    return result

def selecaoMutacao(p, s, h, u, geracoes):
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
