from collections import defaultdict, deque


def find_all_people(n: int, meetings: list[list[int]], first_person: int) -> list[int]:
    time_meetings = defaultdict(list)
    for x, y, t in meetings:
        time_meetings[t].append((x, y))

    knows_secret = [False] * n
    knows_secret[0] = True
    knows_secret[first_person] = True

    for t in sorted(time_meetings.keys()):
        meetings = time_meetings[t]

        meet_list = defaultdict(list)
        for x, y in meetings:
            meet_list[x].append(y)
            meet_list[y].append(x)

        start = set()
        for x, y in meetings:
            if knows_secret[x]:
                start.add(x)
            if knows_secret[y]:
                start.add(y)

        q = deque(start)
        while q:
            person = q.popleft()
            for next_person in meet_list[person]:
                if not knows_secret[next_person]:
                    knows_secret[next_person] = True
                    q.append(next_person)

    return [i for i in range(n) if knows_secret[i]]


print(find_all_people(6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1))
print(find_all_people(4, [[3, 1, 3], [1, 2, 2], [0, 3, 3]], 3))
print(find_all_people(5, [[3, 4, 2], [1, 2, 1], [2, 3, 1]], 1))
