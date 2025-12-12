def count_mentions(number_of_users: int, events: list[list[str]]) -> list[int]:
    mentions = [0] * number_of_users
    back = [0] * number_of_users
    events.sort(key=lambda e: (int(e[1]), e[0] == "MESSAGE"))

    for typ, timestamp, data in events:
        timestamp = int(timestamp)
        if typ == "OFFLINE":
            back[int(data)] = timestamp + 60
            continue

        for mention_type in data.split():
            if mention_type == "ALL":
                for user_id in range(number_of_users):
                    mentions[user_id] += 1
            elif mention_type == "HERE":
                for user_id in range(number_of_users):
                    if timestamp >= back[user_id]:
                        mentions[user_id] += 1
            else:
                mentions[int(mention_type[2:])] += 1

    return mentions


print(count_mentions(2, [["MESSAGE", "10", "id1 id0"], ["OFFLINE", "11", "0"], ["MESSAGE", "71", "HERE"]]))
print(count_mentions(2, [["MESSAGE", "10", "id1 id0"], ["OFFLINE", "11", "0"], ["MESSAGE", "12", "ALL"]]))
print(count_mentions(2, [["OFFLINE", "10", "0"], ["MESSAGE", "12", "HERE"]]))
