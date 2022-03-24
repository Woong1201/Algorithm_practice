import sys
import itertools

def Manhattan_distance (x, y):
    return (abs(x[0]-y[0]) + abs(x[1]-y[1]))

def chicken_distance(house, chicken):
    min_len = 2*N
    for c in chicken:
        if min_len > Manhattan_distance(house, c):
            min_len = Manhattan_distance(house, c)
    return min_len

N, M = map(int, sys.stdin.readline().split())

houses = []
chickens = []

for row in range(N):
    city = list(map(int, sys.stdin.readline().split()))
    for col, c in enumerate(city):
        if c == 1:
            houses.append((row,col))
        elif c == 2:
            chickens.append((row,col))

city_chicken_distance = 2*N*2*N
for chicken in list(itertools.combinations(chickens, M)):
    distance = 0
    for house in houses:
        distance += chicken_distance(house, chicken)
    city_chicken_distance = min(distance, city_chicken_distance)

print(city_chicken_distance)