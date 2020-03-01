import math
import matplotlib.pyplot as plt
n = 23
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
    
plt.figure(figsize=(9,4))
plt.xlabel('Longitud (mm)')
plt.ylabel('Fuerza cortante (N)')
plt.grid()
plt.plot(v,'-b')
plt.savefig('Fuerzacortante.pdf')

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
    if x > 130+2*n:
        aux = aux+(60000+200*n)
    if x>200+2*n:
        aux = aux-(5/36)*(x - (200+2*n))*(x - (200+2*n))*(x - (200+2*n))
    if x>=310+2*n:
        aux = aux + R2*(x-(310+2*n))
    m.append(aux)
   
plt.figure(figsize=(9,4))
plt.grid()
plt.xlabel('Longitud (mm)')
plt.ylabel('Momento flector (N-mm)')
plt.plot(m,'r')
plt.savefig('momento.pdf')

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
  
plt.figure(figsize=(9,4))
plt.grid()
plt.xlabel('Longitud (mm)')
plt.ylabel('Momento de inercia (mm$^4$)')
plt.plot(I,'-m')
plt.savefig('momentoi.pdf')


E = 2.1*10**5
MEI = []
for i in range(0,310+2*n+1):
    MEI.append(m[i]/(E*I[i]))
plt.figure(figsize=(9,4))
plt.grid()
plt.xlabel('Longitud (mm)')
plt.ylabel('M/EI (mm)')
plt.plot(MEI,'-b')
plt.savefig('mei.pdf')


mi = []
mi.append(0)
for i in range(1,310+2*n+1):
    mi.append(m[i]/I[i] + mi[i-1])
plt.figure(figsize=(9,4))
plt.xlabel('Longitud (mm)')
plt.ylabel('$\int M/I$ (N/mm$^{2}$)')
plt.grid()
plt.plot(mi)
plt.savefig('mintegr.pdf')


mii = []
mii.append(0)
for i in range(1,310+2*n+1):
    mii.append(mi[i]+mii[i-1])
plt.figure(figsize=(9,4))
plt.grid()
plt.xlabel('Longitud (mm)')
plt.ylabel('$ \iint M/I\,\mathrm{d}x $ (MPa-mm)')
plt.plot(mii)
plt.savefig('m2i.pdf')

const = -mii[310+2*n]/(310+2*n)
for i in range(0,310+2*n+1):
    mii[i] = (mii[i]+const*i)/E
plt.figure(figsize=(9,4))
plt.grid()
plt.xlabel('Longitud (mm)')
plt.ylabel('Deformada (mm)')
plt.plot(mii,'-k')
plt.savefig('def.pdf')

rect1 = []
rect2 = []
for i in range(0,40):
    rect1.append(-4.0824*10**(-4)*(i) - 2.4*10**-8)
    rect2.append(3.12*10**(-4)*(i+357-20) - 1.1110683*10**(-1))
indx = []
for i in range(357-20,357+20):
    indx.append(i)
plt.figure(figsize=(9,4))
plt.grid()
plt.xlabel('Longitud (mm)')
plt.ylabel('Deformada (mm)')
plt.plot(mii,'-k')
plt.plot(rect1)
plt.plot(indx,rect2)
plt.savefig('ang.pdf')

flechamax = 0
posflecha = 0
for i in range(0,310+2*n+1):
    flechamax = max(flechamax,abs(mii[i]))
for i in range(0,310+2*n+1):
    if(abs(mii[i]) == flechamax):
        posflecha = i
        
area = []
for i in range(0,310+2*n+1):
    if i<10:
        area.append(math.pi*(40/2))
        continue
    if i<80:
        area.append((math.pi*(50/2)))
        continue
    if i<200+2*n:
        area.append((math.pi*(((50+((i-80)*20/(120+2*n)))/2))))
        continue
    if i<260+2*n:
        area.append((math.pi*(70/2)))
        continue
    if i<300+2*n:
        area.append(math.pi*(60/2))
        continue
    area.append((math.pi*(55/2)))


esfm = 0
poses = 0
for i in range(0,310+2*n+1):
    if abs(math.sqrt(area[i]/math.pi)*m[i]/I[i]) > esfm:
        esfm = abs(math.sqrt(area[i]/math.pi)*m[i]/I[i])
        poses = i
print(esfm, poses)
#MPa

esfm = 0
poses = 0
gresf = []
for i in range(0,310+2*n+1):
    esff = abs(math.sqrt(area[i]/math.pi)*m[i]/I[i])
    gresf.append(math.sqrt(esff**2 + (v[i]/area[i])**2))
    if math.sqrt(esff**2 + (v[i]/area[i])**2) > esfm:
        esfm = math.sqrt(esff**2 + (v[i]/area[i])**2)
        poses = i
print(esfm, poses)


plt.figure(figsize=(10,5))
plt.grid()
plt.xlabel('Longitud (mm)')
plt.ylabel('Esfuerzo (MPa)')
plt.plot(gresf)
plt.savefig('esfuerzo.pdf')
