import random as random

C1 = ("p", "t", "k", "b", "d", "g", "m", "n", "tx", "x", "s", "z", "f", "r", "l", "y", "w")
C2 = ("p", "t", "k", "b", "d", "g", "m", "n", "ñ", "ts", "dz", "tx", "x", "s", "z", "f", "r", "l", "y", "w")
V = ("a", "i", "u", "e", "o")
N = ("m", "n", "s", "l", "r", "", "", "")

file1 = open("/Users/alexanderbrost/Documents/Python/export.txt", "w")

monosyllabic = 0
while monosyllabic <= 5:
    monosyllabic = monosyllabic + 1
    print((random.choice(C1) + random.choice(V) + random.choice(N)), file =file1)

disyllabic = 0
while disyllabic <= 5:
    disyllabic = disyllabic + 1
    print((random.choice(C1) + random.choice(V) + random.choice(N) + (random.choice(C2) + random.choice(V) + random.choice(N))), file =file1)


trisyllabic = 0
while trisyllabic <= 5:
    trisyllabic = trisyllabic + 1
    print(((random.choice(C1) + random.choice(V) + random.choice(N)) + (random.choice(C2) + random.choice(V) + random.choice(N) + (random.choice(C2) + random.choice(V) + random.choice(N)))), file =file1)




