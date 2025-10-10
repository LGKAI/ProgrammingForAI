def count_str():
    s = input()
    chars = 0
    digits = 0
    symbols = 0
    for i in s:
        if i.isalpha():
            chars += 1
        elif i.isdigit():
            digits += 1
        else:
            symbols += 1
    print(f"Chars = {chars}")
    print(f"Digits = {digits}")
    print(f"Symbols = {symbols}")

def append_mid(s1: str, s2: str) -> str:
    return s1[:len(s1)//2] + s2 + s1[len(s1)//2:]

def arrange_str(s):
    lst = list(s)
    low = []
    up = []
    for i in lst:
        if i.islower():
            low.append(i)
        else:
            up.append(i)
    return "".join(low + up)

def remove_chars(s):
    digits = []
    for i in s:
        if i.isdigit(): digits.append(i)
    return ''.join(digits)

def remove_empty(lst):
    for i in lst:
        if not i:
            lst.remove(i)
    return lst

def split_str(s):
    result = s.split('-')
    for i in result:
        print(i)

def convert_hex(hex):
    is_valid = True
    dec = 0
    for i in hex:
        if i in '0123456789abcdefABCDEF':
            dec = dec * 16 + int(i, 16)
        else:
            is_valid = False
            break
    if is_valid:
        print(dec)
    else:
        print("Cook!!!")

def count_words(s):
    words = s.lower().split()
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else: count[word] = 1
    return count

def meaningful_int(s):
    result = []
    for i in s:
        if i.isdigit():
            result.append(i)
    result = ''.join(result)
    result = result.replace('0', '')
    return result

def set_email_list(input_file, output_file):
    emails = []

    with open(input_file, 'r', encoding = 'utf-8') as file:
        sv_list = file.readlines()

    result = []

    for sv in sv_list:
        name_parts = sv.strip().split()
        name_tat = name_parts[0][0].lower() + name_parts[-1].lower()

        count = 1
        email = f"{name_tat}@fit.hcmus.edu.vn"
        while email in emails:
            count += 1
            email = f"{name_tat}{count}@fit.hcmus.edu.vn"

        emails.append(email)
        result.append(f"{sv.strip()} - {email}")

    with open(output_file, 'w', encoding = 'utf-8') as file:
        for line in result:
            file.write(line + '\n')

def merge_files(input_directory, output_file):
    from pathlib import Path

    unique_words = set()

    for file_path in Path(input_directory).iterdir():
        if file_path.is_file() and file_path.suffix == '.txt':
            with file_path.open('r', encoding = 'utf-8') as file:
                for line in file:
                    unique_words.add(line.strip())

    with open(output_file, 'w', encoding = 'utf-8') as output:
        for word in sorted(unique_words):
            output.write(word + '\n')


if __name__ == "__main__":
    input_file = "D:\LGKAI\CSLTAI\Session04_String-TextFile\input.txt"
    output_file = "D:\LGKAI\CSLTAI\Session04_String-TextFile\out1a.txt"
    # Do VSCode đang open folder IT-AI nên phải dùng đường dẫn tuyệt đối file
    # Nếu mún chỉ dùng tên file thì phải open folder chứa file là Session04
    set_email_list(input_file, output_file)
