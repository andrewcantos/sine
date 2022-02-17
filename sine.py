import math

def sine_term(theta, n):
    return pow(theta, n)/math.prod(list(range(1,n+1)))

def approx_sine(theta_degrees, terms=10):
    theta_radians = theta_degrees*math.pi/180
    answer = math.sin(theta_radians)
    print(f'Approximating sin({theta_degrees}°). Correct value is {answer:.8f}')
    res = 0
    sign = True
    for i in range(1, terms*2+1, 2):
        term = sine_term(theta_radians, i) * (1 if sign else -1)
        res += term
        sign = not sign
        err = 100*(answer-res)/answer
        print(f'Sine of {theta_degrees}° is approx. {res:.6f} (Δ={term:.6f}), error={err:.2f}%')
        if abs(err) < 0.01:
            break
    return res

approx_sine(theta_degrees=87, terms=7)