nums={int(raw_input()):i for i in range(int(raw_input()))}
out=[None]*len(nums)
a=2
b=3
def gcd(x, y):
    x, y = min(x, y), max(x, y)
    while(x!= 0):
        x, y = y % x, x
    return y

while nums:
    for num in nums.keys():
        g = gcd(num,a)
        if gcd(num,a)>1:
            out[nums[num]]=a,g
            nums.pop(num)
    a,b = b,a+b
    
for f,d in out:
    print f, d