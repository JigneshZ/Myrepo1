def calc(a,b):
    sum=a+b
    sub=a-b
	mul=a*b
	div=a/b
    return sum,sub,mul,div
t = calc(500,30)
print(type(t))
for x in t:
	print(x)