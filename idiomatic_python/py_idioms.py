#enumerate

for i, d in enumerate(days):
    print (i,d)
    
'''
o/p
0 Monday
1 Tuesday
2 Wednesday
3 Thursday
4 Friday
5 Saturday
6 Sunday
'''

#zip
numList = [1, 2, 3]
strList = ['one', 'two', 'three']
for n,s in zip(numList, strList):
    print (n, s)
    
o/p
'''
1 one
2 two
3 three
'''
