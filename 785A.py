n = int(input())
words = []
sum = int('0')
side_counts = {
    'Tetrahedron' : 4,
    'Cube' : 6,
    'Octahedron' : 8,
    'Dodecahedron' : 12,
    'Icosahedron' : 20
}
for i in range (n) :
    words.append(input())
for word in words :
    sum += side_counts[word]
print(sum)
