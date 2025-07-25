def merge_positioned(list1, list2):

    combined = list1 + list2
    combined.sort(key=lambda x: x['positions'][0])

    result = []
    for item in combined:
        if not result:
            result.append({
                'positions': item['positions'][:],
                'values':    item['values'][:]
            })
            continue

        prev = result[-1]
        L1, R1 = prev['positions']
        L2, R2 = item['positions']
        overlap = max(0, min(R1, R2) - max(L1, L2))
        w1, w2 = R1 - L1, R2 - L2

        if overlap > 0 and (overlap > w1/2 or overlap > w2/2):
            prev['values'].extend(item['values'])
        else:
            result.append({
                'positions': item['positions'][:],
                'values':    item['values'][:]
            })

    return result

def main():
    try:
        n1 = int(input("How many elements in the first list? ").strip())
    except ValueError:
        print("Invalid number.")
        return

    list1 = []
    for i in range(n1):
        parts = input(f"  Element {i+1} positions (left right): ").split()
        if len(parts) != 2:
            print("  Enter two integers.")
            return
        left, right = int(parts[0]), int(parts[1])
        vals = input("    Enter values separated by commas: ").split(',')
        vals = [v.strip() for v in vals if v.strip()]
        list1.append({'positions':[left, right], 'values':vals})

    try:
        n2 = int(input("How many elements in the second list? ").strip())
    except ValueError:
        print("Invalid number.")
        return

    list2 = []
    for i in range(n2):
        parts = input(f"  Element {i+1} positions (left right): ").split()
        if len(parts) != 2:
            print("  Enter two integers.")
            return
        left, right = int(parts[0]), int(parts[1])
        vals = input("    Enter values separated by commas: ").split(',')
        vals = [v.strip() for v in vals if v.strip()]
        list2.append({'positions':[left, right], 'values':vals})

    merged = merge_positioned(list1, list2)
    print("\nMerged result:")
    for elem in merged:
        print(elem)

if __name__ == '__main__':
    main()
