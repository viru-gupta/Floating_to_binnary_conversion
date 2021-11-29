#viru binary algorithm
def bin_deci(a):
    ans=''
    i=int(input('enter the number floating digits: '))
    for _ in range(1,i+1):
        if a>=2**-_:
            a-=2**-_
            ans+='1'
        else:
            ans+='0'
    return (ans)
def bin_inti(a):
    ans=''
    i=50
    while a<((2**i)*2):
        i-=1
    for _ in range(i+1,-1,-1):
        if a>=2**_:
            a-=2**_
            ans+='1'
        else:
            ans+='0'
    return (ans)
inp=float(input('Enter a decimal number: '))
inti,point=str(inp).split('.')
point='0.'+point
re=bin_inti(int(inti))
fl=bin_deci(float(point))
res=re+'.'+fl
print(f"Binary Number IS - b'{res}")
