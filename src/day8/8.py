import copy
with open('data.txt') as f:
    dat = [x.split() for x in f.read().split('\n')[:-1]]


class VM:
    def __init__(self, code, ip=0):
        self.ip = 0
        self.acc = 0
        self.code = code
        self.visited = []

    def exec_one_inst(self, debug=False):
        inst = self.code[self.ip][0]
        operand = int(self.code[self.ip][1])
        if debug:
            print(self.ip, ':', inst, ':', operand)

        self.visited.append(self.ip)

        if inst == 'nop':
            self.ip += 1
        elif inst == 'jmp':
            self.ip += operand
        elif inst == 'acc':
            self.acc += operand
            self.ip += 1
        else:
            print(inst, "Op not supported")

    def exec_till_loops_or_done(self, debug=False):
        while self.ip < len(self.code):
            if self.ip in self.visited:
                return self.acc, False
            self.exec_one_inst(debug)
        return self.acc, True


vm = VM(dat)
print("one: ", vm.exec_till_loops_or_done()[0])

for ip in vm.visited:
    if (inst := vm.code[ip][0]) in ('nop', 'jmp'):
        new_dat = copy.deepcopy(dat)
        new_dat[ip][0] = 'nop' if inst == 'jmp' else 'nop'
        temp_vm = VM(new_dat)
        acc, completed = temp_vm.exec_till_loops_or_done()
        if completed:
            print("two: ", acc)
            quit()
