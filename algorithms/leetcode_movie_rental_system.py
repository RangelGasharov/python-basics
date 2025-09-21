from typing import List
from collections import defaultdict
from sortedcontainers import SortedList


class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.available_movies = defaultdict(SortedList)
        self.shop_and_movie_to_price = {}
        self.rented = SortedList()

        for shop, movie, price in entries:
            self.available_movies[movie].add((price, shop))
            self.shop_and_movie_to_price[(shop, movie)] = price

    def search(self, movie: int) -> List[int]:
        return [shop for _, shop in self.available_movies[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_and_movie_to_price[(shop, movie)]
        self.available_movies[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.shop_and_movie_to_price[(shop, movie)]
        self.available_movies[movie].add((price, shop))
        self.rented.remove((price, shop, movie))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for _, shop, movie in self.rented[:5]]


movie_renting_system = MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]])
print(movie_renting_system.search(1))
movie_renting_system.rent(0, 1)
movie_renting_system.rent(1, 2)
print(movie_renting_system.report())
movie_renting_system.drop(1, 2)
print(movie_renting_system.search(2))
