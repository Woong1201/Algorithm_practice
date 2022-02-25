import sys
import itertools

def is_connected(cities):
    city1 = set(cities)
    city2 = all_cities - city1
    city1connect = [city1.pop()]
    city2connect = [city2.pop()]

    while len(city1):
        impossible = 0
        for city1_index in city1connect:
            for city in city1:
                if city1_index in city_connect[city]:
                    city1connect.append(city)
                    city1.remove(city)
                    impossible = 1
                    break
            if impossible == 1:
                break
        if impossible == 0:
            return -1
            
    while len(city2):
        impossible = 0
        for city2_index in city2connect:
            for city in city2:
                if city2_index in city_connect[city]:
                    city2connect.append(city)
                    city2.remove(city)
                    impossible = 1
                    break
            if impossible == 1:
                break
        if impossible == 0:
            return -1

    return 1

N = int(sys.stdin.readline())
all_cities = set([i for i in range(1, N+1)])
population = list(map(int, sys.stdin.readline().split()))
city_connect = {}

for city in range(1, N+1):
    connect = list(map(int, sys.stdin.readline().split()))
    city_connect[city] = connect[1:]

city_split = []
for i in range (1, (N+1)//2+1):
    city_split += list(itertools.combinations([j for j in range(1, N+1)], i))

min = -1
sum_pop = sum(population)
for cities in city_split:
    if is_connected(cities) == 1:
        pop = sum([population[i-1] for i in cities])
        if min > abs(2*pop - sum_pop) or min == -1:
            min = abs(2*pop - sum_pop)

print(min)