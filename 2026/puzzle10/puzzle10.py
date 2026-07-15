#!/usr/bin/python3
import re

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
        # TODO a cleaner version of this
        if line[0:2] == "ba":
            ins = 0
            pos = 2
            while line[pos] == "n" and line[pos+1] == "a":
                ins += 1
                pos += 2

            args = []
            while pos < len(line):
                pos += 2
                arg = 0
                while pos < len(line) and line[pos] == "n" and line[pos+1] == "a":
                    arg += 1
                    pos += 2
                    if pos >= len(line):
                        break
                args.append(arg)

            return Instruction(ins, args)

        elif line[0:2] == "be":
            return Label((len(line) - 2) / 2)

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
