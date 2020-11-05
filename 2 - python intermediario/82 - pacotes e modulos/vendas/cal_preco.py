from formata import preco


def aumento(vl, por, formata=False):
    r = vl + (vl * por / 100)
    if formata:
        return preco.real(r)
    else:
        return r


def reducao(vl, red, formata=False):
    r = vl - (vl * red / 100)
    if formata:
        return preco.real(r)
    else:
        return r
