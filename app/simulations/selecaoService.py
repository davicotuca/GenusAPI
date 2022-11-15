def selecao(p, WAA, WAa, Waa, geracoes):
    result = []
    result.append(p)
    for i in range(0, geracoes):
        currentP = result[i]
        nextP = (currentP*WAA+(1-currentP)*WAa)/(currentP**2+2*currentP*(1-currentP)*WAa+(1-currentP)**2*Waa)*currentP
        result.append(nextP)
    return {"0": result}
