import mpld3
from mpld3 import plugins
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

pi=3.14159265
nSampleNum = 5120
ncount = 2048.0
df = nSampleNum / ncount
sampleTime = ncount / nSampleNum
freqLine = 800
x = np.linspace(0,sampleTime,ncount)#时域波形x轴坐标
sinx = np.sin(2*pi*250*x)
sinx2 = 0.5*np.sin(2*pi*500*x)
sinx3 = 0.3*np.sin(2*pi*1000*x)    #以上是三个标准正弦波形

sinx += sinx2
sinx += sinx3  #叠加一个时域波形

fft = np.fft.fft(sinx)[0:freqLine]  #调用fft变换算法计算频域波形
fftx = np.linspace(0,df*freqLine,freqLine)  #频域波形x轴坐标311)

fig,ax = plt.subplots()

subplot(311)
plot(x,sinx)
xlabel('time(s)')
ylabel('amplitude')
title('time domain graph')

subplot(313)
plot(fftx,abs(fft))
xlabel('freqency(Hz)')
ylabel('amplitude')
title('frequency domain graph')

show(fig)

Shtml=mpld3.fig_to_html(fig)
fh = open('DAC/templates/fig/fig003.html', 'w')
fh.write('{% extends "demo/btn.html"  %}\n{% block content %}\n')
fh.write(Shtml)
fh.write('\n {% endblock %}')
print(fh)
fh.close()

show()