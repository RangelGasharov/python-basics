import heapq


class TaskManager:
    def __init__(self, tasks):
        self.task_id_to_priority = {}
        self.task_id_to_user_id = {}
        self.priority_heap = []

        for task in tasks:
            user_id, task_id, priority = task
            self.task_id_to_priority[task_id] = priority
            self.task_id_to_user_id[task_id] = user_id
            heapq.heappush(self.priority_heap, (-priority, -task_id, task_id))

    def add(self, user_id, task_id, priority):
        self.task_id_to_priority[task_id] = priority
        self.task_id_to_user_id[task_id] = user_id
        heapq.heappush(self.priority_heap, (-priority, -task_id, task_id))

    def edit(self, task_id, new_priority):
        self.task_id_to_priority[task_id] = new_priority
        heapq.heappush(self.priority_heap, (-new_priority, -task_id, task_id))

    def rmv(self, task_id) -> None:
        if task_id in self.task_id_to_priority:
            del self.task_id_to_priority[task_id]
            del self.task_id_to_user_id[task_id]

    def exec_top(self):
        while self.priority_heap:
            neg_priority, neg_task_id, task_id = heapq.heappop(self.priority_heap)
            if task_id in self.task_id_to_priority and self.task_id_to_priority[task_id] == -neg_priority:
                user_id = self.task_id_to_user_id[task_id]
                del self.task_id_to_priority[task_id]
                del self.task_id_to_user_id[task_id]
                return user_id
        return -1
