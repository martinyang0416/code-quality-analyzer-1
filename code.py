def maxProfit(k, prices):
    if not prices or k == 0:
        return 0
    n = len(prices)
    if k >= n // 2:
        # Greedy approach for unlimited transactions
        max_profit = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit
    else:
        # DP approach with limited transactions
        buy = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)
        for price in prices:
      