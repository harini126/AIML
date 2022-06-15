import main_pack as mp
import main_pack.subpack1 as s1
import main_pack.subpack2 as s2
from main_pack.subpack2 import arithmetic as ar2
from main_pack.subpack1 import arithmetic1 as ar1

print(mp.m)
print(mp.mainpackdemo())
print(s1.sub)
print(s1.subpackdemo())
print(s2.sub)
print(s2.subpackdemo())
print(ar2.add(3,5))
print(ar1.sub(8,5))