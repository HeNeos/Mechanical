import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from jupyterthemes import jtplot
jtplot.style()
import numpy as np
import pandas as pd
import math
%matplotlib inline
plt.rcParams['animation.ffmpeg_path'] = '/usr/bin/ffmpeg'

fig,ax = plt.subplots(figsize=(6,6))
plt.title("Lazy mechanism")
xdata,ydata = [], []

s = np.arange(0,213.5,1e-3)
t = s*0
plt.plot(s,t,'-b')
posi3x = []
posi3y = []
posi2x = []
posi2y = []
def test(frame,i):
    pp1 = 91*np.cos(frame)+250*np.cos(i)-213.5-166*np.cos(ff(frame))
    pp2 = 91*np.sin(frame)+250*np.sin(i)-166*np.sin(ff(frame))
    return 250*250-pp1*pp1-pp2*pp2
ln, = plt.plot([],[],'ro')
def init():
    ax.set_xlim(-180,400)
    ax.set_ylim(-320,280)
    return ln,
init()

plt.grid(True)

redDot1, = plt.plot([0],[np.sin(9)],'ro')
redDot2, = plt.plot([0],[np.sin(9)],'ro')
redDot3, = plt.plot([0],[np.sin(9)],'ro')

line1, = plt.plot([0],[np.sin(9)],'-b')
line2, = plt.plot([0],[np.sin(9)],'-b')
line3, = plt.plot([0],[np.sin(9)],'-b')
line4, = plt.plot([0],[np.sin(9)],'-b')

#frr = np.linspace(0,10*np.pi,2000+1)
frr = np.linspace(0,50,1000+1)

def ff(t):
    #return math.pi*(math.sin(math.sin(math.sin(t)+math.cos(t))))+math.log(1+t)
    return math.pi*(math.sin(math.sin(math.sin(t)+math.cos(t))))-math.pi*math.sin(math.sqrt(t))-math.exp(1)*math.cos(math.sqrt(t))
    #return 2*math.sin(math.sqrt(t))*math.log(1+math.sqrt(t))*math.sin(math.sqrt(t)*math.cos(math.sqrt(t)*math.sin(t)))
    #return math.sin(t*math.cos(t*math.sin(t)))
    #return math.exp(math.sqrt(t)*math.sin(math.sqrt(t))+math.cos(math.sqrt(t)))
    #return math.exp(math.sin(t))**0.8
    #return math.log(math.sin(t)+1.5+math.cos(t))
    
def upd(frame):
    redDot1.set_data(91*np.cos(frame),91*np.sin(frame))
    x1 = np.linspace(0,91*np.cos(frame),100)
    y1 = np.linspace(0,91*np.sin(frame),100)
    line1.set_data(x1,y1)
    
    redDot2.set_data(213.5+166*np.cos(ff(frame)),166*np.sin(ff(frame)))
    x2 = np.linspace(213.5,213.5+166*np.cos(ff(frame)),100)
    y2 = np.linspace(0,166*np.sin(ff(frame)),100)
    line2.set_data(x2,y2)
    
    l = 0
    r = np.pi
    for i in range(0,60):
        m1 = l+(r-l)/3
        m2 = r-(r-l)/3
        if(test(frame,m1) > 0):
            r = m1
        else:
            if(test(frame,m2) < 0):
                l = m2
            else:
                l = m1
                r = m2
    if(abs(test(frame,l)) > 1e-1):
        l = -np.pi
        r = 0
        for i in range(0,60):
            m1 = l+(r-l)/3
            m2 = r-(r-l)/3
            if(test(frame,m1) > 0):
                r = m1
            else:
                if(test(frame,m2) < 0):
                    l = m2
                else:
                    l = m1
                    r = m2
    
    value = l
    x3 = np.linspace(91*np.cos(frame),91*np.cos(frame)+250*np.cos(value),100)
    y3 = np.linspace(91*np.sin(frame),91*np.sin(frame)+250*np.sin(value),100)
    x4 = np.linspace(213.5+166*np.cos(ff(frame)),91*np.cos(frame)+250*np.cos(value),100)
    y4 = np.linspace(166*np.sin(ff(frame)),91*np.sin(frame)+250*np.sin(value),100)
    posi2x.append(213.5+166*np.cos(ff(frame)))
    posi2y.append(166*np.sin(ff(frame)))
    posi3x.append(91*np.cos(frame)+250*np.cos(value))
    posi3y.append(91*np.sin(frame)+250*np.sin(value))
    line3.set_data(x3,y3)
    line4.set_data(x4,y4)
    redDot3.set_data(91*np.cos(frame)+250*np.cos(value),91*np.sin(frame)+250*np.sin(value))
    plt.plot(91*np.cos(frame)+250*np.cos(value), 91*np.sin(frame)+250*np.sin(value), marker='o', markersize=2, color="white")
    plt.plot(213.5+166*np.cos(ff(frame)),166*np.sin(ff(frame)), marker='o', markersize=2, color="yellow")
    plt.plot(91*np.cos(frame),91*np.sin(frame), marker='o', markersize=2, color="green")
    return redDot1,redDot2,redDot3,line1,line2,line3,line4,

ani = FuncAnimation(fig,upd,frames=frr,blit=True)
ani.save('test.mp4',writer='ffmpeg',fps=50,dpi=300)
plt.show()
