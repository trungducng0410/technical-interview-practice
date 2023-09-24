from collections import deque
from datetime import datetime


class Animal:
    def __init__(self, type):
        self.type = type
        self.createdAt = datetime.now()


class AnimalShelter:
    def __init__(self):
        self.data = deque()

    # O(1)
    def enqueue(self, animal):
        self.data.append(animal)

    # O(1)
    def dequeueAny(self):
        if self.isEmpty():
            return None

        return self.data.popleft()

    # O(n)
    def dequeueCat(self):
        return self.dequeue("CAT")

    # O(n)
    def dequeueDog(self):
        return self.dequeue("DOG")

    def dequeue(self, type):
        if self.isEmpty():
            return None

        tmp = deque()
        while len(self.data) != 0 and self.data[0].type != type:
            tmp.append(self.data.popleft())

        adoptedAnimal = None
        if len(self.data) != 0:
            adoptedAnimal = self.data.popleft()

        while len(tmp) != 0:
            self.data.appendleft(tmp.pop())

        return adoptedAnimal

    def display(self):
        print("\n")
        for i in range(len(self.data)):
            print(self.data[i], self.data[i].type)

    def isEmpty(self):
        return len(self.data) == 0


# To decrease time complexity of dequeueCat and dequeueDog to O(1)
# We could store each type in different queues, when calling dequeueAny to pop the oldest
class EfficientAnimalShelter:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()

    def enqueue(self, animal):
        if animal.type == "CAT":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueAny(self):
        if len(self.dogs == 0) and len(self.cats) == 0:
            return None
        elif len(self.dogs) == 0 and len(self.cats) != 0:
            return self.dequeueCat()
        elif len(self.dogs) != 0 and len(self.cats) == 0:
            return self.dequeueDog()

        firstDog = self.dogs[0]
        firstCat = self.cats[0]

        if firstDog.createdAt < firstCat.createdAt:
            return self.dogs.popleft()
        else:
            return self.cats.popleft()

    def dequeueCat(self):
        if len(self.cats) == 0:
            return None

        return self.cats.popleft()

    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None

        return self.dogs.popleft()
