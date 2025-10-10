def ex1(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result

def ex2(a):
    result = []
    for row in a:
        result.append(sum(row))
    return result

def ex3(d: dict) -> dict:
    return {value: key for key, value in d.items()}

def ex4(a, b):
    return a.intersection(b)

def ex5(a, b):
    return a.symmetric_difference(b)

def ex6(a):
    result = {}
    for i in a:
        word = "".join(sorted(i))
        if word not in result:
            result[word] = []
        result[word].append(i)
    return list(result.values())

def ex7(d1, d2):
    merged = d1.copy()
    for key, value in d2.items():
        if key in merged:
            if isinstance(merged[key], dict):
                merged[key] = ex7(merged[key], value)
            else:
                merged[key] = value
        else:
            merged[key] = value
    return merged

def ex8(a):
    result = {}
    for row in a:
        for i in row:
            if i not in result:
                result[i] = 0
            result[i] += 1
    most = max(result.values())
    most_lst = [i for i in result.keys() if result[i] == most]
    return result, most_lst

def ex9(a, b):
    return a.difference(b)

def ex10(a):
    result = set()
    for i in range(1, len(a) - 1):
        for j in a[i]:
            if j in a[i] and j in a[i - 1] and j in a[i + 1]:
                result.add(j)
    return result

def ex11(words, order):
    order_list = list(order)

    def compare(word1, word2):
        min_length = min(len(word1), len(word2))
        for i in range(min_length):
            if word1[i] != word2[i]:
                return order_list.index(word1[i]) < order_list.index(word2[i])
        return len(word1) <= len(word2)

    for i in range(len(words) - 1):
        if not compare(words[i], words[i + 1]):
            return False

    return True


if __name__ == "__main__":
    pass