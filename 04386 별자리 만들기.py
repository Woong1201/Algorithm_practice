import math
import sys

N = int(input())
stars = []

for i in range(N):
    stars.append(list(map(float, sys.stdin.readline().split())))

distances = []
for i in range(N):
    j = i + 1
    while j < N:
        distance = math.sqrt((stars[i][0]-stars[j][0])**2+(stars[i][1]-stars[j][1])**2)
        distances.append([distance, i, j])
        j += 1

distances.sort(key=lambda x:-x[0])
parents = {}
childs = {}
star_distance = 0
lines = 0

while lines < N - 1:
    distance, star1, star2 = distances.pop()
    if childs.get(star1, -1) == childs.get(star2, -1) != -1:
        continue

    star_distance += distance
    lines += 1
    if star1 not in childs and star2 not in childs:
        parents[star1] = set([star1, star2])
        childs[star1] = star1
        childs[star2] = star1
    elif star1 not in childs:
        parents[childs[star2]].add(star1)
        childs[star1] = childs[star2]
    elif star2 not in childs:
        parents[childs[star1]].add(star2)
        childs[star2] = childs[star1]
    elif childs[star1] != childs[star2]:
        if len(parents[childs[star1]]) >= len(parents[childs[star2]]):
            parents[childs[star1]] |= parents[childs[star2]]
            new_stars = parents.pop(childs[star2])
            for star in new_stars:
                childs[star] = childs[star1]
        else:
            parents[childs[star2]] |= parents[childs[star1]]
            new_stars = parents.pop(childs[star1])
            for star in new_stars:
                childs[star] = childs[star2]

print(star_distance)