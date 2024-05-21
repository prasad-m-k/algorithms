from typing import List
from collections import defaultdict
import pandas as pd
import numpy as np

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ret = []
                

        print("Final answer", ret)


accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

Solution().accountsMerge(accounts)
        


'''
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

'''


"""
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        acc = defaultdict(str)
        for account in accounts:
            #print(account)
            mails = set(account[1:])
            if account[0] in acc:
                mails = mails | acc[account[0]]
            
            acc[account[0]] = mails

        ret = []
        for k, v in acc.items():
            y=[k]
            for x in v:
                y.append(x)
            ret.append(y)
                

        print("Final answer", ret)

        
"""