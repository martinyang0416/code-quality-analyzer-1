import heapq

def minRefuelStops(target, startFuel, stations):
    heap = []
    prev_pos = 0
    current_fuel = startFuel
    stops = 0
    for pos, fuel in stations:
        distance = pos - prev_pos
        while current_fuel < distance:
            if not heap:
                return -1
            current_fuel += -heapq.heappop(heap)
            stops += 1
        current_fuel -= distance
        prev_pos = pos
        heapq.heappush(heap, -fuel)
    remaining = target - prev_pos
    while 