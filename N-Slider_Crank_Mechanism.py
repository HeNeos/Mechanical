import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#from jupyterthemes import jtplot
#jtplot.style()
import numpy as np
import pandas as pd
import math
from random import seed
from random import randint
%matplotlib inline
plt.rcParams['animation.ffmpeg_path'] = '/usr/bin/ffmpeg'
#import matplotlib.animation as animation
#plt.rcParams['animation.ffmpeg_path'] = '/usr/local/bin/ffmpeg'

fig,ax = plt.subplots(figsize=(6,6))
plt.title("PLANEtarium")
xdata,ydata = [], []

plt.plot([0],[0],'ro')

ln, = plt.plot([],[],'ro')
def init():
    ax.set_xlim(-80,80)
    ax.set_ylim(-80,80)
    return ln,
init()

plt.grid(True)


npoints = 25
Vertex = []
Bars = []
LenBars = []

for i in range(0,npoints+1):
    redDot, = plt.plot([0],[np.sin(9)],'ro')
    Vertex.append(redDot)
    line, = plt.plot([0],[np.sin(9)],'-b')
    Bars.append(line)
LenBars.append(10)
for i in range(0,npoints):
    LenBars.append(randint(30,50))
    #LenBars.append(30)
circangle = np.arange(0,2*math.pi,0.001)
circx = np.cos(circangle)*LenBars[0]
circy = np.sin(circangle)*LenBars[0]
plt.plot(circx,circy,'-w')
for i in range(0,npoints):
    anglee = (2*math.pi/npoints)*(i)
    lline = -LenBars[0]+LenBars[i+1]-5
    rline = LenBars[0]+LenBars[i+1]+5
    if(abs(anglee-math.pi/2) < 0.001):
        posy = np.arange(lline,rline)
        posx = posy*0
        plt.plot(posx,posy,'-y')
        continue
    if(abs(anglee-3*math.pi/2) < 0.001):
        posy = np.arange(-lline,-rline)
        posx = posy*0
        plt.plot(posx,posy,'-y')
        continue    
    ll = min(lline*math.cos(anglee),rline*math.cos(anglee))
    rr = max(lline*math.cos(anglee),rline*math.cos(anglee))
    posx = np.arange(ll,rr,0.05)
    posy = posx*math.tan(anglee)
    plt.plot(posx,posy,'-y')

frr = np.linspace(0,10,800+1)
def ff(t):
    return t**2
    #return t

def upd(frame):
    if(frame%1 == 0):
        print(frame)
    Vertex[0].set_data(LenBars[0]*np.cos(ff(frame)),LenBars[0]*np.sin(ff(frame)))
    x1 = np.linspace(0,LenBars[0]*np.cos(ff(frame)),100)
    y1 = np.linspace(0,LenBars[0]*np.sin(ff(frame)),100)
    Bars[0].set_data(x1,y1)
    
    BarArmy = LenBars[0]*np.sin(ff(frame))
    BarArmx = LenBars[0]*np.cos(ff(frame))
    
    AngleSeparation = 2*math.pi/npoints
    for i in range(1,npoints+1):
        CurrentAngle = AngleSeparation*(i-1)
        CurrentTangent = math.tan(CurrentAngle) # yi/xi
        CurrentDistance = LenBars[i]
        def tests(i):
            return (BarArmx)**2 + (i-BarArmy)**2
        if(abs(CurrentAngle-math.pi/2) < 0.001):
            minposy = BarArmy
            l = BarArmy
            r = 100000
            for j in range(0,50):
                m = l+(r-l)/2
                if(tests(m) > CurrentDistance**2):
                    r = m
                else:
                    l = m
            Vertex[i].set_data(0,l)
            xi = np.linspace(BarArmx,0,100)
            yi = np.linspace(BarArmy,l,100)
            Bars[i].set_data(xi,yi)
            continue
        if(abs(CurrentAngle-3*math.pi/2) < 0.001):    
            minposy = BarArmy
            r = BarArmy
            l = -100000
            for j in range(0,50):
                m = l+(r-l)/2
                if(tests(m) < CurrentDistance**2):
                    r = m
                else:
                    l = m
            Vertex[i].set_data(0,l)
            xi = np.linspace(BarArmx,0,100)
            yi = np.linspace(BarArmy,l,100)
            Bars[i].set_data(xi,yi)
            continue
                
        MaximuxX = (LenBars[0] + LenBars[i])*math.cos(CurrentAngle)
        MinimumX = (-LenBars[0] + LenBars[i])*math.cos(CurrentAngle)
        l = -10000
        r = 10000
        def test(i):
            return (i-BarArmx)**2 + (CurrentTangent*i-BarArmy)**2
        for j in range(0,40):
            m1 = l+(r-l)/3
            m2 = l + 2*(r-l)/3
            #print(j,l,r,m1,m2,test(m1),test(m2))
            if(test(m1) > test(m2)):
                l = m1
            else:
                r = m2
        if(CurrentAngle < math.pi/2 or CurrentAngle > 3*math.pi/2):
            r = 10000
        else:
            r = -10000
        for j in range(0,50):
            m = (l + r)/2
            if(test(m) > CurrentDistance**2):
                r = m
            else:
                l = m
        Vertex[i].set_data(l,l*CurrentTangent)
        xi = np.linspace(BarArmx,l,100)
        yi = np.linspace(BarArmy,l*CurrentTangent,100)
        Bars[i].set_data(xi,yi)
    for i in range(0,npoints+1):
        return Vertex[i],Bars[i],
ani = FuncAnimation(fig,upd,frames=frr,blit=True)
ani.save('Planetary40.mp4',writer='ffmpeg',fps=60,dpi=300)
plt.show()
