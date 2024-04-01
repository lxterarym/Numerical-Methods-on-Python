import math

def f(x):
    return 19 * math.exp(x) * math.cos(x) - 9 * math.exp(math.sin(x)) - 7 * math.log(x + 1) + 7

def ikiye_bolme(Xl, Xu, tol=1e-6, max_iter=100):
    iter_count = 0

    while (Xu - Xl) / 2 > tol and iter_count < max_iter:
        Xr = (Xl + Xu) / 2
        f_Xl = f(Xl)
        f_Xr = f(Xr)

        if f_Xr == 0:
            return Xr
        elif f_Xl * f_Xr < 0:
            Xu = Xr
        else:
            Xl = Xr

        iter_count += 1

    Xr = (Xl + Xu) / 2
    return Xr

# Başlangıç değerleri
Xl = -0.5
Xu = 1.8

# İkiye Bölme yöntemini kullanarak kökü bul
kok = ikiye_bolme(Xl, Xu)

print("Denklemin kökü:", kok)