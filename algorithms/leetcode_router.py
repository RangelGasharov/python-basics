from collections import deque, defaultdict
import bisect


class Router:

    def __init__(self, memory_limit: int):
        self.memoryLimit = memory_limit
        self.packets = deque()
        self.packets_seen = set()
        self.timestamps_by_dst = defaultdict(deque)

    def add_packet(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)

        if packet in self.packets_seen:
            return False

        if len(self.packets) == self.memoryLimit:
            old = self.packets.popleft()
            self.packets_seen.remove(old)

            old_src, old_dst, old_ts = old
            self.timestamps_by_dst[old_dst].popleft()
            if not self.timestamps_by_dst[old_dst]:
                del self.timestamps_by_dst[old_dst]

        self.packets.append(packet)
        self.packets_seen.add(packet)
        self.timestamps_by_dst[destination].append(timestamp)
        return True

    def forward_packet(self) -> list[int]:
        if not self.packets:
            return []
        packet = self.packets.popleft()
        self.packets_seen.remove(packet)
        src, dst, ts = packet
        self.timestamps_by_dst[dst].popleft()
        if not self.timestamps_by_dst[dst]:
            del self.timestamps_by_dst[dst]
        return list(packet)

    def get_count(self, destination: int, start_time: int, end_time: int) -> int:
        timestamps = self.timestamps_by_dst[destination]
        left = bisect.bisect_left(timestamps, start_time)
        right = bisect.bisect_right(timestamps, end_time)
        return right - left
