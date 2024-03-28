poly = {"Tetrahedron":4,
        "Cube":6,
        "Octahedron":8,
        "Dodecahedron":12,
        "Icosahedron":20,}
sum = 0
for i in range(int(input())):
    a = input()
    sum += poly[a]
print(sum)