import exception

pointer = 0
depth = 0


def func(x):
    if x[0] == "%" and len(x) > 1:
        return int(x[1:])
    else:
        return ord(x[0])


def func2(x):
    if x[0] == "%":
        return int(x[1:])
    elif 48 <= ord(x[0]) <= 57:
        return int(x)
    else:
        raise exception.UnknownPrefix


with open("input.btf", "r") as f:
    all_text = f.readlines()


with open("result.txt", "w") as f:
    for line in all_text:
        if line == "":
            continue
        if line[0] == "#":
            continue
        code = line.split()
        command = code[0]
        if command == "select":  # select
            if code[1][0] == "+":
                target = int(code[1][1:])
                f.write(">>" * target + "\n")
                pointer += target
            elif code[1][0] == "-":
                target = int(code[1][1:])
                f.write("<<" * target + "\n")
                pointer -= target
            else:
                target = int(code[1][1:]) if code[1][0] == "$" else int(code[1])
                if target > pointer:
                    f.write(">>" * (target - pointer) + "\n")
                elif target < pointer:
                    f.write("<<" * (pointer - target) + "\n")
                pointer = target
        elif command == "set":  # set
            if code[1][0] == "$":
                target = int(code[1][1:])
                f.write("[-] ")
                if target > pointer:
                    number = target - pointer
                    f.write(">>" * number + " ")
                    f.write("[" + "<<" * number + "+" + ">>" * number + ">+<-" + "]" + " ")
                    f.write(">[<+>-] ")
                    f.write("<<" * number + "\n")
                elif target < pointer:
                    number = pointer - target
                    f.write("<<" * number + " ")
                    f.write("[" + ">>" * number + "+" + "<<" * number + ">+<-" + "]" + " ")
                    f.write(">[<+>-] ")
                    f.write(">" * number + "\n")
            else:
                target = func(code[1])
                f.write("[-] " + "+" * target + "\n")
        elif command == "add":  # add
            if code[1][0] == "$":
                target = int(code[1][1:])
                if target > pointer:
                    number = target - pointer
                    f.write(">>" * number + " ")
                    f.write("[" + "<<" * number + "+" + ">>" * number + ">+<-" + "]" + " ")
                    f.write(">[<+>-] ")
                    f.write("<<" * number + "\n")
                elif target < pointer:
                    number = pointer - target
                    f.write("<<" * number + " ")
                    f.write("[" + ">>" * number + "+" + "<<" * number + ">+<-" + "]" + " ")
                    f.write(">[<+>-] ")
                    f.write(">" * number + "\n")
            else:
                target = func2(code[1])
                f.write("+" * target + "\n")
        elif command == "sub":  # sub
            if code[1][0] == "$":
                target = int(code[1][1:])
                if target > pointer:
                    number = target - pointer
                    f.write(">>" * number + " ")
                    f.write("[" + "<<" * number + "-" + ">>" * number + ">+<-" + "]" + " ")
                    f.write(">[<+>-] ")
                    f.write("<<" * number + "\n")
                elif target < pointer:
                    number = pointer - target
                    f.write("<<" * number + " ")
                    f.write("[" + ">>" * number + "-" + "<<" * number + ">+<-" + "]" + " ")
                    f.write(">[<+>-] ")
                    f.write(">>" * number + "\n")
            else:
                target = func2(code[1])
                f.write("-" * target + "\n")
        elif command == "while":  # while
            depth += 1
            f.write("[\n")
        elif command == "end":  # end
            depth -= 1
            if depth < 0:
                raise exception.NotMatchedWhile
            f.write("]\n")
        elif command == "input":  # input
            f.write(",\n")
        elif command == "output":  # output
            if len(code) == 1:
                f.write(".\n")
            else:
                target = func(code[1])
                f.write("> [-] " + "+" * target + " . [-] <\n")
        elif command == "exit":
            break
        else:
            raise exception.UnknownCommand

if depth:
    raise exception.NotMatchedWhile

print("Convert done, the code is in 'result.txt'.")
