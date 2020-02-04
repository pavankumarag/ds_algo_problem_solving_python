"""
You are given an array of integers representing the prices of single stock on various days(each index in the array
represents a different day), You are also given an integer k, which represents number of transactions you are allowed
to make. One transaction consists of buying the stock on the given day and selling it on another, later day
you can make buying and selling the stock, given k transactions.


Write a function that returns the maximum profit you can make buying and selling the stock, given k transactions.

Note that you can only hold 1 share
of the stock at a time; in other words, you cannot buy more than 1 share of the stock on any given
day, and you cannot buy a share of the stock if you are still holding another share. Note that you also
don't need to use all k transactions that you're allowed.


Sample input: [5, 11, 3, 50, 60, 90], 2
Sample output: 93 (Buy: 5, Sell: 11; Buy: 3, Sell: 90)
"""


def _max_profit_k_transactions(prices, k): # O(nk) time and O(nk) space
	if not len(prices):
		return 0
	profits = [[0 for i in prices] for j in range(k+1)]
	for i in range(1, k+1):
		max_thus_far = float('-inf')
		for j in range(1, len(prices)):
			max_thus_far = max(max_thus_far, profits[i-1][j-1] - prices[j-1])
			profits[i][j] = max(profits[i][j-1], max_thus_far + prices[j])
	return profits[-1][-1]


def _max_profit_k_transactions_optimised(prices, k): # O(nk) time and O(n) space
	if not len(prices):
		return 0
	even_profits = [0 for i in prices]
	odd_profits = [0 for j in prices]
	for i in range(1, k+1):
		max_thus_far = float('-inf')
		if i % 2 == 1:
			current_profits = odd_profits
			previous_profits = even_profits
		else:
			current_profits = even_profits
			previous_profits = odd_profits
		for j in range(1, len(prices)):
			max_thus_far = max(max_thus_far, previous_profits[j-1] - prices[j-1])
			current_profits[j] = max(current_profits[j-1], max_thus_far + prices[j])
	return even_profits[-1] if k %2 == 0 else odd_profits[-1]


if __name__ == "__main__":
	print _max_profit_k_transactions([5,11,3, 50, 60, 90], 2)
	print _max_profit_k_transactions_optimised([5,11,3, 50, 60, 90], 2)