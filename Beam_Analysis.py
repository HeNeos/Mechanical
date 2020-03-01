import math
import matplotlib.pyplot as plt
for ka in range(1,30):
    n = 100*ka
    R2 = 5*(2*n*n + 1135*n + 110780)/(n+155)
    R1 = 7340-60*n-R2
    v = []
    v.append(0)
    for x in range(1,310+2*n+1):
        aux = R1
        if x>10:
            aux = aux-(12-n)*(x-10)
        if x>130+2*n:
            aux = aux-(5000+10*n)
        if x>80:
            aux = aux + (12-n)*(x-80)
        if x>260+2*n:
            aux = aux+(50)*(x-(260+2*n)) + (5/12)*(x-(260+2*n))*(x-(260+2*n))
        if x>200+2*n:
            aux = aux-(5/12)*(x - (200+2*n))*(x - (200+2*n))
        if x>=310+2*n:
            aux = aux + R2
        v.append(aux)
    m = []
    for x in range(0,310+2*n+1):
        aux = R1*x
        if x>10:
            aux = aux-(12-n)*(x-10)*(x-10)/2
        if x>130+2*n:
            aux = aux-(5000+10*n)*(x-(130+2*n))
        if x>80:
            aux = aux + (12-n)*(x-80)*(x-80)/2
        if x>260+2*n:
            aux = aux+(25)*(x-(260+2*n))*(x-(260+2*n)) + (5/36)*(x-(260+2*n))*(x-(260+2*n))*(x-(260+2*n))
        if x > 140+n:
            aux = aux+(60000+200*n)
        if x>200+2*n:
            aux = aux-(5/36)*(x - (200+2*n))*(x - (200+2*n))*(x - (200+2*n))
        if x>=310+2*n:
            aux = aux + R2*(x-(310+2*n))
        m.append(aux)
    I = []
    for i in range(0,310+2*n+1):
        if i<10:
            I.append((math.pi*(40)**4)/64)
            continue
        if i<80:
            I.append((math.pi*(50)**4)/64)
            continue
        if i<200+2*n:
            I.append((math.pi*(((50+((i-80)*20/(120+2*n))))**4)/64))
            continue
        if i<260+2*n:
            I.append((math.pi*(70)**4)/64)
            continue
        if i<300+2*n:
            I.append((math.pi*(60)**4)/64)
            continue
        I.append((math.pi*(55)**4)/64)
    mi = []
    mi.append(0)
    for i in range(1,310+2*n+1):
        mi.append(m[i]/I[i] + mi[i-1])
    mii = []
    mii.append(0)
    for i in range(1,310+2*n+1):
        mii.append(mi[i]+mii[i-1])
    const = -mii[310+2*n]/(310+2*n)
    for i in range(0,310+2*n+1):
        mii[i] = (mii[i]+const*i)/E
    plt.figure(figsize=(10,5))
    plt.grid()
    plt.xlabel('Longitud (mm)')
    plt.ylabel('Deformada (mm)')
    plt.plot(mii,'-k')
    sv = 'defj'
    sv = sv+str(n)
    plt.savefig(sv,dpi=300)
