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

    def run(self):
        while self.program_counter < len(self.program):
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


lines = open('input.txt').read().splitlines()

vm = VM()
vm.load_program(lines)
vm.run()
print(vm.registers[0])
