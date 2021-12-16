import sys

buf = bytes.fromhex(input())
bits = ""
for b in buf:
    bits += format(b, "08b")


def parse_packet(bitstr):
    state = "version"
    i = 0
    v = 0
    ii = ""
    t = 0
    while i < len(bitstr):
        if state == "version":
            v = int(bitstr[i : i + 3], 2)
            i += 3
            state = "type"
            continue
        if state == "type":
            t = int(bitstr[i : i + 3], 2)
            i += 3
            if t == 4:
                state = "integer"
            else:
                state = "op"
            continue
        if state == "integer":
            done = bitstr[i] == "0"
            i += 1
            ii += bitstr[i : i + 4]
            i += 4
            if done:
                return ((v, t, int(ii, 2)), i)
            continue
        if state == "op":
            lt = bitstr[i]
            i += 1
            packets = []
            if lt == "0":
                l = int(bitstr[i : i + 15], 2)
                i += 15
                end = i + l
                while i < end:
                    ps, r = parse_packet(bitstr[i:end])
                    i += r
                    packets.append(ps)
            elif lt == "1":
                ps = int(bitstr[i : i + 11], 2)
                i += 11
                for p in range(ps):
                    pac, r = parse_packet(bitstr[i:])
                    i += r
                    packets.append(pac)
            return ((v, t, packets), i)
    return None, i


def sum_versions(packet):
    v, t, val = packet
    if type(val) == list:
        for p in val:
            v += sum_versions(p)
    return v


def exec(packet):
    v, t, val = packet
    if t == 0:
        sum = 0
        for p in val:
            sum += exec(p)
        return sum
    elif t == 1:
        product = 1
        for p in val:
            product *= exec(p)
        return product
    elif t == 2:
        n = sys.maxsize
        for p in val:
            e = exec(p)
            if e < n:
                n = e
        return n
    elif t == 3:
        n = -sys.maxsize + 1
        for p in val:
            e = exec(p)
            if e > n:
                n = e
        return n
    elif t == 4:
        return val
    elif t == 5:
        p1, p2 = val
        e1 = exec(p1)
        e2 = exec(p2)
        if e1 > e2:
            return 1
        else:
            return 0
    elif t == 6:
        p1, p2 = val
        e1 = exec(p1)
        e2 = exec(p2)
        if e1 < e2:
            return 1
        else:
            return 0
    elif t == 7:
        p1, p2 = val
        e1 = exec(p1)
        e2 = exec(p2)
        if e1 == e2:
            return 1
        else:
            return 0


packets, read = parse_packet(bits)
print(sum_versions(packets))
print(exec(packets))
