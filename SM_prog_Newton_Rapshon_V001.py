def newton(f, Df, x0, eps, max_iter):
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < eps:
            print('Solução encontrada depois de',n,'iterações.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Derivada Nula. Solução não encontrada.')
            return None
        xn = xn - fxn/Dfxn
    print('Excede o número máximo de iterações. Solução não encontrada.')
    return None

p = lambda x: x**3 - x**2 - 1
Dp = lambda x: 3*x**2 - 2*x
approx = newton(p,Dp,1,1e-10,10)
print(approx)