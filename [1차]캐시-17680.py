def solution(cacheSize, cities):
    answer = 0
    c = []

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.upper()

        # hit
        if city in c:
            c.remove(city)
            c.append(city)
            answer += 1
            continue

        # miss - 가득 차지 않은 경우
        if len(c) != cacheSize:
            c.append(city)
            answer += 5
        # miss - 가득찬 경우
        else:
            c.pop(0)
            c.append(city)
            answer += 5

    return answer