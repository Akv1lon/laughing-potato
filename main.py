# def strcounter(s):
#     for sy in set(s):
#         counter = 0
#         for s_sy in s:
#             if sy == s_sy:
#                 counter += 1  
#         print(sy, counter)
    
# strcounter('aabbcc')

<<<<<<< HEAD
#O(N**2) - 2 цикла

counter = {}
def strcounter(s):
    for sym in s:
        counter[sym] = counter.get(sym, 0) + 1
        
    for sym, count in counter.items():
        print(sym, count)
        
strcounter('aabbcccdd')
=======
#O(N**2) - 2 цикла(цикл в цикле)

counter = {}
 def strcounter(s):
     for sym in s:
         counter[sym] = counter.get(sym, 0) + 1
        
     for sym, count in counter.items():
         print(sym, count)
        
 strcounter('aabbcccdd')
>>>>>>> 3b1f82608307c2723510c8b8491dca7d8c89ece8

#O(N) - 1 цикл(2 необяз и может быть вне функции)
