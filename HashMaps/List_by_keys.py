
Tv = {'TMKUC' : 88, 'BreakingBad':100, 'GameOfThrones':1292}

print(Tv)

mxkey = max(Tv, key=lambda x : Tv[x])

print(mxkey)
print(sorted(list(Tv.keys())))