def  findPotentialInsiderTraders(datafeed):
    if not datafeed:
        return
    threshold = 5000000
    date_diff = 2

    from collections import deque

    buys = deque()
    sells = deque()
    line = datafeed[0]
    prev_day, price = map(int, line.strip().split('|'))
    prices = {}
    prices[prev_day] = price
    violators = set()
    suspicious_trade = []
    for line in datafeed[1:]:
        tokens = line.split('|')
        day = int(tokens[0])
        if len(tokens) > 2:
            trader = tokens[1]
            action = tokens[2]
            amnt = int(tokens[3])
            if action == "BUY" and trader not in violators:
                buys.append((day, trader, amnt))
            elif action == "SELL" and trader not in violators:
                sells.append((day, trader, amnt))
        else:
            price = int(tokens[1])
            prices[day] = price

            while buys and day - buys[0][0] > date_diff:
                if buys[0][0] in prices:
                    del prices[buys[0][0]]
                buys.popleft()
            while sells and day - sells[0][0] > date_diff:
                if sells[0][0] in prices:
                    del prices[sells[0][0]]
                sells.popleft()

            # considers buys
            for trade in buys:
                diff = price - prices[trade[0]]
                profit = diff * trade[2]
                if profit > threshold:
                    if trade[1] not in violators:
                        violators.add(trade[1])
                        suspicious_trade.append(tuple(trade[:2]))

            # consider sells
            for trade in sells:
                diff = price - prices[trade[0]]
                profit = (-diff) * trade[2]
                if profit > threshold:
                    if trade[1] not in violators:
                        violators.add(trade[1])
                        suspicious_trade.append(tuple(trade[:2]))

    return map(lambda x: "|".join((str(x[0]), x[1])), sorted(suspicious_trade))
