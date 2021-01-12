with open('data.txt') as f:
    data = [x for x in f.read().split('\n') if x != '']


def scan(source):
    return (f'({source})').replace('(', ' ( ').replace(')', ' ) ').split()


def parse_one(ts, i=0):
    parsed = []

    while i < len(ts):
        c = ts[i]
        if c == '(':
            sub, i = parse_one(ts, i + 1)
            parsed.append(sub)
        elif c == ')':
            return parsed, i
        elif c.isdigit():
            parsed.append(int(c))
        elif c in ('+', '*'):
            parsed.append(c)
        else:
            raise Exception('Invalid Token')
        i += 1
    return parsed[0]


def eval_one(expr, direction='left'):
    if isinstance(expr, int):
        return expr
    left = eval_one(expr[0])
    op = env[expr[1]]
    right = eval_one(expr[2])
    if expr[3:] == []:
        return op(left, right)
    else:
        return eval_one([op(left, right), *expr[3:]])


class Parser:
    def __init__(self, ts):
        # ts are semi-parsed here
        self.ts = ts
        self.i = 0

    def advance(self):
        self.i += 1
        return self.ts[self.i-1]

    def peek(self):
        return self.ts[self.i]

    def not_at_end(self):
        return self.i != len(self.ts)

    def parse(self):
        return self.factor()

    def factor(self):
        left = self.term()
        while self.not_at_end() and self.peek() == '*':
            op = self.advance()
            right = self.term()
            left = [left, op, right]
        return left

    def term(self):
        left = self.primary()
        while self.not_at_end() and self.peek() == '+':
            op = self.advance()
            right = self.primary()
            left = [left, op, right]
        return left

    def primary(self):
        t = self.advance()
        if isinstance(t, list):
            return Parser(t).parse()
        else:
            return t


def parse_two(expr):
    return Parser(parse_one(expr)).parse()


def eval_two(ast):
    if isinstance(ast, int):
        return ast
    left, op, right = ast
    return env[op](eval_two(left), eval_two(right))


env = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y
}

print('One:', sum(eval_one(parse_one(scan(e))) for e in data))
print('Two:', sum(eval_two(parse_two(scan(e))) for e in data))
