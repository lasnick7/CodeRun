def is_median(arr, x, n):
        count_less = 0
        count_greater = 0
        count_equals = 0
        
        for i in range(n):
            if arr[i] < x:
                count_less += 1
            elif arr[i] > x:
                count_greater += 1
            else:
                count_equals += 1
                
        if count_less == count_greater:
            return [True, "equal"]
        elif count_less + count_equals == count_greater:
            return [False, "greater"]
        elif count_less == count_equals + count_greater:
            return [False, "less"]
        elif count_less < count_equals + count_greater and count_less + count_equals > count_greater:
            return [True, "equal"]
        elif count_less < count_equals + count_greater and count_less + count_equals < count_greater:
            return [False, "greater"]
        elif count_less > count_equals + count_greater and count_less + count_equals > count_greater:
            return [False, "less"]

    def find_median(arr, n):
        start = min(arr)
        end = max(arr) + 1
        while start + 1 != end:
            mid = (start + end) // 2
            response = is_median(arr, mid, n)
            if response[0]:
                return mid
            if response[1] == 'less':
                end = mid
            else:
                start = mid
        return start

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

    generator = RandomGenerator(a, b, 0)
    houses = [generator.next_rand_32() for _ in range(n)] 
        
    print(find_sum(houses, find_median(houses, n), n))
