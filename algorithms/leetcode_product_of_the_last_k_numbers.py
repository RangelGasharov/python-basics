class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]


productOfNumbers = ProductOfNumbers()
productOfNumbers.add(4)
productOfNumbers.add(2)
productOfNumbers.add(1)
productOfNumbers.add(10)
print(productOfNumbers.getProduct(3))
