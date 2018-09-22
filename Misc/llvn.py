import operator

ops = {"add": operator.add, "sub": operator.sub, "mult": operator.mul, "and": operator.and_, "or": operator.or_, "xor": operator.xor}
def calculate_output(buf):
    d = {}
    for i in buf.split("\n"):
        if i.startswith(">show"):
            return sum(d[i] for i in i[6:].split(" + "))
        elif i.startswith(">%"):
            l, r = i[1:].split(" = ")
            if "," in r:
                op, *v = r.replace(",", "").split(" ")
                d[l] = ops[op](*[d[i] if i.startswith("%") else int(i) for i in v])
            else:
                d[l] = int(r, 16)

if __name__ == "__main__":
    import socket
    s = socket.create_connection(("misc.chal.csaw.io", 10101))

    while True:
        buf = ""
        while not buf.endswith("?: "):
            buf += s.recv(4096).decode()
            if "flag" in buf:
                print(*[i for i in buf.split("\n") if "flag" in i])
                break
        else:
            s.send(str(calculate_output(buf)).encode() + b"\n")
            continue
        break
