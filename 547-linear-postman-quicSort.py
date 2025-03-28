def q_sort(arr):
    if len(arr) <= 1:
        return arr
    left = []
    center = []
    right = []
    pivot = arr[0]
    for i in range(len(arr)):
        if arr[i] > pivot:
            right.append(arr[i])
        elif arr[i] == pivot:
            center.append(arr[i])
        elif arr[i] < pivot:
            left.append(arr[i])
    return q_sort(left) + center + q_sort(right)

def find_median_in_sorted(arr, n):
    if n % 2 == 0:
        return (arr[n // 2] + arr[n // 2 - 1]) // 2
    else:
        return arr[n // 2]
def find_sum(arr, x, n):
    sum = 0
    for i in range(n):
        sum += abs(arr[i] - x)
    return sum

n = int(input())
a, b = [int(x) for x in input().split()]

class RandomGenerator:
    def __init__(self, a, b, cur):
        self.a = a
        self.b = b
        self.cur = cur
        
    def next_rand_24(self):
        self.cur = (self.cur * self.a + self.b) & 0xFFFFFFFF
        return self.cur >> 8
    
    def next_rand_32(self):
        a = self.next_rand_24()
        b = self.next_rand_24()
        return (a << 8) ^ b 

generator = RandomGenerator(a, b, cur=0)
houses = [0] * n

for i in range(n):
    houses[i] = generator.next_rand_32()
    
print(find_sum(houses, find_median_in_sorted(q_sort(houses), n), n))
