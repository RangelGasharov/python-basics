from typing import List


def read_binary_watch(turned_on: int) -> List[str]:
    result = []

    for hour in range(12):
        for minute in range(60):
            if (bin(hour).count("1") + bin(minute).count("1")) == turned_on:
                time = f"{hour}:{minute:02d}"
                result.append(time)
    return result

print(read_binary_watch(0))
print(read_binary_watch(2))
print(read_binary_watch(3))
print(read_binary_watch(9))
