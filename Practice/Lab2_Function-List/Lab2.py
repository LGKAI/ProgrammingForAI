def ex1(names, heights):
    n = len(heights)
    for i in range(n):
        for j in range(0, n - i - 1):
            if heights[j] > heights[j + 1]:
                heights[j], heights[j + 1] = heights[j + 1], heights[j]
                names[j], names[j + 1] = names[j + 1], names[j]
    return names

def ex2(lst):
    dic = {}
    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return max(dic, key = dic.get)

def ex3(a):
    n = len(a)
    total = n * (n + 1) // 2
    miss = total - sum(a)
    return miss

def ex4(a, k):
    a.sort(reverse = True)
    return a[k - 1]

def ex5(a):
    num = 0
    for i in range(len(a)):
        num = num * 10 + a[i]
    num += 1
    result = []
    while num > 0:
        result.insert(0, num % 10)
        num //= 10
    return result

def ex6(a, b):
    result = a + b
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

def ex7(nums):
    nums_str = [str(num) for num in nums]
    def compare(x, y):
        if x + y > y + x:
            return True
        else:
            return False
    n = len(nums_str)
    for i in range(n):
        for j in range(0, n - i - 1):
            if not compare(nums_str[j], nums_str[j + 1]):
                nums_str[j], nums_str[j + 1] = nums_str[j + 1], nums_str[j]
    result = ''.join(nums_str)
    return '0' if result[0] == '0' else result

def ex8(matrix):
    for i in range(len(matrix)):
        matrix[i] = [1 - pixel for pixel in matrix[i][::-1]]
    return matrix

def ex9(a):
    a.sort()
    triplets = []
    for i in range(len(a) - 2):
        if i > 0 and a[i] == a[i - 1]:
            continue
        left, right = i + 1, len(a) - 1
        while left < right:
            total = a[i] + a[left] + a[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triplets.append([a[i], a[left], a[right]])
                while left < right and a[left] == a[left + 1]:
                    left += 1
                while left < right and a[right] == a[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return triplets

def ex10(a, k):
    a.sort()
    result = []
    for i in range(len(a) - 1):
        next = i + 1
        while next < len(a):
            sum = a[i] + a[next]
            if sum < k:
                next += 1
            elif sum == k:
                result.append([a[i], a[next]])
                next += 1
            else:
                break
    return result

def ex11(a, k):
    from collections import Counter
    count = Counter(a)
    for num in list(count.keys()):
        complement = k - num
        if num == complement:
            if count[num] % 2 != 0:
                return False
        else:
            if count[num] > count[complement]:
                return False
            count[complement] -= count[num]
            count[num] = 0
    return True


if __name__ == "__main__":
    pass