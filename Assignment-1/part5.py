class TowerOfHanoi:
    def __init__(self, n):
        self.first_rod = [index for index in range(n, 0, -1)]
        self.second_rod = []
        self.third_rod = []
        self.n = n

    def move_disks(self):

        self.move_disk(self.n, self.first_rod, self.second_rod, self.third_rod)

    def move_disk(self, n, first, second, third):
        if n >= 1:
            self.move_disk(n-1, first, third, second)

            disk_from_first_rod = first.pop()
            third.append(disk_from_first_rod)

            self.move_disk(n-1, second, first, third)



hanoi = TowerOfHanoi(9)
print("Before Move.")
print(hanoi.first_rod)
print(hanoi.second_rod)
print(hanoi.third_rod)

hanoi.move_disks()

print("After Move.")
print(hanoi.first_rod)
print(hanoi.second_rod)
print(hanoi.third_rod)