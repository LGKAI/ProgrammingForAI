def is_happy(n):
    lst = []
    while n != 1 and n not in lst:
        lst.append(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

def shift_step(a, step):
    a = a[-step:] + a[:-step]
    return a

def find_most_score(a):
    scores = []
    count = []
    for score in a:
        if score in scores:
            index = scores.index(score)
            count[index] += 1
        else:
            scores.append(score)
            count.append(1)
    most_count = max(count)
    most_score = [scores[i] for i in range(len(count)) if count[i] == most_count]
    return most_score

def find_max_50p_consecutive_scores(a):
    max_count = 0
    cur_count = 0
    last_lst = []
    cur_lst = []

    for score in a:
        if score >= 50:
            cur_count += 1
            cur_lst.append(score)
        else:
            if cur_count >= max_count:
                max_count = cur_count
                last_lst = cur_lst.copy()
            cur_count = 0
            cur_lst = []

    if cur_count >= max_count:
        max_count = cur_count
        last_lst = cur_lst

    return max_count, last_lst

def main_diagonal(matrix):
    for i in range(len(matrix)):
        print(matrix[i][i], end = " ")
    print("\n")

def anti_diagonal(matrix):
    for i in range(len(matrix)):
        print(matrix[i][-(i + 1)], end = " ")
    print("\n")

def lower_triangular(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1):
            print(matrix[i][j], end = " ")
        print()
    print()

def upper_triangular(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            print(" ", end = "")
        for k in range(i, len(matrix)):
            print(matrix[i][k], end = " ")
        print()
    print()

def transpose(matrix):
    matrixT = []
    for i in range(len(matrix)):
        matrixT.append([row[i] for row in matrix])
    return matrixT

def mid_row(matrix):
    l = len(matrix)
    row = matrix[(l - 1) // 2]
    print(" ".join(map(str, row)))

def mid_column(matrix):
    column = []
    for row in matrix:
        h = len(row)
        column.append(row[(h - 1) // 2])
    print(" ".join(map(str, column)))

def find_repeated_elements(t):
    element_count = {}
    
    for element in t:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    
    repeated_elements = []
    
    for element, count in element_count.items():
        if count > 1:
            repeated_elements.append(element)
    
    return repeated_elements

def find_second_max(t):
    unique_elements = set(t)
    sorted_elements = sorted(unique_elements, reverse = True)
    if len(sorted_elements) < 2:
        raise ValueError("Cook!!!")
    return sorted_elements[1]

def count_primes(t):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
            return True
    count = 0
    for i in t:
        if is_prime(i):
            count += 1
    return count

def add_element_to_tuple(t: tuple, n: int, p: int) -> tuple:
    temp_list = list(t)
    temp_list.insert(p, n)
    modified_tuple = tuple(temp_list)
    return modified_tuple

def remove_empty_tuple(l: list) -> list:
    return [t for t in l if t]

def remove_intersection(s1, s2):
    s = s1
    s1 = s1.difference(s2)
    s2 = s2.difference(s)
    print(s1)
    print(s2)

def all_subsets(input_set):
    subsets = [[]]
    for element in input_set:
        new_subsets = []
        for subset in subsets:
            new_subset = subset + [element]
            new_subsets.append(new_subset)
        subsets.extend(new_subsets)
    return [set(subset) for subset in subsets if subset]

def symmetric_difference(a, b):
    return a ^ b

def find_max_votes(candidates):
    vote_count = {}
    for candidate in candidates:
        if candidate in vote_count:
            vote_count[candidate] += 1
        else:
            vote_count[candidate] = 1
    max_votes = max(vote_count.values())
    max_candidates = [candidate for candidate, votes in vote_count.items() if votes == max_votes]
    return min(max_candidates)

def days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return "Invalid month"
    
def sort_via_keys(dic):
    return {key: dic[key] for key in sorted(dic)}

def sort_via_values(dic):
    return {key: value for key, value in sorted(dic.items(), key = lambda item: item[1])}


if __name__ == '__main__':
    matrix = [
        [2, 3, 1, 5, 0],
        [7, 1, 5, 3, 1],
        [2, 5, 7, 8, 1],
        [0, 1, 5, 0, 1],
        [3, 4, 9, 1, 5]
    ]
    main_diagonal(matrix)
    anti_diagonal(matrix)
    lower_triangular(matrix)
    upper_triangular(matrix)
