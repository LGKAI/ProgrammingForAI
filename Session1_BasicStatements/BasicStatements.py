def abs():
    n = int(input())
    if n >= 0: print(n)
    else: print(-n)

def bigger_num():
    a, b = map(int, input().split())
    if a >= b: print(a)
    else: print(b)

def squared_num():
    n = int(input())
    if int(n ** (1/2)) ** 2 == n: print(True)
    else: print(False)

def leap_year():
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): print(True)
    else: print(False)

def days_in_month():
    year = int(input("Enter a year (> 0): "))
    month = int(input("Enter a month (1...12): "))
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("29 days")
        else: print("28 days")
    elif month == 4 or month == 6 or month == 9 or month == 11: print("30 days")
    else: print("31 days")

def ascending():
    a, b, c = map(int, input().split())
    if a < b:
        if b < c: print(a, b, c)
        else:
            if a < c: print(a, c, b)
            else: print(c, a, b)
    else:
        if a < c: print(b, a, c)
        else:
            if b < c: print(b, c, a)
            else: print(c, b, a)

def check_triangle():
    a, b, c = map(int, input().split())
    if a + b > c and a + c > b and b + c > a: print(True)
    else: print(False)

def taxi_fare():
    km = float(input('Enter a number of km (> 0): '))
    vnd = 0
    if km <= 1: vnd = km * 15
    elif km <= 5: vnd = 1 * 15 + (km - 1) * 13.5
    else: vnd = 1 * 15 + 4 * 13.5 + (km - 5) * 11
    if km > 120: vnd *= 0.9
    vnd *= 1000
    print(f'Total fare: {vnd:.3f} vnd')


if __name__ == "__main__":
    taxi_fare()