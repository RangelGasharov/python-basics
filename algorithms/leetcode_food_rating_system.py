import heapq


class FootRatings:
    def __init__(self, foods, cuisines, ratings):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_heap = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r
            if c not in self.cuisine_to_heap:
                self.cuisine_to_heap[c] = []
            heapq.heappush(self.cuisine_to_heap[c], (-r, f))

    def change_rating(self, food, new_rating):
        cuisine = self.food_to_cuisine[food]
        self.food_to_rating[food] = new_rating
        heapq.heappush(self.cuisine_to_heap[cuisine], (-new_rating, food))

    def highest_rating(self, cuisine):
        heap = self.cuisine_to_heap[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)


footRatings = FootRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                          ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
                          [9, 14, 8, 15, 14, 7])

print(footRatings.food_to_rating["kimchi"])
footRatings.change_rating("kimchi", 10)
print(footRatings.food_to_rating["kimchi"])
print(footRatings.highest_rating("japanese"))
print(footRatings.highest_rating("greek"))
