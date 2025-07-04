import math

def d(p1, p2):
    return math.sqrt( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )

p1 = (1, 1)
p2 = (2, 2)

print("Distancia entre os pontos {} e {}: {}".format(p1, p2, d(p1, p2)))
