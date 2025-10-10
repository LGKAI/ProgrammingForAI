class Stack:
    def __init__(self, limit = 1000):
        self.data = []
        self.limit = limit

    def push(self, item):
        self.data.append(item)

    def pop(self):
        del_item = self.data[-1]
        self.data.pop()
        return del_item

    def top(self):
        return self.data[-1]

    def is_full(self):
        if len(self.data) < self.limit:
            return False
        else:
            return True

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.data)
    
def sort_stack(stack):
    aux_stack = Stack()

    while not stack.is_empty():
        temp = stack.pop()
        while not aux_stack.is_empty() and aux_stack.top() > temp:
            stack.push(aux_stack.pop())
        aux_stack.push(temp)
   
    while not aux_stack.is_empty():
        stack.push(aux_stack.pop())

def add_nums(s1: Stack, s2: Stack) -> Stack:
    result = Stack()
    carry = 0

    while not s1.is_empty() or not s2.is_empty() or carry != 0:
        num1 = s1.pop() if not s1.is_empty() else 0
        num2 = s2.pop() if not s2.is_empty() else 0

        total = num1 + num2 + carry
        carry = total // 10
        result.push(total % 10)

    final_result = Stack()
    while not result.is_empty():
        final_result.push(result.pop())

    return final_result

def is_matching_pair(a, b):
    if a == '(' and b == ')': return True
    elif a == '[' and b == ']': return True
    elif a == '{' and b == '}': return True
    else: return False

def check_brackets(expression):
    stack = Stack()
    for char in expression:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty() or not is_matching_pair(stack.pop(), char):
                return False
    return stack.is_empty()


if __name__ == "__main__":
    # s1 = Stack()
    # s1.push(2)
    # s1.push(3)
    # s1.push(4)

    # s2 = Stack()
    # s2.push(5)
    # s2.push(6)
    # s2.push(7)

    # result_stack = add_nums(s1, s2)
    # while not result_stack.is_empty():
    #     print(result_stack.pop(), end = "")

    ex1 = '((a + b * {123})){}'
    ex2 = '([)]abc'
    print(check_brackets(ex1))
    print(check_brackets(ex2))
