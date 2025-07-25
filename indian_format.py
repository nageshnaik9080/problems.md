def format_indian_number(num):
    """
    Convert a number (int or float) into Indian‑style comma format.
    E.g. 123456.789 → "1,23,456.789"
    """
    s = str(num)
    if 'e' in s or 'E' in s:
        s = format(num, 'f')
    sign = ''
    if s.startswith('-'):
        sign, s = '-', s[1:]
    if '.' in s:
        int_part, frac_part = s.split('.', 1)
    else:
        int_part, frac_part = s, ''
    if len(int_part) > 3:
        head, tail = int_part[:-3], int_part[-3:]
        groups = []
        while head:
            groups.insert(0, head[-2:])
            head = head[:-2]
        int_fmt = ','.join(groups) + ',' + tail
    else:
        int_fmt = int_part

    return sign + int_fmt + ('.' + frac_part if frac_part else '')

def main():
    user_input = input("Enter a number to format:-").strip()
    try:
        num = float(user_input)
    except ValueError:
        print("Invalid number.")
        return

    print("Formatted ""Indian style"":-", format_indian_number(num))

if __name__ == '__main__':
    main()
