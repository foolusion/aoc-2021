result = 0

with open("day_08.in") as f:
    for line in f:
        digit_string, output_string = [i.strip() for i in line.split(" | ")]
        digits = [set(i) for i in digit_string.split(" ")]
        output = [set(i) for i in output_string.split(" ")]
        zero = set()
        one = set()
        two = set()
        three = set()
        four = set()
        five = set()
        six = set()
        seven = set()
        eight = set()
        nine = set()
        for o in digits:
            l = len(o)
            if l == 2:
                one = o
            elif l == 3:
                seven = o
            elif l == 4:
                four = o
            elif l == 7:
                eight = o

        for i in digits:
            if len(i) == 6:
                if not one.issubset(i):
                    six = i
                    continue
                middle = four - i
                if len(middle) == 1:
                    zero = i
                    continue
                nine = i
        for i in digits:
            if len(i) == 5:
                if one.issubset(i):
                    three = i
                    continue
                c_seg = nine - i
                if len(c_seg) == 1:
                    five = i
                    continue
                two = i

        total = 0
        for o in output:
            total *= 10
            if o == one:
                total += 1
            elif o == two:
                total += 2
            elif o == three:
                total += 3
            elif o == four:
                total += 4
            elif o == five:
                total += 5
            elif o == six:
                total += 6
            elif o == seven:
                total += 7
            elif o == eight:
                total += 8
            elif o == nine:
                total += 9

        print(total)
        result += total
print(result)
