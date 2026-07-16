#!/usr/bin/python3

class Instruction:
    def __init__(self, id, args):
        self.id = id
        self.args = args

class Label:
    def __init__(self, id):
        self.id = id

class VM:
    def load_program(self, lines):
        self.registers = [0] * 16
        self.program_counter = 0
        self.program = []
        self.labels = {}
        for line in lines:
            token = self.parse_line(line)
            if type(token) is Instruction:
                self.program.append(token)
            elif type(token) is Label:
                self.labels[token.id] = len(self.program)

    def parse_line(self, line):
        parts = line.split("ne")

        if parts[0][0:2] == "ba":
            ins = (len(parts[0]) - 2) // 2
            args = []
            for part in parts[1:]:
                args.append(len(part) // 2)
            return Instruction(ins, args)

        elif parts[0][0:2] == "be":
            return Label((len(parts[0]) - 2) // 2)

    def set_register(self, register, value):
        self.registers[register] = value

    def get_register(self, register):
        return self.registers[register]

    def reset(self):
        self.registers = [0] * 16
        self.program_counter = 0

    def run(self):
        instruction_count = -1
        while self.program_counter < len(self.program):
            instruction_count += 1
            if instruction_count > 5000000:
                return -1
            instruction = self.program[self.program_counter]
            match instruction.id:
                case 0:
                    self.registers[instruction.args[1]] = instruction.args[0]
                case 1:
                    self.registers[instruction.args[1]] = self.registers[instruction.args[0]]
                case 2:
                    self.registers[instruction.args[2]] = (self.registers[instruction.args[0]] + self.registers[instruction.args[1]]) % 65536
                case 3:
                    self.registers[instruction.args[2]] = (self.registers[instruction.args[0]] - self.registers[instruction.args[1]]) % 65536
                case 4:
                    self.registers[instruction.args[2]] = (self.registers[instruction.args[0]] * self.registers[instruction.args[1]]) % 65536
                case 5:
                    if self.registers[instruction.args[1]] == 0:
                        self.registers[instruction.args[2]] = 0
                    else:
                        self.registers[instruction.args[2]] = (self.registers[instruction.args[0]] % self.registers[instruction.args[1]]) % 65536
                case 6:
                    self.registers[instruction.args[0]] = (self.registers[instruction.args[0]] + 1) % 65536
                case 7:
                    self.registers[instruction.args[0]] = (self.registers[instruction.args[0]] - 1) % 65536
                case 8:
                    self.program_counter = self.labels[instruction.args[0]]
                    continue
                case 9:
                    if self.registers[instruction.args[0]] == 0:
                        self.program_counter = self.labels[instruction.args[1]]
                        continue
                case 10:
                    if self.registers[instruction.args[0]] != 0:
                        self.program_counter = self.labels[instruction.args[1]]
                        continue
                
            self.program_counter += 1

        return 0


lines = open('input.txt').read().splitlines()

vm = VM()
vm.load_program(lines)
vm.run()
part1 = vm.get_register(0)

def is_double(results):
    if len(results) // 2 == 1:
        return False

    half = len(results) // 2
    for i in range(0, half):
        if results[i] != results[i + half]:
            return False

    return True


part2 = 0
for val in range(0, 100):
    vm.reset()
    vm.set_register(0, val)
    if vm.run() == -1:
        part2 += 1


part3 = 0
for r1 in range(0, 16):
    r0 = 0

    results = []
    looping = 0

    while True:
        vm.reset()
        vm.set_register(0, r0)
        vm.set_register(1, r1)
        result = vm.run()
        val = vm.get_register(0)

        if result == -1:
            looping += 1
            results.append(-1)
        else:
            results.append(val)

        if len(results) > 10 and is_double(results):
            results = results[:len(results) // 2]
            looping //= 2

            amount = 65536 // len(results) * looping
            for i in range(0, 65536 % len(results)):
                if results[i] == -1:
                    amount += 1
            break

        r0 += 1

    part3 += amount


print(f"{part1}\n{part2}\n{part3}")
