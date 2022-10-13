def calc(ops):
    _ops = ops
    lst = []
    for o in ops:
        if o.isdigit():
            i = int(o)
            lst.append(i)
        else:
            if o == "C":
                lst.pop()
            elif o == "D":
                last = lst[len(lst)-1]
                lst.append(2 * last)
            elif o == "+":
                lst.append(sum(lst))

    print(lst)

if __name__ == "__main__":
    line = '5 2 C D +'
    ops = line.strip().split()
    calc(ops)
