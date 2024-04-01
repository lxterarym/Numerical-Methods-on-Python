import math

def f(x):
    return 19 * math.exp(x) * math.cos(x) - 9 * math.exp(math.sin(x)) - 7 * math.log(x**2 + 1) + 7
def regula_falsi_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) > 0:
        print("There is a no zero point in this zone")
        return None
    iter_count = 0
    while abs(func(b)) > tol and iter_count < max_iter:
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if func(c) == 0:
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    return c
a = -0.5
b = 1.8
result = regula_falsi_method(f, a, b)
if result is not None:
    print("Regular Falsi Method Root:", result)
else:
    print("not found")

