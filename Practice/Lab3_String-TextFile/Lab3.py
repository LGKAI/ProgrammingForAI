def ex1(name):
    with open(name, "r", encoding = "utf-8") as file:
        print(file.read())

def ex2(name, n):
    with open(name, "r", encoding = "utf-8") as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines if line.strip() != ""]
    for i in range(n):
        print(lines[i])

def ex3(name):
    with open(name, "r", encoding = "utf-8") as f:
        last_line = f.readlines()[-1]
    print(last_line)

def ex4(name):
    with open(name, "r", encoding = "utf-8") as f:
        lines = f.readlines()
    longest = lines[0]
    for i in lines:
        if len(i) > len(longest):
            longest = i
    print(longest)

def ex5(name):
    with open(name, "r", encoding = "utf-8") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines if line.strip() != ""]
    shortest = lines[0]
    for i in lines:
        if len(i) < len(shortest):
            shortest = i
    print(shortest)

def ex6(name):
    with open(name, "r", encoding = "utf-8") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines if line.strip() != ""]
    print(len(lines))

def ex7(name):
    with open(name, "r", encoding = "utf-8") as f:
        text = f.read()
    words = text.lower().split()
    words = [word.strip(',;.!:()"') for word in words]
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

def ex8(name):
    count = ex7(name)
    max_count = max(count.values())
    most_word = [word for word in count.keys() if count[word] == max_count]
    return most_word

def ex9(name):
    count = ex7(name)
    min_count = min(count.values())
    least_word = [word for word in count.keys() if count[word] == min_count]
    return least_word

def ex10(name, k):
    with open(name, "r", encoding = "utf-8") as f:
        text = f.read()
    words = text.lower().split()
    words = [word.strip(',;.!:()"') for word in words]
    count = 0
    for word in words:
        if word[-1] == k:
            count += 1
    return count

def ex11(name):
    with open(name, "r", encoding = "utf-8") as f:
        text = f.read()
    words = text.lower().split()
    words = [word.strip(',;.!:()"') for word in words]
    letters = "".join(map(str, words))
    count = {}
    for letter in letters:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count

def ex12(name, n, k):
    count = ex7(name)
    result = []
    for word in count.keys():
        if n <= count[word] <= k:
            result.append(word)
    return result

def ex13(name, n, k, out_file = "output.txt"):
    with open(name, "r", encoding = "utf-8") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines if line.strip() != ""]
    out_lines = lines[n - 1 : k]

    with open(out_file, "w", encoding = "utf-8") as out_f:
        for line in out_lines:
            out_f.write(line + "\n")

def ex14(name, k):
    with open(name, "r", encoding = "utf-8") as f:
        contents = f.read()
    words = contents.lower().split()
    words = [word.strip(',;.:()"') for word in words]
    lst = []
    count = []
    for i in range(len(words)):
        if words[i - 1] == k and words[i] in lst:
            index = lst.index(words[i])
            count[index] += 1
        elif words[i - 1] == k and words[i] not in lst:
            lst.append(words[i])
            count.append(1)
    max_count = max(count)
    most_word = [lst[i] for i in range(len(count)) if count[i] == max_count]
    return most_word

def ex15(name, k):
    k = k.lower()
    with open(name, "r", encoding = "utf-8") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines if line.strip() != ""]
    result = []
    for line in lines:
        if k in line.lower():
            result.append(line)
    if not result:
        print(None)
    else:
        print("\n".join(result))

def ex16(name, h, k):
    with open(name, "r", encoding = "utf-8") as f:
        text = f.read()
    new_text = text.replace(h, k)
    print(new_text)

def ex17(name, n, k):
    with open(name, "r", encoding = "utf-8") as f:
        lines = [line.strip() for line in f if line.strip() != ""]
        lines.insert(n - 1, k)
        print("\n".join(lines))

def ex18(name, n):
    with open (name, "r", encoding = "utf-8") as f:
        lines = [line.strip() for line in f if line.strip() != ""]
        lines.pop(n - 1)
        print("\n".join(lines))

def ex19(array, out_file = "output2.txt"):
    with open(out_file, 'w') as f:
        for element in array:
            f.write(f"{element}\n")

def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]

    def words(num):
        if num == 0:
            return "zero"
        elif num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + ('' if num % 10 == 0 else ' ' + ones[num % 10])
        elif num < 1000:
            return ones[num // 100] + " hundred" + ('' if num % 100 == 0 else ' ' + words(num % 100))
        else:
            for i, word in enumerate(thousands):
                if num < 1000 ** (i + 1):
                    return words(num // 1000 ** i) + ' ' + word + ('' if num % 1000 ** i == 0 else ' ' + words(num % 1000 ** i))

    return words(n)

def ex20(name, out_file = "output3.txt"):
    with open(name, 'r') as file:
        content = file.read()
    words = content.split()
    converted_words = []
    for word in words:
        if word.isdigit():
            word = number_to_words(int(word))
        converted_words.append(word)
    converted_content = ' '.join(converted_words)

    with open(out_file, 'w') as file:
        file.write(converted_content)


if __name__ == "__main__":
    pass