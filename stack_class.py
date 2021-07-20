

class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) < 1:
            return True
        else:
            return False

    def push(self, add_element):
        self.stack.append(add_element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def size_stack(self):
        return len(self.stack)

    def valid_parentheses(self, string):
        if len(string) > 0:
            for simvol in string:
                if simvol == '(' or ')' or '[' or ']' or '{' or '}':
                    self.push(simvol)
                    if self.stack.count(')') > self.stack.count('(') or \
                            self.stack.count(']') > self.stack.count('[') or \
                            self.stack.count('}') > self.stack.count('{'):
                        del self.stack[0:]
                        return "Несбалансированно"
            if self.stack.count('(') != self.stack.count(')') or \
                    self.stack.count('[') != self.stack.count(']') or \
                    self.stack.count('{') != self.stack.count('}'):
                del self.stack[0:]
                return "Несбалансированно"
            else:
                del self.stack[0:]
                return "Сбалансированно"
        else:
            del self.stack[0:]
            return "Пустая строка"


if __name__ == '__main__':
    stack = Stack()
    print(stack.valid_parentheses('(((([{}]))))'))
    print(stack.valid_parentheses('[([])((([[[]]])))]{()}'))
    print(stack.valid_parentheses('{{[()]}}'))
    print(stack.valid_parentheses('}{}'))
    print(stack.valid_parentheses('{{[(])]}}'))
    print(stack.valid_parentheses('[[{())}]'))
