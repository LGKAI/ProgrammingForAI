def ex1(n):
    sum = 0
    for i in range(4, n):
        if i % 4 == 0 and i % 5 != 0:
            sum += i
    return sum

def ex2(n):
    s = 1
    for i in range(2, n + 1):
        s += (i / i - 1)
    return s

def ex3(n):
    sum = 0
    fac = 1
    for i in range(1, n + 1):
        for j in range(2, n + 1):
            fac *= j
        sum += fac
    return sum

def ex4(n):
    count = 0
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end = " ")
            count += 1
            sum += i
    print()
    print(count)
    print(sum)

def ex5():
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, int(k ** 0.5) + 1):
            if k % i == 0:
                return False
        return True

    k = int(input())
    print(is_prime(k))

    n = int(input())
    largest = None
    for i in range(n - 1, 1, -1):
        if is_prime(i):
            largest = i
            break
    print(largest)

def ex6():
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    a, b = map(int, input().split())
    print(gcd(a, b))
    print(lcm(a, b))

def ex7():
    for i in range(1, 10):
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()

def ex8(h):
    space = h - 1
    star = 1
    for i in range(1, h + 1):
        for j in range(space):
            print(" ", end = "")
        for j in range(star):
            print("*", end = "")
        space -= 1
        star += 2
        print()

def ex9(t):
    return f"{(t * 3.6):.1f}"

def ex10(n):
    salary = 1
    total = 0
    for i in range(1, n + 1):
        total += salary
        salary *= 2
    print(total, salary)

def ex11():
    A, a, B, b = map(int, input().split())
    year = 0
    while A < B:
        A *= (1 + a/100)
        B *= (1 + b/100)
        year += 1
    print(year)

def ex12(n):
    a = 0
    b = 1
    count = 1
    while count != n:
        a, b = b, a + b
        count += 1
    return b

def ex13():
    lst = []
    while True:
        height = float(input("Enter height: "))
        if height == 0: break
        lst.append(height)
    lst.sort()
    print(f"Height of the first student on the list: {lst[0]} (m)")
    print(f"Height of the last student on the list: {lst[-1]} (m)")

def ex14():
    while True:
        print("SIMPLE CALCULATOR")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("0. Exit program\n")
        choice = int(input("Your choice: "))
        print()
        if choice == 1:
            a = int(input("Please enter the first number: "))
            b = int(input("Please enter the second number: "))
            print("Result:", a, "+", b, "=", a + b)
        elif choice == 2:
            a = int(input("Please enter the first number: "))
            b = int(input("Please enter the second number: "))
            print("Result:", a, "-", b, "=", a - b)
        elif choice == 3:
            a = int(input("Please enter the first number: "))
            b = int(input("Please enter the second number: "))
            print("Result:", a, "*", b, "=", a * b)
        elif choice == 4:
            a = int(input("Please enter the first number: "))
            b = int(input("Please enter the second number: "))
            print("Result:", a, "/", b, "=", a / b)
        else:
            print("You have exited the program!")
            break
        print("----------------------------------------")

def ex15():
    import time
    minute = int(input("Enter minutes: "))
    second = int(input("Enter seconds: "))
    while minute + second > 0:
        print("0" if minute < 10 else "", minute, ":", "0" if second < 10 else "", second,
              " Tick tock" if minute == 0 and second <= 5 else "", sep = "")
        time.sleep(1)
        if second == 0:
            second = 59
            minute -= 1
        else:
            second -= 1
    print("00:00 Ring ring ring")

def ex16(n):
    step = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        step += 1
    return step

def ex17(n):
    m = 0
    even = 0
    odd = 0
    while n:
        m = (m * 10) + (n % 10)
        if (n % 10) % 2 == 0:
            even += 1
        else: odd += 1
        n //= 10
    print(m)
    print(f"{even} even number(s)")
    print(f"{odd} odd number(s)")

def ex18(hours, minutes, seconds):
    if 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60:
        return True
    else: return False

def ex19():
    m = float(input("Enter Math's score: "))
    p = float(input("Enter Physics's score: "))
    c = float(input("Enter Chemistry's score: "))
    if m + p + c >= 15.0 and min(m, p, c) >= 4.0:
        print("Pass")
        if min(m, p, c) > 5.0:
            print("Consistent performance in all subjects")
        elif min(m, p, c) < 5.0:
            print("Inconsistent performance in subjects")
    else:
        print("Fail")

def ex20(n):
    return int(n ** 0.5) ** 2 == n

def ex21(n):
    if n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

def ex22():
    year = int(input())
    month = int(input())
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap year")
    else: print("Del leap year")
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("29 days")
        else:
            print("28 days")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("30 days")
    else: print("31 days")

def ex23(n):
    words = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return words[n]

def ex24():
    lst = list(map(int, input().split()))
    print(f"Largest number: {max(lst)}")
    print(f"Smallest number: {min(lst)}")
    lst.sort()
    print(" ".join(map(str, lst)))

def ex25():
    def is_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def triangle_type(a, b, c):
        if a == b == c:
            return "Equilateral"
        elif a == b or b == c or a == c:
            return "Isosceles"
        elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
            return "Right"
        else:
            return "Scalene"

    a, b, c = map(float, input().split())
    print(is_triangle(a, b, c))
    print(triangle_type(a, b, c))

def ex26():
    km = float(input())
    if km <= 1:
        vnd = km * 15
    elif km <= 5:
        vnd = 15 + (km - 1) * 13.5
    else:
        vnd = 15 + 4 * 13.5 + (km - 5) * 11
    if km > 120:
        vnd *= 0.9
    vnd *= 1000
    print(f"{vnd:.1f}")

def ex27(pre, cur):
    use = cur - pre
    if use <= 100:
        amount = use * 1000
    elif use <= 150:
        amount = 100 * 1000 + (use - 100) * 1200
    elif use <= 200:
        amount = 100 * 1000 + 50 * 1200 + (use - 150) * 2000
    else:
        amount = 100 * 1000 + 50 * 1200 + 50 * 2000 + (use - 200) * 2500
    return amount

def ex28():
    n = int(input("Enter number of km/h over the speed limit: "))
    if n <= 5:
        print("No fine")
    elif n <= 10:
        print("The amount of fine is 0.7 million")
    elif n <= 20:
        print("The amount of fine is 2.5 million")
    elif n <= 35:
        print("The amount of fine is 5.5 million")
    else:
        print("The amount of fine is 7.5 million")

def ex29(n):
    if n <= 9:
        print(n)
    else:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        print(alphabet[n - 10])

def ex30():
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[0] ** 2 + arr[1] ** 2 == arr[2] ** 2:
        print(True)
    else:
        print(False)

def ex31():
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        print("Infinite solutions")
    elif a == 0:
        if b == 0:
            print("No solution")
        else:
            print("1 solution:", "%.2f" % (-c / b))
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            print("No solution")
        elif delta == 0:
            print("1 solution:", "%.2f" % (-b / (2 * a)))
        else:
            print("2 solutions:", "%.2f" % ((-b + delta ** 0.5) / (2 * a)), "and",
                  "%.2f" % ((-b - delta ** 0.5) / (2 * a)))

def ex32():
    a = int(input("Enter operand 1: "))
    b = int(input("Enter operand 2: "))
    s = input("Enter operator: ")
    if s == "+":
        print(a, "+", b, "=", a + b)
    elif s == "-":
        print(a, "-", b, "=", a - b)
    elif s == "*":
        print(a, "*", b, "=", a * b)
    elif s == "/":
        print(a, "/", b, "=", a / b)
    else:
        print(a, "%", b, "=", a % b)

def ex33(acc_type, min_balance, end_balance):
    if end_balance < min_balance:
        if acc_type == 's':
            return "Service fee: $10"
        elif acc_type == 'c':
            return "Service fee: $25"
    else:
        if acc_type == 's':
            interest = end_balance * 0.04
            return f"Total interest earned: ${interest:.2f}"
        elif acc_type =='c':
            if end_balance - min_balance >= 5000:
                interest = end_balance * 0.03
            else:
                interest = end_balance * 0.05
            return f"Total interest earned: ${interest:.2f}"

def ex34(weight, wrist, waist, hip, forearm, gender):
    if gender == 'female':
        A1 = (weight * 0.732) + 8.987
        A2 = wrist / 3.140
        A3 = waist * 0.157
        A4 = hip * 0.249
        A5 = forearm * 0.434
        B = A1 + A2 - A3 - A4 + A5
    elif gender == 'male':
        A1 = (weight * 1.082) + 9.442
        A2 = wrist * 4.15
        B = A1 - A2
    body_fat = weight - B
    body_fat_percentage = (body_fat * 100) / weight
    return body_fat_percentage

def ex35(weight, height):
    BMI = weight / (height ** 2)
    if BMI < 18.5:
        print("Underweight")
    elif BMI <= 25:
        print("Normal")
    elif BMI <= 30:
        print("Overweight")
    elif BMI <= 40:
        print("Obese and should lose weight")
    else:
        print("Severely obese and should lose weight immediately")


if __name__ == "__main__":
    pass