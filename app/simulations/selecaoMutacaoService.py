def selecaoComMutacao(p, s, h, u, geracoes):
    result = []
    result.append(p)
    for i in range(0, geracoes):
        currentP = result[i]
        print(currentP)
        q = 1 - currentP
        x = (currentP * (1.0 - q * h * s) * (1.0 - u))
        wBar = (1.0 - s * q * (q + 2.0 * p * h))
        nextP = (x/wBar)
        result.append(round(nextP, 10))

    return result
