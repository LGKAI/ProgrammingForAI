def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def equation1(n):
    res = 0
    tu = 0
    mau = 0
    for i in range(1, n + 1):
        tu += i
        mau = factorial(i)
        res += (tu / mau)
    return round(res, 2)

def equation2(n):
    res = 0
    tu = 0
    mau = 0
    for i in range(1, n + 1):
        tu += i
        mau = factorial(n - i + 1)
        res += (tu / mau)
    return round(res, 2)

def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

def average_primes(a, b): # a < b
    total = 0
    count = 0
    for i in range(a, b + 1):
        if is_prime(i):
            total += i
            count += 1
    return round(total/count, 2)

def is_perfect(n):
    sum = 1
    for i in range(2, n):
        if n % i == 0: sum += i
    if sum == n: return True
    else: return False

def is_squared(n):
    sqrt_n = int(n ** 0.5)
    return sqrt_n ** 2 == n

def display_squareds(n):
    for i in range(4, n + 1):
        if is_squared(i):
            print(i, end = " ")

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return a * b // find_gcd(a, b)

def count_digits(n):
    count = 0
    while n:
        count += 1
        n //= 10
    return count

def check_ascending(n):
    while n:
        min = n % 10
        n //= 10
        if min < n % 10: return False
    return True

def find_max_digit(n):
    max = n % 10
    while n:
        n //= 10
        if n % 10 > max:
            max = n % 10
    return max

def reverse_num(n):
    res = 0
    while n:
        res = (res * 10) + (n % 10)
        n //= 10
    return res

def reverse_pattern(n):
    while n:
        for i in range(n, 0, -1):
            print(i, end = ' ')
        print()
        n -= 1

def display_fibonacci(k):
    a, b = 0, 1
    count = 0
    while count < k:
        print(a, end = " ")
        a, b = b, a + b
        count += 1

def equation3(n):
    res = 0
    for i in range(n - 1, 0, -2):
        res = (res + i / (i + 1)) ** 0.5
    return round(res, 2)

def delete_digits(n):
    str_n = str(n)
    big = 0
    for i in set(str_n):
        removed_n = str_n.replace(i, '')
        if not removed_n: return big
        removed_n = int(removed_n)
        big = max(removed_n, big)
    return big

def next_prime(k):
    while True:
        k += 1
        if is_prime(k): return k

def find_min_num():
    a = list(map(int, input().split()))
    min = a[0]
    for i in a:
        if i < min: min = i
    print(min)

def count_primes():
    a = list(map(int, input().split()))
    count = 0
    for i in a:
        if is_prime(i): count += 1
    return count

def interchange_sort(a):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[j] < a[i]:
                a[j], a[i] = a[i], a[j]
    return a

def check_symmetrical(a):
    return a == a[::-1]

def simplify_fraction(a, b): # a là tử, b là mẫu khác 0
    gcd = find_gcd(a, b)
    tu = a // gcd
    mau = b // gcd
    return f"{tu}/{mau}"


if __name__ == '__main__':
    print(simplify_fraction(-6, 24))