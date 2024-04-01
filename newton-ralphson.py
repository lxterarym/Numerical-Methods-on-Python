import math

def f(x):
    return 19 * math.exp(x) * math.cos(x) - 9 * math.exp(math.sin(x)) - 7 * math.log(x**2 + 1) + 7

def f_prime(x):
    return 19 * math.exp(x) * (math.cos(x) - math.sin(x)) - (18 * math.exp(math.sin(x)) * math.cos(x)) / (math.exp(2*math.sin(x)) + 1) + (14 * x) / (x**2 + 1)

def newton_raphson(initial_guess, tolerance=1e-6, max_iterations=100):
    x = initial_guess
    iteration = 0

    while abs(f(x)) > tolerance and iteration < max_iterations:
        x = x - f(x) / f_prime(x)
        iteration += 1

    if abs(f(x)) <= tolerance:
        return x
    else:
        raise ValueError("Newton-Raphson method did not converge.")

initial_guess = 1.0
result = newton_raphson(initial_guess)
print("Newton-Ralphson Method Root:", result)
