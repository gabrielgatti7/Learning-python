# set = collection which is unordered, unindexed. No dulicate values

set1 = {1,2,3,4,5}
set2 = {'a', 'b', 'c'}

set2.add(1)
set1.remove(4)
# set2.update(set1)
set3 = set1.union(set2)

print(set1)
print(set2)
print(set3)
# for element in set2:
#     print(element)

print(set1.difference(set2))
print(set1.intersection(set2))