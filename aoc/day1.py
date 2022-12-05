import heapq

with open('../resources/day1_input.txt', 'r') as in_file:
    heap = []
    current = 0

    for line in in_file:
        text = line.strip()
        if text == '':
            heapq.heappush(heap, current)
            current = 0
        else:
            current -= int(text)

    if current != 0:
        heapq.heappush(heap, current)
        current = 0

    print(f'Largest 3: ')
    for _ in range(3):
        print(heapq.heappop(heap))
