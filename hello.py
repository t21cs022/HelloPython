'''


Created on 2023/10/13

@author: t21cs022
'''


print("Hello, Python world")
a = 10
b = 0.000001
c = 'string'
d = 10; e = 0.000001; f = "string"
# This is comment
print(a,b,c)
print(d,e,f)

#for文
for x in {1,2,3}:
    print(x)

n = 3; x = 0;
for i in range(n):
    print(x)
    x += 1
    
#if文
if 0 < x < 10:
    print('0 < x < 10')
else:
    print('x<=0, x>=10')

#while文
p = 0
while p < 3:
    print('p = ', p)
    p += 1

#quick_sort呼び出し
data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
from quick_sort import quick_sort
print(quick_sort(data))


