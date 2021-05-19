def D_H(x):
    h='0123456789ABCDEF'
    out=[]
    while x>0:
        out+=h[x%16],
        x=x//16
    return ''.join(out[::-1])
print(D_H(31))