from typing import List

class MakingChange:
    def __init__(self, coins: List[int]):
        self._coins = coins
        
    def change1(self, n: int):
        dp = [0] * (n+1)
        return self.top_down_change_helper(n, dp)
        
    def top_down_change_helper(self, n: int, dp: List[int]):
        #print(dp)
        if n == 0:
            return 0
        if dp[n] == 0:
            min_coins = float("inf")
            # Try each different coin to see which is best
            for coin in self._coins:
                if n - coin >= 0:
                    curr_min = self.top_down_change_helper(n-coin, dp)
                    min_coins = min(min_coins, curr_min)
            dp[n] = min_coins + 1
        print(dp)
        return dp[n]
        
    def change(self, n: int):
        dp = [0] * (n+1)
        print(dp)
        for i in range(1, n+1):
            min_coins = float("inf")

            # Try removing each coin from the total and see which requires
            # the fewest additional coins
            for coin in self._coins:
                if i - coin >= 0:
                    #print(i, coin, dp)
                    min_coins = min(min_coins, dp[i - coin])
                    #print(f"loop {i} coin={coin}, min={min_coins}, [i-coin]={i - coin}, dp[i-coin]{dp[i - coin]} {dp}")
            dp[i] = min_coins + 1
            #print(f"loop {i} coin={coin}, min={min_coins}, few={i - coin}, {dp[i - coin]} {dp}")
        
        print(dp)
        return dp[n]
    
    
american_coins = [25, 10, 7, 5, 1]
random_coins = [10, 6, 1]

change=MakingChange(american_coins)
print(change.change(237))