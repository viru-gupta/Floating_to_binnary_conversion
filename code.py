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
    if a<=63:
        i=6
    elif a<=1023:
        i=10
    elif a<=4096*2-1:
        i=12
    elif a<=16384*2-1:
        i=16
    for _ in range(i-1,-1,-1):
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
