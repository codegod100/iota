def S(x):
    return lambda y: lambda z: x(z)(y(z))

def K(x):
    return lambda y: x

def I(x):
    return x # S(K)(K)

def iota(x):
    return x(S)(K)

f = iota(iota) # iota(S)(K) == S(S)(K)

f = iota(I) # I(S)(K) == S(K)
print(f)