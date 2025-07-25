def find_min_loss(prices):
    best_loss = None
    answer = None
    n = len(prices)

    for i in range(n):
        for j in range(i+1, n):
            if prices[j] < prices[i]:
                loss = prices[i] - prices[j]
                if best_loss is None or loss < best_loss:
                    best_loss = loss
                    answer = (i+1, j+1, loss)

    return answer

def main():
    s = input("Enter projected prices for each year, separated by spaces: ").strip()
    parts = s.split()
    try:
        prices = [float(x) for x in parts]
    except ValueError:
        print("Invalid price list.")
        return

    res = find_min_loss(prices)
    if res:
        buy, sell, loss = res
        print(f"Buy in year {buy}, sell in year {sell}, loss = {loss}")
    else:
        print("No valid loss opportunity found.")

if __name__ == '__main__':
    main()
