from math import sqrt
from math import cos
from math import acos
from math import sin
from math import asin


def arcG(A, B, C):
    R = sqrt((C[0] - A[0]) ** 2 + (C[1] - A[1]) ** 2)
    coeff = round(sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2) / 6) + 3
    AB = [B[0] - A[0], B[1] - A[1]]
    CA = [A[0] - C[0], A[1] - C[1]]
    alpha = asin(sqrt(AB[0] ** 2 + AB[1] ** 2) / (2 * R)) / 3.14159265 * 360  # calcul de l'angle
    omega = alpha / coeff
    lCord = []

    for i in range(1, coeff):
        cordx = 0
        cordy = 0
        lCord.append([cordx, cordy])

    print(C[0] + sin(10/360*2*3.14159265) * R * (-1 if CA[0] < 0 else 1))
    print(C[1] + cos(10/360*2*3.14159265) * R * (-1 if CA[1] < 0 else 1))

    #print(C[0] + CA[0] + sin(10 / 360 * 2 * 3.14159265) * R, C[1] + CA[1] + cos(10 / 360 * 2 * 3.14159265) * R)

    print('coeff = ' + str(coeff) + ', R = ' + str(R) + ', AB = ' + str(AB) + ', C = ' + str(C) + ', alpha = ' + str(
        alpha) + ', Omega = ' + str(omega) + ', CA = ' + str(CA))


arcG((15, 75), (170, -5), (170, 185))
