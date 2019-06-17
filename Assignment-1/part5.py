class TowerOfHanoi:
    def __init__(self, n):
        self.first_rod = [index for index in range(n, 0, -1)]
        self.second_rod = []
        self.third_rod = []
        self.n = n
        self.number_of_rods = 3

    def move_disks(self):
        self.move_disk_recursive(self.n, self.first_rod, self.second_rod, self.third_rod)

    def move_disk_recursive(self, n, first, second, third):
        if n >= 1:
            self.move_disk_recursive(n-1, first, third, second)

            self.move_disk(first, third)

            self.move_disk_recursive(n-1, second, first, third)

    def move_disk(self, starting_rod, destination_rod):
        destination_rod.append(starting_rod.pop())

    def number_of_rods(self):
        return self.number_of_rods

    def disks_at_rod(self, index):
        if index >= 0 and index < self.number_of_rods():
            if index is 0:
                return len(self.first_rod)
            elif index is 1:
                return len(self.second_rod)
            elif index is 2:
                return len(self.third_rod)
        else:
            return 0


hanoi = TowerOfHanoi(6)
print("Before Move.")
print(hanoi.first_rod)
print(hanoi.second_rod)
print(hanoi.third_rod)

hanoi.move_disks()

print("After Move.")
print(hanoi.first_rod)
print(hanoi.second_rod)
print(hanoi.third_rod)