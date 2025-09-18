import heapq


class TaskManager:
    def __init__(self, tasks):
        self.taskId_to_priority = {}
        self.taskId_to_userId = {}
        self.priority_heap = []

        for task in tasks:
            userId, taskId, priority = task
            self.taskId_to_priority[taskId] = priority
            self.taskId_to_userId[taskId] = userId
            heapq.heappush(self.priority_heap, (-priority, -taskId, taskId))

    def add(self, userId, taskId, priority):
        self.taskId_to_priority[taskId] = priority
        self.taskId_to_userId[taskId] = userId
        heapq.heappush(self.priority_heap, (-priority, -taskId, taskId))

    def edit(self, taskId, newPriority):
        self.taskId_to_priority[taskId] = newPriority
        heapq.heappush(self.priority_heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId) -> None:
        if taskId in self.taskId_to_priority:
            del self.taskId_to_priority[taskId]
            del self.taskId_to_userId[taskId]

    def execTop(self):
        while self.priority_heap:
            negPriority, negTaskId, taskId = heapq.heappop(self.priority_heap)
            if taskId in self.taskId_to_priority and self.taskId_to_priority[taskId] == -negPriority:
                userId = self.taskId_to_userId[taskId]
                del self.taskId_to_priority[taskId]
                del self.taskId_to_userId[taskId]
                return userId
        return -1
